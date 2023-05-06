import json
import pandas as pd

history = pd.read_csv('./data/history_filtered.csv')
history['checkout_gmt'] = pd.to_datetime(history['checkout_gmt'])
history = history[history['checkout_gmt'].dt.year >= 2020]
history = history.reset_index(drop=True)
history = history[["bib_record_metadata_id","patron_record_metadata_id"]]
history.index += 1

book = pd.read_csv('./data/book_filtered.csv',usecols=["bib_record_id", "best_title"])
book = book.rename(columns={'bib_record_id': 'bib_record_metadata_id'})
# book = book[book['bib_record_metadata_id'].isin(history['bib_record_metadata_id'].values.tolist())]
book = book.reset_index(drop=True)
book.index += 1 
book['bookID'] = book.index

patron = pd.read_csv('./data/patron_filtered.csv',usecols=["id"])
patron = patron.rename(columns={'id': 'patron_record_metadata_id'})
patron = patron[patron['patron_record_metadata_id'].isin(history['patron_record_metadata_id'].values.tolist())]
patron = patron.reset_index(drop=True)
patron.index += 1
patron['userID'] = patron.index

merged_history = pd.merge(history, book, on='bib_record_metadata_id')
merged_history = pd.merge(merged_history, patron, on='patron_record_metadata_id')
merged_history = merged_history[['bookID','userID']]
merged_history = merged_history.reset_index(drop=True)
merged_history.index += 1 
merged_history['borrowId'] = merged_history.index

bookToSubject = pd.read_csv('./data/sierra_view_subfield_subjectterms_202301181521.csv', usecols=["record_id", "content"],dtype={"content": str})
bookToSubject = bookToSubject.drop_duplicates()
bookToSubject = bookToSubject[bookToSubject['content'].notna()]
bookToSubject = bookToSubject[bookToSubject['record_id'].isin(book['bib_record_metadata_id'].values.tolist())]
bookToSubject = bookToSubject.rename(columns={'record_id': 'bib_record_metadata_id'})

bookToSubject['content'] = bookToSubject['content'].apply(lambda x: x.strip())
bookToSubject['content'] = bookToSubject['content'].apply(lambda x: x.split(','))
bookToSubject = bookToSubject.explode('content')
bookToSubject = bookToSubject[bookToSubject['content'].str.contains("etc") == False]
bookToSubject['content'] = bookToSubject['content'].apply(lambda x: x.lower())

subject = bookToSubject[['content']]
subject = subject.drop_duplicates()
subject = subject.reset_index(drop=True)
subject.index += 1
subject['subjectID'] = subject.index

bookToSubject = pd.merge(bookToSubject, book, on='bib_record_metadata_id')
bookToSubject = pd.merge(bookToSubject, subject, on='content')
bookToSubject = bookToSubject[['bookID','subjectID']]
bookToSubject = bookToSubject.drop_duplicates()

faculty = pd.read_csv('./data/faculty_data.csv')
faculty.index += 1 
faculty['facultyID'] = faculty.index

department = pd.read_csv('./data/faculty_department_map.csv')
department["department_dict"] = department["department_dict"].apply(json.loads)
department = department.explode('department_dict')
department[['department_name', 'department_code']] = department['department_dict'].apply(lambda x: pd.Series([list(x.items())[0][0], list(x.items())[0][1][0]]))
department = pd.merge(department, faculty, on='faculty_id')
department = department.loc[:, ['facultyID', 'department_name', 'department_code']]
department.index += 1 
department['departmentID'] = department.index

departmentBook = pd.read_csv('./data/department_book_map.csv', dtype={'faculty_department_id': object})
departmentBook = departmentBook.rename(columns={'faculty_department_id': 'department_code'})
departmentBook = pd.merge(departmentBook, department, on='department_code')
departmentBook = departmentBook.loc[:, ['departmentID', 'bookID']]

with open('./data/book.sql', 'w') as f:
    for index, row in book.iterrows():
        name = row['best_title'].replace("'", "''").replace('"', '\\"')
        f.write(f"insert into Book (id, name, bibRecord) values ({row['bookID']}, \"{name}\", \"{row['bib_record_metadata_id']}\");\n")

with open('./data/user.sql', 'w') as f:
    for index, row in patron.iterrows():
        f.write(f"insert into User (id, patronRecord) values ({row['userID']}, \"{row['patron_record_metadata_id']}\");\n")

with open('./data/userTOBook.sql', 'w') as f:
    for index, row in merged_history.iterrows():
        f.write(f"insert into UserToBook (id,userId, bookId) values ({row['borrowId']},{row['userID']}, {row['bookID']});\n")

with open('./data/subject.sql', 'w') as f:
    for index, row in subject.iterrows():
        name = row['content'].replace("'", "''").replace('"', '\\"')
        f.write(f"insert into Subject (id, name) values ({row['subjectID']}, \"{name}\");\n")

with open('./data/bookToSubject.sql', 'w') as f:
    for index, row in bookToSubject.iterrows():
        f.write(f"insert into BookToSubject (bookId, subjectId) values ({row['bookID']}, {row['subjectID']});\n")

with open('./data/faculty.sql', 'w') as f:
    for index, row in faculty.iterrows():
        f.write(f"insert into faculty (id, name) values ({row['facultyID']}, '{row['faculty_name']}');\n")

with open('./data/department.sql', 'w') as f:
    for index, row in department.iterrows():
        f.write(f"insert into department (id, name, facultyId, code) values ({row['departmentID']}, '{row['department_name']}',{row['facultyID']}, '{row['department_code']}');\n")

with open('./data/departmentBook.sql', 'w') as f:
    for index, row in departmentBook.iterrows():
        f.write(f"insert into departmentBook (departmentId, bookId) values ({row['departmentID']}, {row['bookID']});\n")

print("done")
import pandas as pd

history = pd.read_csv('./data/history_filtered.csv')
history['checkout_gmt'] = pd.to_datetime(history['checkout_gmt'])
history = history[history['checkout_gmt'].dt.year >= 2020]
history = history.reset_index(drop=True)
history = history[["bib_record_metadata_id","patron_record_metadata_id"]]
history.index += 1

book = pd.read_csv('./data/book_filtered.csv',usecols=["bib_record_id", "best_title"])
book = book.rename(columns={'bib_record_id': 'bib_record_metadata_id'})
book = book[book['bib_record_metadata_id'].isin(history['bib_record_metadata_id'].values.tolist())]
book.index += 1 
book['bookID'] = book.index

patron = pd.read_csv('./data/patron_filtered.csv',usecols=["id"])
patron = patron.rename(columns={'id': 'patron_record_metadata_id'})
patron = patron[patron['patron_record_metadata_id'].isin(history['patron_record_metadata_id'].values.tolist())]
patron.index += 1
patron['userID'] = patron.index

merged_history = pd.merge(history, book, on='bib_record_metadata_id')
merged_history = pd.merge(merged_history, patron, on='patron_record_metadata_id')
merged_history = merged_history[['bookID','userID']]

bookToSubject = pd.read_csv('./data/sierra_view_subfield_subjectterms_202301181521.csv', usecols=["record_id", "content"],dtype={"content": str})
bookToSubject = bookToSubject.drop_duplicates()
bookToSubject = bookToSubject[bookToSubject['content'].notna()]
bookToSubject = bookToSubject[bookToSubject['record_id'].isin(book['bib_record_metadata_id'].values.tolist())]
bookToSubject = bookToSubject.rename(columns={'record_id': 'bib_record_metadata_id'})

subject = bookToSubject[['content']]
subject = subject.reset_index(drop=True)
subject.index += 1
subject['subjectID'] = subject.index

bookToSubject = pd.merge(bookToSubject, book, on='bib_record_metadata_id')
bookToSubject = pd.merge(bookToSubject, subject, on='content')
bookToSubject = bookToSubject[['bookID','subjectID']]

with open('./data/book.sql', 'w') as f:
    for index, row in book.iterrows():
        name = row['best_title'].replace("'", "''").replace('"', '\\"')
        f.write(f"insert into Book (id, name, bibRecord) values ({row['bookID']}, \"{name}\", \"{row['bib_record_metadata_id']}\");\n")

with open('./data/user.sql', 'w') as f:
    for index, row in patron.iterrows():
        f.write(f"insert into User (id, patronRecord) values ({row['userID']}, \"{row['patron_record_metadata_id']}\");\n")

with open('./data/userTOBook.sql', 'w') as f:
    for index, row in merged_history.iterrows():
        f.write(f"insert into UserToBook (userId, bookId) values ({row['userID']}, {row['bookID']});\n")

with open('./data/subject.sql', 'w') as f:
    for index, row in subject.iterrows():
        name = row['content'].replace("'", "''").replace('"', '\\"')
        f.write(f"insert into Subject (id, name) values ({row['subjectID']}, \"{name}\");\n")

with open('./data/bookToSubject.sql', 'w') as f:
    for index, row in bookToSubject.iterrows():
        f.write(f"insert into BookToSubject (bookId, subjectId) values ({row['bookID']}, {row['subjectID']});\n")

print("done")
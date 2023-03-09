FROM python:3.9

WORKDIR /code

COPY ./backend/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY /backend /code/app

EXPOSE 3000

CMD ["uvicorn", "app.index:app", "--reload"]
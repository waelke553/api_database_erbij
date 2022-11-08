FROM python:3.10.0-slim
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./myproject /code
# Dit is gedaan zodat we van de folder een volume te maken. Dit doen we voordat python dit gaat doen!!
RUN mkdir -p /code/sqlitedb
CMD ["uvicorn", "myproject.main:main", "--host", "0.0.0.0", "--port", "8000"]

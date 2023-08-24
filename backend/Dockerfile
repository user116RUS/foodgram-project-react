FROM python:3.10

WORKDIR /app

COPY req.txt .

RUN pip install -r req.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:9000" ]
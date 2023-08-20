FROM python:3.9

WORKDIR /app

COPY req.txt .

RUN pip install -r req.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "foodgram_backend.wsgi"]
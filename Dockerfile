FROM python:3.10-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=run.py
ENV FLASK_ENV=production

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "run:app"]

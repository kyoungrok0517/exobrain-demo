FROM python

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]


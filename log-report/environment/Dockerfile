FROM python@sha256:a9e4190f02729f01e5b3719bd8b3ea0f8d9350dc17d01a1ce1ca6e3fbfcf7a99

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-report==1.5.0

WORKDIR /app

COPY access.log /app/access.log

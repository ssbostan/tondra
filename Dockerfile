ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION

WORKDIR /opt/app

COPY requirements.txt .
RUN pip install -r requirements.txt

ARG APP_VERSION
ARG APP_LCOMMIT

RUN echo "$APP_VERSION:$APP_LCOMMIT" > .appinfo

COPY . .

RUN adduser -D tondra
USER tondra

EXPOSE 8080

CMD gunicorn --no-sendfile \
  --bind 0.0.0.0:8080 \
  --access-logfile - --error-logfile - \
  --workers 4 app:app

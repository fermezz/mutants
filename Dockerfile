FROM python:3.8-slim-buster

RUN pip install -U \
      pipenv \
      dnspython

COPY Pipfile Pipfile.lock /app/
ENV PIPENV_PIPFILE /app/Pipfile
RUN pipenv install --system --deploy

COPY . /app/

WORKDIR /app/

ENV FLASK_ENV production

CMD ["gunicorn", "-c", "conf/gunicorn.conf.py", "flaskr:create_app()"]

FROM python:3.8-slim-buster

RUN pip install -U pipenv

COPY Pipfile Pipfile.lock /app/
ENV PIPENV_PIPFILE /app/Pipfile
RUN pipenv install --system --deploy

COPY . /app/

WORKDIR /app/

CMD ["gunicorn", "-c", "gunicorn.conf.py", "flaskr:create_app()"]

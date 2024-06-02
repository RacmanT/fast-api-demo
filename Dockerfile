FROM python:slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app /code/app

CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0"]
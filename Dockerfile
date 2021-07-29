FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

RUN mkdir -p /vol/web/media /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
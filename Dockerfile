FROM python:3.7-alpine
RUN apk update && apk add python3-dev \
                        gcc \
                        libffi-dev \
                        libc-dev
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]

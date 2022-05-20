FROM python:3.9-slim

WORKDIR /usr/src/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]
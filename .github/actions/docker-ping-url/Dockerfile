FROM python:alpine3.19
WORKDIR /app

COPY requirements.txt .


RUN python -V

RUN pip install --no-cache -r requirements.txt

COPY . .

CMD [ "python" ,"/app/main.py"] 
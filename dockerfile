FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -U prettytable

CMD [ "python3", "app.py" ]
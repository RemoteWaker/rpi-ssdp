FROM python:3-alpine

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

EXPOSE 1900/udp
VOLUME [ "/data" ]

CMD ["python", "main.py"]
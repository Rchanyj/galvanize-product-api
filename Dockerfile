FROM python:3.7
WORKDIR /app

ADD api/requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

ENV PYTHONUNBUFFERED 1
ADD api /app
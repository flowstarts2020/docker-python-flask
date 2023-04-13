FROM python:3
WORKDIR /Users/User/Docker-flask/trying-0.1
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python", "./app.py"]
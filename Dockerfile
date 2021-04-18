FROM python:3.9.4
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY Task1.py .
EXPOSE 5000
CMD ["python", "./Task1.py"]


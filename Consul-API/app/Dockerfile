FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=main.py
CMD ["gunicorn", "--bind", "0.0.0.0:6000", "--access-logfile", "-", "--error-logfile", "-", "main:app"]

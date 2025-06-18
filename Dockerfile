# Minimalistic Python Image
FROM python:3.11-slim

# Set Workdirectory in container
WORKDIR /app

# first copy and ...
COPY requirements.txt .
# install requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other Code
COPY . .

# Start Flask-Server
CMD ["python", "flaskserver.py"]

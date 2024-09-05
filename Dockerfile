FROM python:3.12-slim

# Install system dependencies for mysqlclient
RUN apt-get update && \
    apt-get install -y \
    gcc \
    pkg-config \
    libmariadb-dev \
    vim \
    && apt-get clean

# Define virtual directory
WORKDIR /app

# Copy requirements
COPY requirements.txt requirements.txt

# Install requirements
RUN pip3 install -r requirements.txt

# Copy all files into virtual directory
COPY . .

CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:4450"]
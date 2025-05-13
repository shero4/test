# Sample Dockerfile
FROM python:3.9-slim
LABEL maintainer="24f2008495@ds.study.iitm.ac.in"

# Set the working directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies (adjust based on your project)
RUN pip install -r requirements.txt

# Set the default command
CMD ["python", "main.py"]

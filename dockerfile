# Use a more recent, slim version of Python for a smaller image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy dependency file and install python packages

# Copy the rest of the application code
COPY . .

CMD ["python3", "app.py", "|", "pip", "-r", "requirements.txt"]


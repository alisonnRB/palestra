# Use a more recent, slim version of Python for a smaller image
FROM python:3.11-slim

# Install Tkinter system dependencies before copying app code
# This layer will be cached and won't re-run on every code change
COPY requirements.txt .
RUN requirements.txt && rm requirements.txt

# Set the working directory
WORKDIR /app

# Copy dependency file and install python packages

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["python3", "app.py"]

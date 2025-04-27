# 1. Use Python base image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements.txt first
COPY requirements.txt .

# 4. Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all your app files
COPY app ./app

# 6. Expose port
EXPOSE 5000

# 7. Start the application
CMD ["python", "app/main.py"]

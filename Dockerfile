# 1. Use Python base image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Install Flask and Werkzeug
RUN pip install flask==2.2.3 werkzeug==2.2.3

# 4. Copy requirements.txt first
COPY requirements.txt .

# 5. Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy all your app files
COPY app ./app

# 7. Expose port
EXPOSE 5000

# 8. Start the application with Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]

# Use full Python base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TRANSFORMERS_CACHE=/app/.hf_cache

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose the Streamlit port
EXPOSE 8501

# Run Streamlit using Python module to avoid PATH issues
CMD ["python", "-m", "streamlit", "run", "app/main.py", "--server.port=8501", "--server.enableCORS=false"]


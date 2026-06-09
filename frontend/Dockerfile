# 1. Using standard Python Base image
FROM python:3.10-slim

# 2. Setting working directory inside the container
WORKDIR /frontend

# 3. Copying requirements.txt and installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copying the entire frontend code into the container
COPY . .

# 5. Exposing Streamlit's default port 8501
EXPOSE 8501

# 6. Running the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
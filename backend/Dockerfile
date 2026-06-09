# 1. Using standard Python Base image 
FROM python:3.10-slim

# 2. Setting working directory inside the container
WORKDIR /backend

# 3. Copying requirements.txt and installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copying the entire backend code into the container
COPY . .

# 5. Exposing port 8000
EXPOSE 8000

# 6. Running the FastAPI application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Python runtime parent image
FROM python:3.9-slim

# Setup workdir at `/app`
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 50051 (default gRPC port)
EXPOSE 50051

# Run the server
CMD ["python3", "run.py"]

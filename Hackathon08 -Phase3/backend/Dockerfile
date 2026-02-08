# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create a non-root user for security (Hugging Face Spaces often run as user 1000)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Expose the port Hugging Face Spaces expects (7860)
EXPOSE 7860

# Command to run the application
# We use uvicorn to run the app
# host 0.0.0.0 is required for container networking
# port 7860 is required by Hugging Face Spaces
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "7860"]

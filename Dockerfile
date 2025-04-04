# Use an offical Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Coy your code and requirments
COPY . .

# Install Dependecies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

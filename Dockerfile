# Use an official Python image as the base
FROM python:3.10-slim

# Install system dependencies required for pyodbc and msodbcsql18.
# These commands update the package cache, install build tools, ODBC headers,
# and then install the Microsoft ODBC Driver 18 for SQL Server.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      gcc \
      curl \
      gnupg2 \
      unixodbc-dev && \
    # Add the Microsoft package signing key and repository
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list \
         > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    # Install the ODBC driver (accepting the EULA automatically)
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    # Clean up to keep the image slim
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy your code and requirements into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]

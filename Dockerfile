FROM python:3.10-slim

WORKDIR /app
COPY . .

# Install dependencies and Microsoft SQL ODBC Driver 18
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        curl \
        gnupg2 \
        apt-transport-https && \
    # Remove conflicting older ODBC libs before new install
    apt-get remove -y libodbc2 unixodbc-common && \
    # Add Microsoft ODBC repo
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev && \
    # Python dependencies
    pip install --no-cache-dir -r requirements.txt && \
    # Clean up to keep image size down
    rm -rf /var/lib/apt/lists/*

EXPOSE 5000
CMD ["python", "app.py"]

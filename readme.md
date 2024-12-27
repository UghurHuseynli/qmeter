# Project Setup Guide

This guide will help you set up and run the project locally using Docker and Python.

## Prerequisites

- Git
- Python 3.x
- Docker and Docker Compose
- pip (Python package installer)

## Installation Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
# or download the ZIP file and extract it
```

### 2. Set Up Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
cd <project-directory>
python -m venv env
```

### 3. Activate Virtual Environment

Depending on your operating system:

**Windows:**
```bash
env\Scripts\activate
```

**Linux/macOS:**
```bash
source env/bin/activate
```

### 4. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

### 5. Database Setup

While `.env` files are typically not included in version control for security reasons, it has been included in this repository for demonstration purposes.

Start the Docker containers and initialize the database:

```bash
docker-compose up -d --build
```

> **Note:** Please allow 1-2 minutes for the database initialization and data seeding process to complete. The duration may vary depending on your system's performance.

### 6. Accessing the Application

Once the setup is complete, you can access the feedback endpoint at:

```
http://localhost/feedback/
```

## Important Notes

- The included `.env` file contains configuration for demonstration purposes only. In a production environment, you should use your own secure environment variables.
- Ensure all Docker containers are running properly before accessing the endpoints.
- If you encounter any issues during database initialization, check the Docker logs for detailed information.


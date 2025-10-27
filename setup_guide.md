# Flask Application Setup Guide

## Prerequisites
- Python 3.8 or higher installed
- pip package manager
- Git (optional, for version control)

## Initial Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal prompt indicating the virtual environment is active.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Copy the example environment file and configure it:
```bash
cp .env.example .env
```

Edit the `.env` file with your actual configuration values:
- Database credentials
- Secret keys
- API keys
- Other environment-specific settings

### 5. Database Migration

Initialize the database migration repository:
```bash
flask db init
```

Create the initial migration:
```bash
flask db migrate -m "Initial migration"
```

Apply the migration to create database tables:
```bash
flask db upgrade
```

## Running the Application

### Development Server
```bash
flask run
```

Or with debug mode:
```bash
flask run --debug
```

Or with live reloading:
```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000/`
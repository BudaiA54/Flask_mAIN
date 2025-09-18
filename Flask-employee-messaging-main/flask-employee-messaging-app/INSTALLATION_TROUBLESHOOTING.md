# Installation Troubleshooting Guide

## Common Installation Issues and Solutions

### 1. Pip Network Timeout Issues

If you encounter network timeout errors when installing packages:

```bash
# Option 1: Use a different PyPI mirror
pip install --index-url https://pypi.python.org/simple/ -r requirements.txt

# Option 2: Increase timeout
pip install --timeout 1000 -r requirements.txt

# Option 3: Install packages individually
pip install Flask==2.3.3
pip install Flask-SQLAlchemy==3.0.5
pip install Flask-Login==0.6.2
pip install Flask-WTF==1.0.0
pip install psycopg2==2.9.3
pip install Werkzeug==2.3.7
```

### 2. Version Compatibility Issues

If you encounter compatibility issues between Flask and Werkzeug:

**Option A: Use compatible versions (recommended)**
```bash
pip install Flask==2.3.3 Werkzeug==2.3.7
```

**Option B: Use latest versions**
```bash
pip install Flask Flask-SQLAlchemy Flask-Login Flask-WTF psycopg2 Werkzeug
```

### 3. PostgreSQL Connection Issues

**Check PostgreSQL Status:**
```bash
# Ubuntu/Debian
sudo systemctl status postgresql

# macOS
brew services list | grep postgresql

# Start PostgreSQL if needed
sudo systemctl start postgresql  # Linux
brew services start postgresql   # macOS
```

**Test Database Connection:**
```bash
psql -h localhost -U messaging_user -d messaging_app
```

### 4. Python Path Issues

If you get import errors, ensure you're in the correct directory:
```bash
cd flask-employee-messaging-app
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### 5. Virtual Environment Setup

Always use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Verify virtual environment
which python
which pip
```

### 6. Database Migration for Existing Installations

If upgrading from a previous version:

1. **Backup existing data:**
```sql
-- Connect to PostgreSQL
\c messaging_app

-- Export existing users (modify as needed)
\copy (SELECT username, role FROM users) TO 'users_backup.csv' CSV HEADER;
```

2. **Add missing columns:**
```sql
-- Add email column (modify constraint as needed)
ALTER TABLE users ADD COLUMN email VARCHAR(120) UNIQUE;

-- Add password_hash column
ALTER TABLE users ADD COLUMN password_hash VARCHAR(128);

-- Update existing users with placeholder data
UPDATE users SET email = username || '@example.com' WHERE email IS NULL;
UPDATE users SET password_hash = '$2b$12$placeholder_hash' WHERE password_hash IS NULL;

-- Add constraints
ALTER TABLE users ALTER COLUMN email SET NOT NULL;
ALTER TABLE users ALTER COLUMN password_hash SET NOT NULL;
```

3. **Users will need to register again** with proper email and password.

### 7. Testing the Installation

Once installed, test basic functionality:

```bash
# Test Python imports
python3 -c "import flask, flask_sqlalchemy, flask_login; print('All modules imported successfully')"

# Test database connection (update connection string)
python3 -c "
import psycopg2
try:
    conn = psycopg2.connect('postgresql://messaging_user:password@localhost:5432/messaging_app')
    print('Database connection successful')
    conn.close()
except Exception as e:
    print(f'Database connection failed: {e}')
"

# Create database tables
python3 create_db.py

# Run the application
python3 run.py
```

### 8. Production Deployment Considerations

For production deployment:

1. **Use environment variables:**
```bash
export SECRET_KEY='your-secret-key-here'
export DATABASE_URL='postgresql://user:password@localhost:5432/dbname'
export FLASK_ENV='production'
```

2. **Use a production WSGI server:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

3. **Set up SSL/HTTPS** for secure password transmission

4. **Configure firewall** to allow only necessary ports

### 9. Development vs Production

**Development:**
- Use `python3 run.py` (Flask development server)
- Debug mode enabled
- Local database

**Production:**
- Use Gunicorn or uWSGI
- Debug mode disabled
- Secure database configuration
- Environment variables for sensitive data
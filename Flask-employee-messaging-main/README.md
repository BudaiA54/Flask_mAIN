# Flask Employee Messaging App

A Flask-based web application for communication between managers and employees using PostgreSQL database with secure user registration and authentication.

## Features

- **User Registration**: Secure email-based registration with password hashing
- **Role-Based Access**: Manager and Employee roles with different permissions
- **Authentication**: Email and password login with session management
- **Manager Dashboard**: Send messages to all employees
- **Employee Dashboard**: View and respond to manager messages

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

## Database Setup

### Installing PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

**MacOS (using Homebrew):**
```bash
brew install postgresql
brew services start postgresql
```

**Windows:**
Download and install from [PostgreSQL official website](https://www.postgresql.org/download/windows/)

### Creating Database and User

1. Connect to PostgreSQL as postgres user:
```bash
sudo -u postgres psql
```

2. Create database and user:
```sql
-- Create database
CREATE DATABASE messaging_app;

-- Create user (replace 'your_password' with a secure password)
CREATE USER messaging_user WITH PASSWORD 'your_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE messaging_app TO messaging_user;

-- Exit PostgreSQL
\q
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/BudaiA54/Flask-employee-messaging.git
cd Flask-employee-messaging/flask-employee-messaging-app
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure database connection:
Edit `config.py` and update the database URI:
```python
SQLALCHEMY_DATABASE_URI = 'postgresql://messaging_user:your_password@localhost:5432/messaging_app'
```

Alternatively, set environment variable:
```bash
export DATABASE_URL='postgresql://messaging_user:your_password@localhost:5432/messaging_app'
```

5. Create database tables:
```bash
python create_db.py
```

## Running the Application

1. Start the Flask development server:
```bash
python run.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

### First Time Setup

1. **Register a Manager Account**:
   - Go to the registration page
   - Fill in email, username, password, and select "Manager" role
   - Click Register

2. **Register Employee Accounts**:
   - Repeat the process but select "Employee" role

### Manager Functions

- Send messages to all employees
- View sent messages
- Access manager dashboard

### Employee Functions

- View messages from managers
- Respond to messages (feature in development)
- Access employee dashboard

## Configuration

### Environment Variables

- `SECRET_KEY`: Flask secret key for session management
- `DATABASE_URL`: PostgreSQL connection string

### Security Features

- **Password Hashing**: Uses Werkzeug for secure password storage
- **Session Management**: Flask-Login for user session handling
- **Role-Based Access**: Restricts access based on user roles
- **Form Validation**: Server-side validation for all user inputs

## Database Migration (For Existing Installations)

If you're upgrading from a previous version without email/password authentication:

1. Backup your existing database:
```bash
pg_dump messaging_app > backup.sql
```

2. The new User model includes additional fields:
   - `email` (required, unique)
   - `password_hash` (required)

3. For existing users, you'll need to:
   - Add email addresses to existing user records
   - Set passwords using the registration form
   - Or manually update the database with proper password hashes

## File Structure

```
flask-employee-messaging-app/
├── app/
│   ├── __init__.py          # Flask app factory and configuration
│   ├── models.py            # Database models (User, Message)
│   ├── routes.py            # Application routes and logic
│   ├── static/              # CSS, JS, images
│   └── templates/           # HTML templates
│       ├── login.html       # Login form
│       ├── register.html    # Registration form
│       ├── manager_dashboard.html
│       └── employee_dashboard.html
├── config.py                # Configuration settings
├── create_db.py            # Database initialization script
├── run.py                  # Application entry point
└── requirements.txt        # Python dependencies
```

## Dependencies

- **Flask 2.3.3**: Web framework
- **Flask-SQLAlchemy 3.0.5**: Database ORM
- **Flask-Login 0.6.2**: User session management
- **Flask-WTF 1.0.0**: Form handling and CSRF protection
- **psycopg2 2.9.3**: PostgreSQL adapter
- **Werkzeug 2.3.7**: WSGI toolkit with password hashing

## Development

### Adding New Features

1. Database changes: Update models in `app/models.py`
2. Routes: Add new routes in `app/routes.py`
3. Templates: Create HTML templates in `app/templates/`
4. Static files: Add CSS/JS in `app/static/`

### Database Schema

**User Table:**
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `password_hash`: Hashed password
- `role`: 'manager' or 'employee'

**Message Table:**
- `id`: Primary key
- `content`: Message text
- `user_id`: Foreign key to User (sender)
- `created_at`: Timestamp

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify PostgreSQL is running
   - Check database credentials in config.py
   - Ensure database and user exist

2. **Import Errors**:
   - Verify virtual environment is activated
   - Install all requirements: `pip install -r requirements.txt`

3. **Permission Errors**:
   - Check database user has proper privileges
   - Verify file permissions for application files

### Logs

Check the console output when running `python run.py` for detailed error messages.

## Security Considerations

- Change default secret key in production
- Use environment variables for sensitive configuration
- Keep dependencies updated
- Use HTTPS in production
- Regular database backups

## License

This project is open source. Please check the repository for license details.

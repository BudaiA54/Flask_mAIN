# Flask Employee Messaging App

This project is a web application built using Flask and PostgreSQL that facilitates communication between managers and employees. Managers can send messages to all employees, and employees can read and respond to these messages.

## Project Structure

```
flask-employee-messaging-app
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── manager_dashboard.html
│   │   └── employee_dashboard.html
│   └── static
│       └── styles.css
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-employee-messaging-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   Update the `config.py` file with your PostgreSQL database connection details.

5. **Run the application:**
   ```
   python run.py
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage Guidelines

- **Login:** Users can log in as either a manager or an employee using the login page.
- **Manager Dashboard:** Managers can send messages to all employees and view responses from employees.
- **Employee Dashboard:** Employees can read messages from managers and respond to them.

## Dependencies

- Flask
- Flask-SQLAlchemy
- psycopg2

## License

This project is licensed under the MIT License.
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # Create test manager
    if not User.query.filter_by(email='manager@test.com').first():
        manager = User(username='manager', email='manager@test.com', role='manager')
        manager.set_password('manager123')
        db.session.add(manager)
        print('Manager account created: manager@test.com / manager123')
    else:
        print('Manager account already exists.')

    # Create test employee
    if not User.query.filter_by(email='employee@test.com').first():
        employee = User(username='employee', email='employee@test.com', role='employee')
        employee.set_password('employee123')
        db.session.add(employee)
        print('Employee account created: employee@test.com / employee123')
    else:
        print('Employee account already exists.')

    db.session.commit()
    print('Test accounts setup complete.')

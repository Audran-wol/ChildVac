# Child Vaccination Management System

The Child Vaccination Management System is a web-based application built using Python and the Django framework. It aims to provide a platform for parents to manage their children's vaccination schedules, book appointments, and receive reminders. Additionally, it allows hospitals to register, view appointments, and update vaccination statuses. The admin can oversee the entire system, manage hospital registrations, view child data, and export appointment data.

## File Structure
child_vaccination_management_system/
├── manage.py
├── requirements.txt
├── README.md
└── vaccination_app/
├── init.py
├── admin.py
├── apps.py
├── forms.py
├── migrations/
│ └── init.py
├── models.py
├── static/
│ ├── css/
│ ├── js/
│ └── images/
├── templates/
│ ├── admin/
│ ├── hospital/
│ ├── parent/
│ └── base.html
├── tests.py
├── urls.py
└── views.py
## Features

- **Parent Module**
  - Register and login
  - Manage child data (add, update, delete)
  - Book appointments for child's vaccination
  - View appointments and their status
  - Receive appointment reminders

- **Hospital Module**
  - Register and request approval from admin
  - Login (after admin approval)
  - View appointments with date filtering
  - Update appointment status

- **Admin Module**
  - Login
  - View and approve/reject hospital registrations
  - View child data
  - View appointment details
  - Export and save appointment data

## Technologies Used

- Python
- Django (Web Framework)
- HTML, CSS, JavaScript (Front-end)
- MySQL (Database)

## Getting Started

1. Clone the repository
2. Install Python and Django
3. Set up a virtual environment and install dependencies
4. Configure the database settings
5. Run database migrations
6. Start the development server

## Contributing

Contributions are welcome! Please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE).

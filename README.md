# Ibn Al-Qayem Laboratory - Messaad
## مخبر إبن القيم - مسعد

A professional medical laboratory website built with Django that allows patients to check their medical test results online.

### Features
- Bilingual support (Arabic/English)
- Patient result lookup system
- QR code generation for results
- Secure admin panel
- Responsive design
- Result management system

### Installation
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

### Default Admin Credentials
- Username: admin
- Password: ali

### Security Note
Please change the default admin credentials after first login for security purposes.

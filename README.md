# IBAN Validator Project

## Description

This project is a Django application for validating IBANs (International Bank Account Numbers). It includes functionality for validating IBANs, saving validation history, and suggesting corrections for invalid IBANs.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- Django CORS Headers

## Installation

Follow these steps to set up the project:

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/iban-validator.git
   cd iban-validator

2. **Create a virtual environment**
    python -m venv venv

3. **Activate the virtual environment**

    - On Windows:
        venv\Scripts\activate
    
    - On macOS/Linux:
        source venv/bin/activate

4. **Install the dependencies**
    pip install -r requirements.txt

5. **Apply database migrations**
    python manage.py migrate

6. **Create a superuser**
    python manage.py createsuperuser

7. **Running the Project**
    To start the development server, use the following command:
        python manage.py runserver
    Visit http://localhost:8000/ in your web browser to view the project.

    Admin Panel
        You can access the Django admin panel at http://localhost:8000/admin/. Log in with the superuser credentials you created.

    In the admin panel, you can manage the IbanHistory model.

8. **API Endpoints**
    Validate IBAN: POST /validate/

    Validates an IBAN without saving it to the database.
    Real-time Validation and Save: POST /real-time-validation/

    Validates and saves an IBAN to the database if valid.
    IBAN History: GET /history/

    Retrieves the history of all validated IBANs, ordered by timestamp.
    Test-Driven Development Validate: POST /test-driven-development-validate/

    Similar to the first validation endpoint.
    Suggest Correct IBAN: POST /suggest-correct-iban/

    Validates an IBAN and suggests a correction if it is invalid.

9. **Testing**
    To run tests, use the following command:
        python manage.py test






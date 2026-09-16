# Healthcare Backend API

A healthcare backend built with Django, Django REST Framework, PostgreSQL, and JWT authentication.

## Features

- User registration and JWT authentication
- Patient management
- Doctor management
- Patient-doctor mapping
- User-specific patient records
- RESTful API endpoints
- PostgreSQL database
- Environment-based configuration
- API validation and authentication

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- psycopg2

## Project Structure

```text
healthcare-backend/
├── accounts/
├── doctors/
├── patients/
├── mappings/
├── healthcare/
├── manage.py
├── .env
└── .gitignore
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd healthcare-backend
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a user |
| POST | `/api/auth/login/` | Obtain JWT access and refresh tokens |
| POST | `/api/auth/refresh/` | Refresh access token |

### Patients

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/patients/` | Create a patient |
| GET | `/api/patients/` | List authenticated user's patients |
| GET | `/api/patients/<id>/` | Get patient details |
| PUT | `/api/patients/<id>/` | Update patient |
| DELETE | `/api/patients/<id>/` | Delete patient |

### Doctors

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/doctors/` | Create a doctor |
| GET | `/api/doctors/` | List doctors |
| GET | `/api/doctors/<id>/` | Get doctor details |
| PUT | `/api/doctors/<id>/` | Update doctor |
| DELETE | `/api/doctors/<id>/` | Delete doctor |

### Patient-Doctor Mappings

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/mappings/` | Assign a doctor to a patient |
| GET | `/api/mappings/` | List mappings |
| GET | `/api/mappings/<patient_id>/` | Get doctors assigned to a patient |
| DELETE | `/api/mappings/<id>/` | Remove a mapping |

## Authentication

Protected endpoints require a JWT access token.

Add the token to the request headers:

```text
Authorization: Bearer <access_token>
```

## Testing

Run the Django test suite with:

```bash
python manage.py test
```

API endpoints can also be tested using Postman or another API client.

## Security

- JWT-based authentication
- Password hashing through Django's authentication system
- Authenticated access to protected resources
- Sensitive configuration stored using environment variables
- PostgreSQL used for persistent data storage

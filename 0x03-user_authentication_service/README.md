# User Authentication Service

This project implements a simple user authentication service using Flask and SQLAlchemy. It includes features for user registration, session management, and password reset.

## Requirements

- Python 3.7
- Flask 1.1.2
- SQLAlchemy 1.3.23
- bcrypt 3.1.7

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/alx-interview.git
    cd alx-interview/0x03-user_authentication_service
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. Initialize the database and create the necessary tables:
    ```bash
    python db_setup.py
    ```

## Running the Application

1. Make sure all your Python files are executable:
    ```bash
    chmod +x *.py
    ```

2. Run the Flask application:
    ```bash
    ./main.py
    ```

   The application will be accessible at `http://0.0.0.0:5000`.

## API Endpoints

### User Registration

- **URL**: `/api/v1/register`
- **Method**: `POST`
- **Form Data**:
  - `email`: User's email address
  - `password`: User's password

- **Response**:
  - `201 Created` on success
  - `400 Bad Request` if the email is missing, password is missing, or the user already exists

### User Login

- **URL**: `/api/v1/session`
- **Method**: `POST`
- **Form Data**:
  - `email`: User's email address
  - `password`: User's password

- **Response**:
  - `200 OK` on success, sets a session cookie
  - `400 Bad Request` if the email or password is missing
  - `401 Unauthorized` if the credentials are invalid

### User Logout

- **URL**: `/api/v1/logout`
- **Method**: `POST`
- **Response**:
  - `200 OK` on success, deletes the session cookie

### Password Reset

- **Generate Reset Token**:
  - **URL**: `/api/v1/reset_password`
  - **Method**: `POST`
  - **Form Data**:
    - `email`: User's email address

  - **Response**:
    - `200 OK` with the reset token
    - `404 Not Found` if the user does not exist

- **Update Password**:
  - **URL**: `/api/v1/update_password`
  - **Method**: `POST`
  - **Form Data**:
    - `reset_token`: The reset token received via email
    - `new_password`: The new password

  - **Response**:
    - `200 OK` on success
    - `400 Bad Request` if the reset token is invalid

## Project Structure


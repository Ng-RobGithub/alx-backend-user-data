# Basic Authentication Project

This project implements a simple API with Basic Authentication using Python and Flask. It is intended to help you understand the basics of authentication, Base64 encoding, and how to secure API endpoints.

## Requirements

- Python 3.7
- Flask

## Setup

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:

    ```bash
    python3 app.py
    ```

3. Access the application in your browser at `http://127.0.0.1:5000/`.

## Usage

To access the protected endpoint, use Basic Authentication with the following credentials:

- Username: `user`
- Password: `password`

### Example with `curl`:

```bash
curl -u user:password http://127.0.0.1:5000/protected

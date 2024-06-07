# Session Authentication Project

## Introduction

This project implements a Session Authentication mechanism from scratch using Flask. It aims to provide a deeper understanding of how session-based authentication works, including handling cookies, parsing them, and managing user sessions.

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Endpoints](#endpoints)
7. [License](#license)

## Requirements

- Python 3.7
- Flask
- pycodestyle 2.5

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/alx-backend-user-data.git
    ```
2. Navigate to the project directory:
    ```bash
    cd alx-backend-user-data/0x02-session_authentication
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python3 -m api.v1.app
    ```
2. Access the API at `http://0.0.0.0:5000/api/v1/`.

## Project Structure

```plaintext
alx-backend-user-data/
└── 0x02-session_authentication/
    ├── api/
    │   ├── __init__.py
    │   └── v1/
    │       ├── __init__.py
    │       ├── app.py
    │       ├── views/
    │       │   ├── __init__.py
    │       │   └── session_auth.py
    │       └── auth/
    │           ├── __init__.py
    │           └── session_auth.py
    ├── models/
    │   ├── __init__.py
    │   └── user.py
    ├── README.md
    ├── requirements.txt
    └── setup.py

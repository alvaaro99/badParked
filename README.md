# BadParked

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**BadParked** is a backend application under development that allows users to manage improperly parked vehicles and notify the owner if the vehicle is causing an inconvenience. Users can register multiple vehicles, activate the visibility of their contact information when the vehicle is improperly parked, and generate a QR code to facilitate communication with those who need to contact them.

## Table of Contents

-   [Project Status](#project-status)
-   [Technologies Used](#technologies-used)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Authentication and Security](#authentication-and-security)
-   [QR Code Generation](#qr-code-generation)
-   [Documentation](#documentation)
-   [License](#license)

## Project Status

BadParked is currently under development and is a proof-of-concept application without a frontend. The project includes a functional backend and an OpenAPI documentation endpoint to view the available endpoints.

## Technologies Used

-   **Language**: Python
-   **Frameworks**: FastAPI, SQLModel
-   **Database**: PostgreSQL (Docker)
-   **Database Version Control**: Alembic
-   **Authentication**: JWT
-   **Security**: Passwords stored as hashes
-   **QR Code Generation**: `qrcode` library

## Installation

To install and run BadParked on your local environment, follow these steps:

```bash
# Clone the repository
git clone https://github.com/your-username/BadParked.git

# Navigate to the project directory
cd BadParked

# Create a virtual environment (optional but recommended)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Set up and run Docker for PostgreSQL
docker-compose up -d

# Perform database migrations with Alembic
alembic upgrade head

# Run the application
fastapi dev src/main.py
```

## Usage

BadParked provides a series of endpoints to manage users and vehicles. You can access the full API documentation via the /docs URL when the server is running.

## Authentication and Security

### Authentication

Users authenticate using JWT. Tokens are generated upon login and are required to access most of the endpoints.

### Passwords

Passwords are stored as hashes in the database to ensure security.

### QR Code Generation

The application allows users to generate QR codes using the qrcode library. These codes contain a URL that directs to a page with the vehicle owner's contact information. The QR codes are generated and saved as PNG files within the project.

## Documentation

You can access the API documentation through the following endpoints when the application is running:

/docs - Interactive documentation with Swagger UI

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

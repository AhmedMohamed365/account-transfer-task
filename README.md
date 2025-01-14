# Account Transfer Web App

This project is a simple web application built using Django that allows users to manage fund transfers between accounts. The application supports importing accounts from CSV files, querying account information, and transferring funds between accounts.

## Functional Requirements

- **Import Accounts**: Users can import a list of accounts with opening balances from CSV files.
- **List Accounts**: Users can view a list of all accounts.
- **Get Account Information**: Users can retrieve detailed information about a specific account.
- **Transfer Funds**: Users can transfer funds between any two accounts.

## Project Structure

The project is organized as follows:

```
account-transfer-app
├── accounts
│   ├── migrations          # Database migration files
│   ├── templates           # HTML templates for the web interface
│   │   └── accounts
│   │       ├── account_list.html   # Template for listing accounts
│   │       ├── account_detail.html  # Template for account details
│   │       └── transfer.html        # Template for fund transfer form
│   ├── __init__.py
│   ├── admin.py            # Admin site configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Data models for accounts
│   ├── tests.py            # Unit tests for the accounts app
│   ├── urls.py             # URL routing for the accounts app
│   └── views.py            # View functions for handling requests
├── account_transfer
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL routing for the project
│   └── wsgi.py             # WSGI entry point
├── manage.py                # Command-line utility for the project
├── requirements.txt         # Project dependencies
├── Dockerfile (optional)    # Dockerfile for containerization
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd account-transfer-app
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   ```
   python manage.py migrate
   ```

4. **Run the Development Server**:
   ```
   python manage.py runserver
   ```

5. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Unit Tests

The project includes unit tests located in `accounts/tests.py` to ensure functionality and maintain coverage.

## Optional Features

- A Dockerfile is provided for building a Docker image of the web app.

## License

This project is licensed under the MIT License.
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
account-transfer-project
├── accounts
│   ├── migrations          # Database migration files
│   ├── templates           # HTML templates for the web interface
│   │   └── accounts
│   │       ├── account_list.html   # Template for listing accounts
│   │       ├── account_detail.html  # Template for account details
│   │       └── transfer.html        # Template for fund transfer form
│   │       └── base.html        # Base template for navbar and bootstrap styles
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
   cd account-transfer-project
   ```

2. **Install Dependencies**:
Used virtual env, but you can use pipenv for better depenency management or conda environment.
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

To run the tests : 
```bash
python manage.py test
```

## Optional Features
- Application is accepting any text format like .xlsx , .txt , .csv
- A Dockerfile is provided for building a Docker image of the web app.

## To run using docker

Simply run these commands in "src" directory to be able to use it and reflect anychange to the project directory inside the container.
```bash
docker build -t account-transfer-container .
 ```
This command works on windows
```
docker run --name account-transfer-app -p 8000:8000 -v %cd%:/app -it account-transfer-container
```

## License

This project is licensed under the MIT License.
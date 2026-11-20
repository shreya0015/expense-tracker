# Personal Expense Tracker

A web-based Personal Expense Tracker built using **Python, Flask, MySQL, HTML, CSS, and Bootstrap 5**.

The project aims to help users manage their daily expenses, organize spending into categories, and understand their financial habits through reports and visualizations.

## Technologies Used

- **Backend:** Python, Flask
- **Database:** MySQL
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database Connection:** PyMySQL
- **Configuration:** python-dotenv
- **Security:** Flask-WTF (CSRF protection)

## Features

### Currently Implemented
- Flask application setup
- MySQL database configuration
- Database tables for users, categories, and expenses
- Login page interface
- Registration page interface
- CSRF protection setup
- Environment variable configuration

### Planned Features
- User registration with secure password hashing
- User login and logout using sessions
- Add, edit, and delete expenses
- Custom expense categories
- Dashboard showing total spending
- Monthly expense summaries
- Expense charts using Chart.js
- Expense filtering and searching
- CSV report export
- User profile management

## Project Structure

```text
expense_tracker/
├── app.py
├── config.py
├── database.sql
├── requirements.txt
├── test_db.py
├── .env
├── .vscode/
│   └── launch.json
├── templates/
│   ├── login.html
│   └── register.html
└── README.md
```

Additional files and directories will be added as development progresses.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd expense_tracker
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create a MySQL database named `expense_tracker`.

Import the database schema:

```bash
mysql -u <mysql-user> -p expense_tracker < database.sql
```

Ensure the MySQL user has the required permissions.

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_generated_secret_key
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=expense_tracker
```

Generate a secure secret key using:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Important:** Never commit `.env` or database credentials to GitHub.

### 6. Test the Database Connection

```bash
python test_db.py
```

Expected output:

```text
SUCCESS: Connected to MySQL!
Database tables:
- categories
- expenses
- users
```

### 7. Run the Application

```bash
python app.py
```

Open the application at:

http://127.0.0.1:5001/login

The development server currently uses port **5001** to avoid a port conflict on macOS.

## Database Design

The project uses three main tables:

| Table | Description |
|---|---|
| `users` | Stores user account information |
| `categories` | Stores expense categories belonging to users |
| `expenses` | Stores individual expense records |

Foreign keys maintain relationships between users, categories, and expenses.

## Development Status

**In Progress**

The initial project setup, database connection, and authentication page interfaces are complete.

The next development milestone is implementing user registration and login functionality with secure database integration.

## Future Improvements

- Responsive expense dashboard
- Spending analytics and charts
- Monthly and category-based reports
- Improved form validation
- Additional automated tests

## License

This project is currently intended for educational and portfolio purposes.

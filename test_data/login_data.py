# testdata/login_testdata.py

wrong_email_data = [
    {
        "email": "wrong@demo.com",
        "password": "demo",
        "error": "Invalid email or password!"  # updated to match app
    },
]

wrong_password_data = [
    {
        "email": "demo@demo.com",
        "password": "wrong_password",
        "error": "Invalid email or password!"  # updated to match app
    },
]

invalid_email_format_data = [
    {
        "email": "invalidemail",
        "password": "demo",
        "error": "Please enter a valid email address."
    }
]

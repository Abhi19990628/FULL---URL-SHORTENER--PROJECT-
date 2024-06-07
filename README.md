# URL Shortener

This is a simple URL shortener web application built with Django.

## Features

- Allows registered users to shorten URLs.
- Redirects users to the original URL when they visit the shortened URL.
- Provides a form for registered users to retrieve the original URL using the shortened URL.
- Implements user authentication and authorization for security.
- Generates a unique shortened URL for each original URL.
- Uses Django's built-in forms for user authentication and URL input.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/url-shortener.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application at `http://127.0.0.1:8000/`.

## Usage

1. **Register/Login:**
   - Access the registration page at `http://127.0.0.1:8000/register/` to create a new account.
   - After registering, log in using the credentials.
   
2. **Shorten URL:**
   - Once logged in, access the URL shortening form at `http://127.0.0.1:8000/shorten/`.
   - Enter the original URL you want to shorten and submit the form.
   - You will receive a shortened URL which you can use to redirect to the original URL.

3. **Retrieve Original URL:**
   - If you want to retrieve the original URL associated with a shortened URL, visit `http://127.0.0.1:8000/retrieve/`.
   - Enter the shortened URL in the provided form and submit.
   - You will be presented with the original URL if it exists in the database.

4. **Logout:**
   - To logout from the application, visit `http://127.0.0.1:8000/logout/` and click on the logout button.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/awesome-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/awesome-feature`).
6. Create a new Pull Request.

## Acknowledgments

- This project is inspired by [youtube long links].
- Special thanks to [YATENDRA SINGH] for their valuable contributions.

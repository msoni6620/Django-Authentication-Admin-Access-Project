# Django Authentication & Admin Access Project

## Overview

The **Django Authentication & Admin Access Project** is a secure web application built using the Django framework that focuses on implementing user authentication, authorization, and role-based access control. It features a custom user model with role assignments (Admin and User), allowing users to access specific sections of the application based on their assigned role. The project includes a Django-admin interface for easy management of users and roles and provides a robust system for managing authentication via JSON Web Tokens (JWT) for API security.

This project leverages Django’s built-in authentication system while extending it to provide more flexible and secure access control through roles. It aims to demonstrate how to implement a custom user model, secure RESTful API endpoints, and role-based permissions in a Django application.

## Key Features

- **Custom User Model**: Extends Django's AbstractUser to add a role field, allowing the creation of distinct user roles (Admin and User).
  
- **Role-Based Access Control**: Grants different permissions based on user roles (Admin can manage users, while regular Users can only access specific views).
  
- **JWT Authentication**: Implements JSON Web Token (JWT) authentication for secure and stateless API access, ensuring that sensitive data is protected.

- **Admin Interface**: Customize the Django Admin panel to manage users, roles, and access control directly from the dashboard.

- **Secure API Endpoints**: All API routes are protected using JWT tokens to ensure secure access. Only authorized users can access restricted endpoints.

## Technologies Used

- **Django**: A high-level Python web framework that simplifies the process of building secure and scalable web applications.
  
- **Django REST Framework (DRF)**: A toolkit for building Web APIs in Django, enabling the creation of RESTful endpoints for user authentication and interaction.
  
- **JWT (JSON Web Tokens)**: A compact, URL-safe means of representing claims to be transferred between two parties, used for secure API authentication.

- **SQLite/PostgreSQL/MySQL**: Relational databases used for storing user data and role-based permissions.

## Installation

To get started with this project, follow the steps below to set up the environment and dependencies:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/django-authentication-admin-access.git
    cd django-authentication-admin-access
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Mac/Linux
    venv\Scripts\activate  # For Windows
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser to access the Django Admin**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server**:

    ```bash
    python manage.py runserver
    ```

7. Now you can access the application at `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel**: To access the Django admin panel, navigate to `http://127.0.0.1:8000/admin/`. Log in using the superuser credentials you created during setup.

- **JWT Authentication**: The authentication for API endpoints uses JWT tokens. You can obtain a JWT token by logging in at the login endpoint (e.g., `http://127.0.0.1:8000/token/`). Once you have the token, include it in the Authorization header of your requests as a bearer token to access protected resources.

- **Role-Based Access**: Users are assigned roles (Admin/User), and their access is controlled based on these roles. Admins can manage other users via the Django admin panel, while regular users have limited access.

## API Endpoints

- **Login**: `POST /token/`
  - Request body: `{"username": "your-username", "password": "your-password"}`
  - Response: Returns a JWT token that can be used for authentication.

- **Refresh Token**: `POST /token/refresh/`
  - Request body: `{"refresh": "your-refresh-token"}`
  - Response: Returns a new access token.

- **User Profile**: `GET /profile/`
  - Requires authentication (JWT Token).
  - Response: Returns user profile details.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

Steps to contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b your-branch-name`.
3. Make your changes.
4. Commit your changes: `git commit -am 'Add new feature'`.
5. Push to your branch: `git push origin your-branch-name`.
6. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, you can reach me at:

- **Email**: msoni6620@gmail.com
- **LinkedIn**: [linkedin.com/in/mayanksoni-](https://www.linkedin.com/in/mayanksoni-/)

## Demo

You can view the live demo or visit the deployed version of the project at GitHub Pages.

## Summary

The **Django Authentication & Admin Access Project** provides a comprehensive solution for implementing secure user authentication and role-based access in Django applications. It integrates custom user models, JWT authentication, and flexible permissions to control access to resources based on user roles. Whether you're building a simple web app or a complex application, this project serves as a robust foundation for secure user management and API access control.

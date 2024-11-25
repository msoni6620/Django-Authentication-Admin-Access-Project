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



## Contact

For any questions or feedback, you can reach me at:

- **Email**: msoni6620@gmail.com
- **LinkedIn**: [linkedin.com/in/mayanksoni-](https://www.linkedin.com/in/mayanksoni-/)

## Demo

You can view the working of my video- **working.mp4.

## Summary

The **Django Authentication & Admin Access Project** provides a comprehensive solution for implementing secure user authentication and role-based access in Django applications. It integrates custom user models, JWT authentication, and flexible permissions to control access to resources based on user roles. Whether you're building a simple web app or a complex application, this project serves as a robust foundation for secure user management and API access control.

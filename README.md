# Task Management App with Google Login

A simple task management web application built with Django. Users can log in using their Google accounts to manage tasks (create, view, edit, delete). The app also includes an admin panel to manage Google OAuth credentials and user invites.

## Features

- **Google Authentication**: Users can log in using their Google account.
- **Task Management**: Users can create, view, edit, and delete tasks.
- **Admin Panel**:
  - Admin can store and manage Google OAuth credentials.
  - Admin can invite new users via email with a registration link.
  
## Technologies Used

- **Backend**: Django (Python)
- **Authentication**: Google OAuth (using `django-allauth`)
- **Database**: SQLite (for development) or PostgreSQL (for production)
- **Frontend**: HTML, CSS (Bootstrap for responsive design)
- **Email**: Django Email (for sending invitation emails)

## Prerequisites

- Python 3.x
- Django 4.x or above
- Google Cloud Console account (for OAuth credentials)
- SQLite or PostgreSQL (for database)



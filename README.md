# CineBooker - Movie Ticket Booking System

A smart, cloud-based movie ticket booking system built with Flask, designed to provide a seamless and modern movie-watching experience.

## Description

CineBooker is a Flask-based web application that allows users to register, log in, and book movie tickets online with ease. Users can search for movies and events based on location, view real-time seat availability, and complete their bookings in just a few clicks. The system is designed to be deployed on AWS EC2 with DynamoDB integration and AWS SNS for email notifications.

## Features

- ✅ User Registration and Authentication
- ✅ Secure Password Hashing
- ✅ Movie Listing with Details
- ✅ Location-based Theater Information
- ✅ Real-time Seat Selection
- ✅ Interactive Booking Interface
- ✅ Booking Confirmation System
- ✅ Session Management
- ✅ Flash Messages for User Feedback

## Technology Stack

- **Backend**: Flask (Python)
- **Security**: Werkzeug (Password Hashing)
- **Frontend**: HTML, CSS, JavaScript
- **Storage**: In-memory

## Project Structure

```
CineBooker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── home1.html
│   ├── about.html
│   ├── contact_us.html
│   ├── b1.html
│   └── tickets.html
└── static/               # Static files
    └── style.css
```

## Installation & Setup

### Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd CineBooker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your browser and navigate to: `http://localhost:5000`

## Usage

### For Users

1. **Sign Up**: Create a new account by clicking "Sign Up" on the homepage
2. **Login**: Use your credentials to log in
3. **Browse Movies**: View available movies on the home page
4. **Select Showtime**: Click on a showtime for your preferred movie
5. **Choose Seats**: Select your preferred seats from the interactive seat map
6. **Confirm Booking**: Review your booking summary and confirm
7. **Receive Confirmation**: View your booking confirmation with all details

### Routes

- `/` - Homepage
- `/login` - User login page
- `/signup` - User registration page
- `/logout` - User logout
- `/home1` - Movies listing page (requires login)
- `/about` - About page
- `/contact_us` - Contact page
- `/b1` - Booking page (requires login)
- `/tickets` - Booking confirmation (POST)


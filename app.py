from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'cinebooker-secret-key'

# Temporary in-memory storage
users = []
bookings = []
booking_counter = 0

# Sample movies data
movies = [
    {
        'id': 1,
        'name': 'Avengers: Endgame',
        'genre': 'Action',
        'rating': '4.8',
        'theater': 'PVR Cinemas',
        'address': '123 Main Street, Downtown',
        'price': 350,
        'showtimes': ['10:00 AM', '1:30 PM', '5:00 PM', '8:30 PM']
    },
    {
        'id': 2,
        'name': 'The Dark Knight',
        'genre': 'Action',
        'rating': '4.9',
        'theater': 'INOX Multiplex',
        'address': '456 Park Avenue, Midtown',
        'price': 300,
        'showtimes': ['11:00 AM', '2:30 PM', '6:00 PM', '9:30 PM']
    },
    {
        'id': 3,
        'name': 'Inception',
        'genre': 'Sci-Fi',
        'rating': '4.7',
        'theater': 'Cinepolis',
        'address': '789 Broadway, Uptown',
        'price': 320,
        'showtimes': ['10:30 AM', '2:00 PM', '5:30 PM', '9:00 PM']
    },
    {
        'id': 4,
        'name': 'Interstellar',
        'genre': 'Sci-Fi',
        'rating': '4.8',
        'theater': 'PVR Cinemas',
        'address': '123 Main Street, Downtown',
        'price': 340,
        'showtimes': ['12:00 PM', '3:30 PM', '7:00 PM', '10:30 PM']
    }
]

# Authentication Routes

@app.route('/')
def index():
    """Homepage"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Find user by email
        user = next((u for u in users if u['email'] == email), None)
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_email'] = user['email']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home1'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Signup page"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not name or not email or not password:
            flash('All fields are required', 'error')
            return render_template('signup.html')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('signup.html')
        
        # Check if email already exists
        if any(u['email'] == email for u in users):
            flash('Email already registered', 'error')
            return render_template('signup.html')
        
        # Create new user
        user_id = len(users) + 1
        new_user = {
            'id': user_id,
            'name': name,
            'email': email,
            'password': generate_password_hash(password)
        }
        users.append(new_user)
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    """Logout"""
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))

# Main Application Pages

@app.route('/home1')
def home1():
    """Home page after login"""
    if 'user_id' not in session:
        flash('Please login to access this page', 'error')
        return redirect(url_for('login'))
    
    return render_template('home1.html', movies=movies, user_name=session.get('user_name'))

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/contact_us')
def contact_us():
    """Contact Us page"""
    return render_template('contact_us.html')

@app.route('/b1')
def b1():
    """Booking page"""
    if 'user_id' not in session:
        flash('Please login to book tickets', 'error')
        return redirect(url_for('login'))
    
    # Get movie details from query parameters
    movie_id = request.args.get('movie_id', type=int)
    showtime = request.args.get('showtime', '')
    
    if movie_id:
        movie = next((m for m in movies if m['id'] == movie_id), None)
        if movie:
            return render_template('b1.html', movie=movie, showtime=showtime)
    
    flash('Movie not found', 'error')
    return redirect(url_for('home1'))

@app.route('/tickets', methods=['POST'])
def tickets():
    """Ticket booking submission"""
    if 'user_id' not in session:
        flash('Please login to book tickets', 'error')
        return redirect(url_for('login'))
    
    # Get form data
    movie_name = request.form.get('movie_name')
    theater = request.form.get('theater')
    address = request.form.get('address')
    showtime = request.form.get('showtime')
    seats = request.form.getlist('seats')
    price_per_ticket = float(request.form.get('price', 0))
    
    if not seats:
        flash('Please select at least one seat', 'error')
        return redirect(url_for('home1'))
    
    # Calculate total price
    total_price = price_per_ticket * len(seats)
    
    # Create booking
    global booking_counter
    booking_counter += 1
    
    booking = {
        'id': booking_counter,
        'user_id': session['user_id'],
        'user_name': session['user_name'],
        'user_email': session['user_email'],
        'movie_name': movie_name,
        'theater': theater,
        'address': address,
        'showtime': showtime,
        'seats': seats,
        'price_per_ticket': price_per_ticket,
        'total_price': total_price,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    bookings.append(booking)
    
    return render_template('tickets.html', booking=booking)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

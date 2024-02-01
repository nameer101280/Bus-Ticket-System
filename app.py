from flask import Flask, render_template, request, jsonify, redirect, url_for
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__, static_url_path='/static', template_folder='templates')

# AWS Cognito configuration
USER_POOL_ID = 'eu-north-1_PqLuLDbkW'
CLIENT_ID = 'PqLuLDbkW'
REGION_NAME = 'eu-north-1'

# Initialize AWS clients and resources
client = boto3.client('cognito-idp', region_name=REGION_NAME)
dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
table_name = 'bus_tickets'
table = dynamodb.Table(table_name)

# Helper function to verify JWT token
def verify_token(token):
    try:
        response = client.admin_get_user(
            UserPoolId=USER_POOL_ID,
            Username=token  # Assuming the username is the same as the access token
        )
        return response['Username']
    except ClientError as e:
        return None

# Root route to provide a welcome message
@app.route('/')
def index():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        # Check user credentials and log in the user
        # Add your authentication logic here
        return redirect(url_for('user_dashboard'))  # Redirect to the user dashboard page after successful login
    else:
        # Render the login form
        return render_template('login.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration form submission
        # Create a new user account
        # Add your registration logic here
        return redirect(url_for('login'))  # Redirect to the login page after successful registration
    else:
        # Render the registration form
        return render_template('register.html')

# User dashboard route
@app.route('/dashboard', methods=['GET', 'POST'])
def user_dashboard():
    # Render the user dashboard template
    return render_template('user_dashboard.html')

# Route for booking a ticket
@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    # Get the token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Token is missing'}), 401
    
    # Verify the token
    username = verify_token(token)
    if not username:
        return jsonify({'error': 'Invalid token'}), 401
    
    # Extract bus_id and seat_number from the request body
    data = request.get_json()
    bus_id = data.get('bus_id')
    seat_number = data.get('seat_number')
    
    # Validate bus_id and seat_number (you can add more validation as needed)
    if not bus_id or not seat_number:
        return jsonify({'error': 'Bus ID and seat number are required'}), 400
    
    # Book the ticket in DynamoDB
    try:
        table.put_item(
            Item={
                'username': username,
                'bus_id': bus_id,
                'seat_number': seat_number
            }
        )
        return jsonify({'message': 'Ticket booked successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

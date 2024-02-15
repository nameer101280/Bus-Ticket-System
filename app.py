from flask import Flask, request, session, render_template, url_for, redirect
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__, static_url_path='/static', template_folder="templates")

app.secret_key = "your_secret_key"  # Change this to a secure secret key

# AWS Cognito configuration
USER_POOL_ID = 'us-east-1_pDrDU0PvZ'
CLIENT_ID = '2MBhhu4Dm'
REGION_NAME = 'us-east-1'

client = boto3.client('cognito-idp', region_name=REGION_NAME)

@app.route('/', methods=['GET'])  # Add route for the home page
def home():
    return render_template('index.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            response = client.initiate_auth(
                ClientId=CLIENT_ID,
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': email,
                    'PASSWORD': password
                }
            )
            session['access_token'] = response['AuthenticationResult']['AccessToken']
            return redirect(url_for('user_dashboard'))  # Changed redirect URL
        except ClientError as e:
            error_message = e.response['Error']['Message']
            return render_template('login.html', error=error_message)
    return render_template('login.html')

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            client.sign_up(
                ClientId=CLIENT_ID,
                Username=email,
                Password=password,
                UserAttributes=[
                    {'Name': 'email', 'Value': email}
                ]
            )
            return redirect(url_for('login'))  # Changed redirect URL
        except ClientError as e:
            error_message = e.response['Error']['Message']
            return render_template('register.html', error=error_message)
    return render_template('register.html')

@app.route('/book_ticket.html')
def book_tickets():
    return render_template('book_ticket.html')

@app.route('/user_dashboard.html')  # Changed route URL
def user_dashboard():
    if 'access_token' not in session:
        return redirect(url_for('login'))
    return render_template('user_dashboard.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

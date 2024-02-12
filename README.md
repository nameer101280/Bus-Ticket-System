# Bus Ticketing System

This is a simple bus ticketing system built with Python Flask and AWS services.

## Prerequisites

- Python 3.x
- AWS account with Cognito and DynamoDB setup
- Python packages mentioned in requirements.txt

## Configuration

1. Replace the placeholders in `config.py` with your actual AWS Cognito user pool ID, client ID, and region name.
2. Make sure you have set up the necessary AWS IAM permissions for your application to access Cognito and DynamoDB.

## Usage

1. Install the required Python packages using `pip install -r requirements.txt`.
2. Run the Flask application using `python app.py`.
3. Access the application through the provided URL (usually http://127.0.0.1:5000).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

from flask import Blueprint , jsonify ,request
import jwt, logging
# Create a Blueprint
# Configure logging
logging.basicConfig(filename='login_attempts.log', level=logging.INFO)
auth_router = Blueprint('auth', __name__)

# Define routes within this Blueprint
@auth_router.route('/google_auth', methods=['POST'])
def google_auth():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']

        # Check email and password (Replace with your authentication logic)
        if email == 'correct_email' and password == 'correct_password':
            # Create a session and JWT token
            session_data = {'email': email}
            jwt_token = jwt.encode(session_data, 'your_secret_key', algorithm='HS256')
            return jsonify({'message': 'Login successful', 'token': jwt_token}), 200
        else:
            # Log incorrect login attempts
            logging.warning(f'Incorrect login attempt for email: {email}')
            return jsonify({'error': 'Incorrect email or password'}), 401
    except Exception as e:
        # Log exceptions
        logging.error(f'Exception during login: {str(e)}')
        return jsonify({'error': 'An error occurred during login'}), 500

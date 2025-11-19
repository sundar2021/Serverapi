import os
from flask import Flask, jsonify
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
 
# Load environment variables from .env file
load_dotenv()
 
app = Flask(__name__)
 
# Configuration from environment variables
TENANT_ID = os.getenv('TENANT_ID')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SUBDOMAIN = os.getenv('SUBDOMAIN')
RESOURCE = "https://cognitiveservices.azure.com/"
 
if not all([TENANT_ID, CLIENT_ID, CLIENT_SECRET, SUBDOMAIN]):
    raise ValueError("Missing environment variables. Check your .env file.")
 
@app.route('/getimmersivereaderlaunchparams', methods=['GET'])
def get_launch_params():
    try:
        # Acquire a token using the DefaultAzureCredential
        # This will use environment variables (ClientSecretCredential in this case)
        credential = DefaultAzureCredential()
        # The scope is the resource URL plus "/.default"
        scope = f"{RESOURCE}/.default"
        token_credential = credential.get_token(scope)
        token = token_credential.token
 
        return jsonify({
            'token': token,
            'subdomain': SUBDOMAIN
        })
    except Exception as e:
        app.logger.error(f"Error acquiring token: {e}")
        return jsonify({'error': 'Unable to acquire Microsoft Entra token.'}), 500
 
if __name__ == '__main__':
    # Ensure this endpoint is secured in a production environment
    app.run(debug=True)

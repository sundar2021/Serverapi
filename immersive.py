import os
from flask import Flask, jsonify
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
 
# Load environment variables from .env file
load_dotenv()
 
app = Flask(__name__)
 
# Configuration from environment variables
TENANT_ID = "cb561bac-8eae-4e86-979a-765c514af3ae"
CLIENT_ID = "https://immersivereader100.cognitiveservices.azure.com/"
CLIENT_SECRET = "DWMjNMH2pDwwfzJAE9QtV7UnTC2mMV6bfo2javqyyuh0Kj5Kv4A5JQQJ99BKACYeBjFXJ3w3AAAOACOGnDiu"
SUBDOMAIN = "immersivereader100"
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

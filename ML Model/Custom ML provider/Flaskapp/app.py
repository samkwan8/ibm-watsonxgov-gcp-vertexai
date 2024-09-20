from flask import Flask, request, abort, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

import subprocess
#subprocess.check_output('pip install google-cloud-aiplatform', shell=True)
from google.oauth2 import service_account
import google.auth.transport.requests as google_requests
import json
import base64
import requests, io
import pandas as pd
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

with open("credentials.json") as creds:
    CREDENTIALS = json.load(creds)

gcp_json_credentials_dict = CREDENTIALS['GCP_TOKEN']

users = {
    CREDENTIALS['username']: generate_password_hash(CREDENTIALS['password'])
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def index():
    return jsonify("Hello, {}!".format(auth.current_user()))

@app.route('/predictions', methods=['POST'])
@auth.login_required
def score_model():
    if not request.json:
        abort(400)
        
    dataset = request.json
    dataset['columns'] = dataset.pop('fields')
    dataset['data'] = dataset.pop('values')
    scoring_payload = json.dumps(dataset, allow_nan=True)

    ## ! Replace you deployed prediction endpoint below
    predictions_url = 'https://us-central1-aiplatform.googleapis.com/v1/projects/900139867450/locations/us-central1/endpoints/5087464490975363072:predict'
    
    # Get the GCP OAuth token
    credentials = service_account.Credentials.from_service_account_info(gcp_json_credentials_dict, scopes=['https://www.googleapis.com/auth/cloud-platform'])
    google_request = google_requests.Request()
    credentials.refresh(google_request)
    token = credentials.token
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    scoring_payload_dict = json.loads(scoring_payload)
    input_values = scoring_payload_dict['data']

    # Construct the scoring payload for GCP Vertex AI
    gcp_scoring_payload = {"instances": input_values}
    
    # Get the response
    response = requests.post(predictions_url, headers=headers, json=gcp_scoring_payload, verify=False)
    response_json = response.json()

    # Construct the response to what WML Python Function should send back.
    response_payload = response_json["predictions"][0]
    return jsonify(response_payload)

if __name__ == '__main__':
    app.run (host='0.0.0.0', port='8080') #(port=5000, debug=True)

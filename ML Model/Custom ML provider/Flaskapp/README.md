# Insctruction for deploying Flask App connected with VertexAI model endpoint as custom ML provider

This instruction deploys the app on Google Compute Engine (VM instance). You may also deploy it on Google App Engine or another technology stack of your preference.

## Step 1: Edit and Insert Your GCP Access Token

Edit and insert you GCP access token in [credentals.json](https://github.ibm.com/samkwan/wxgov-gcp-vertexai/blob/main/ML%20Model/Custom%20ML%20provider/Flaskapp/credentials.json). Update the file with the following values:

### Credential file values:
```
{
    "GCP_TOKEN": <Your GCP_TOKEN API key>,
    "username": <username for basic authentication on flask app, default "admin">,
    "password": <password for basic authentication on flask app, default "password">
}
```

## Step 2: Edit and Insert Deployed Endpoint ID and Project ID

In the deployed endpoint, click "Sample Request" to retrieve the necessary information.

<img width="664" alt="image" src="https://media.github.ibm.com/user/461759/files/d22cc9c2-200a-4ebf-9e8c-2ca45d17f042">

Replace the ```prediction_url``` in [app.py]()

![image](https://media.github.ibm.com/user/461759/files/2869b597-fd82-4735-93b4-8bbefb839160)

## Step 3: Create an Instance in Google Compute Engine
Provide a name for the instance and choose E2 for the machine type. Use default settings and click ```Create``` at the bottom.

<img width="1157" alt="image" src="https://media.github.ibm.com/user/461759/files/3d21c5bf-69a9-4dcd-8cda-4ff7cbafcb42">

<img width="1113" alt="image" src="https://media.github.ibm.com/user/461759/files/9656e240-bfe0-4553-8285-67b535fd68bb">

## Step 4: Deploy the Flask App on the VM instance.

1. SSH into the instance by clicking the connect `SSH` in right-hand side.

<img width="1158" alt="image" src="https://media.github.ibm.com/user/461759/files/7dc0ecc8-c4d8-42a4-95ab-8865eaa596e0">

<img width="944" alt="image" src="https://media.github.ibm.com/user/461759/files/ac7b1494-4fb5-4f8d-b493-fd558ac74515">

2. Once logged into the Linux instance, execute the following commands:

```shell
sudo apt-get update
alias python=python3
sudo apt install pip
sudo apt install python3.11-venv
mkdir flask-app
cd flask-app!
```

Use VI editor to create the ```app.py```, ```requirements.txt``` and ```credentials.json```. Alternatively, use any preferred method to upload the files.

```shell
vi app.py
```
Copy and paste the app.py code, save and quit vi.

```shell
vi requirements.txt
```
Copy and paste the requirements.txt code, save and quit vi.

```shell
vi credentials.json
```
Copy and paste the credentials.json code, save and quit vi.

Execute the following commands:
```shell
python -m venv .venv
source .venv/bin/activate
screen -S flask
pip install -r requirements.txt
python app.py
```

This starts the Flask app in a screen session to prevent disconnecting when the terminal is closed.

<img width="664" alt="image" src="https://media.github.ibm.com/user/461759/files/d47b52df-d9e0-4147-a401-a4160118fd81">

## Step 5: Add Firewall Rule in GCP VPC Networks

1. Navigate to "VPC Network" -> "Firewalls" -> "Add Firewall Rule".

<img width="664" alt="image" src="https://media.github.ibm.com/user/461759/files/53ea3c2a-7cb1-4be4-b557-2a74f56f598f">

<img width="758" alt="image" src="https://media.github.ibm.com/user/461759/files/7646564c-a796-4551-abaf-7f938cdc1eec">

2. Configure the firewall rule with the following details:
- Targets: All instances in the network
- Source IP ranges: 0.0.0.0/0
- Protocols and ports: tcp:8080 (adjust port if different from Flask app default)

<img width="664" alt="image" src="https://media.github.ibm.com/user/461759/files/7a5f8c44-f2c9-4e10-8510-6c848656cc24">

<img width="664" alt="image" src="https://media.github.ibm.com/user/461759/files/0772fa81-2d67-41c5-a365-4daa7098edc8">

You can now access the instance and the flask app with the External IP

<img width="788" alt="image" src="https://media.github.ibm.com/user/461759/files/84205177-4957-4360-9c01-c30505a27374">


You can now access the instance and Flask app using the External IP. Test the deployment with a ```curl``` command:

```shell
curl -X POST http://<EDIT THE IP>/predictions \
     -u admin:password \
     -H "Content-Type: application/json" \
     -d '{"fields": ["LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"], "values": [[20000.0, 2.0, 2.0, 1.0, 24.0, 2.0, 2.0, -1.0, -1.0, -2.0, -2.0, 3913.0, 3102.0, 689.0, 0.0, 0.0, 0.0, 0.0, 689.0, 0.0, 0.0, 0.0, 0.0], [120000.0, 2.0, 2.0, 2.0, 26.0, -1.0, 2.0, 0.0, 0.0, 0.0, 2.0, 2682.0, 1725.0, 2682.0, 3272.0, 3455.0, 3261.0, 0.0, 1000.0, 1000.0, 1000.0, 0.0, 2000.0]]}'
```

### Your Flask app is now deployed and ready to use as a custom ML provider for OpenScale.






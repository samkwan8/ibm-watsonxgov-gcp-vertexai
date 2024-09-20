# Monitor Google VertexAI Machine Learning Model with watsonx.gov Custom ML Provider

<img width="928" alt="image" src="https://media.github.ibm.com/user/461759/files/49250853-169b-4f97-b090-4402e8d9d33c">

## Step 1: Deploying the Machine Learning Model and create model entry in AI Factsheet

To deploy the Machine Learning Model, run the [GCP Model Building with AI Factsheet.ipynb](https://github.ibm.com/samkwan/wxgov-gcp-vertexai/blob/main/ML%20Model/notebook/GCP%20model%20training/GCP%20Model%20Building_with%20AI%20Factsheet.ipynb) to train and deploy the model on Google Cloud Platform (GCP).

1. This notebook trains a Credit Default prediction ML model using logistic regression and deploys the model with a [Custom Prediction Routine](https://cloud.google.com/vertex-ai/docs/predictions/custom-prediction-routines) as an online prediction endpoint.

2. Upload the notebook to the GCP Vertex AI Workbench JupyterLab and run all cells after updating the credentials. Alternatively, you can run the notebook elsewhere, but you will need to update the code for gcloud authentication.

3. All model training metadata will be captured and pushed to the watsonx.gov AI Factsheet.
<br/><br/>

## Step 2: Deploying the Custom ML Provider

After deploying the online endpoint, deploy a Custom ML provider as a proxy endpoint. This allows watsonx OpenScale to send prediction requests for real-time evaluation.

1. In `app.py` within the Flaskapp folder, update the `predictions_url` to your deployed endpoint URL.

2. Deploy the Flaskapp on GCP Cloud Compute Engine or App Engine by following the instructions [here](https://github.ibm.com/samkwan/wxgov-gcp-vertexai/tree/main/ML%20Model/Custom%20ML%20provider/Flaskapp)
<br/><br/>


## Step 3: Subscribing the Model on OpenScale

Subscribe the model on OpenScale for production model monitoring using the watsonx-GCP-model-subscription [notebook](https://github.ibm.com/samkwan/wxgov-gcp-vertexai/blob/main/ML%20Model/notebook/watsonx/watsonx-GCP-model-subscription.ipynb)
<br/><br/>

## Step 4: Send paylaod and feedback data to OpenScale for evalution (Optional)

Send or schedule the sample [notebook](https://github.ibm.com/samkwan/wxgov-gcp-vertexai/blob/main/ML%20Model/notebook/watsonx/watsonx-GCP-model-send%20payload%20%26%20feedback.ipynb) to send payload and feedback data for showing historical record and timeline for monitor


#After completing the above steps, go to the WatsonX monitoring dashboard (OpenScale) to find your newly subscribed model.
<img width="1661" alt="image" src="https://media.github.ibm.com/user/461759/files/d54742cd-e4aa-42e0-90d8-d69e05ea7502">
<img width="1658" alt="image" src="https://media.github.ibm.com/user/461759/files/ef083570-db64-4fa6-826d-3bae0a508a64">


# Monitor Google VertexAI Generative AI Model with Detached Prompt Template

In watsonx.gov, you can monitor nad evaluate your 3rd Party generative AI use cases with prompt template from Design time to Production time
![image](https://media.github.ibm.com/user/461759/files/9247bf38-c57a-4d1f-a7af-08fbd26ec5fe)

In this sample, we are using GCP vertexAI Gemini Pro model to perform:
1. Call center dialog summerization - [notebook](https://github.ibm.com/samkwan/wxgov-gcp-vertexai/blob/main/GenAI%20Model/notebook/Summarization/GCP-LLM-summarization.ipynb)
2. Bank FAQ document Retrieval Augmented Generation (RAG) application - [notebook](https://github.ibm.com/samkwan/wxgov-gcp-vertexai/blob/main/GenAI%20Model/notebook/RAG%20application/GCP-LLM-RAG%20Monitoring.ipynb)

## Custom Metrics

Addtionally, you can find the sample notebook to add `Custom Metrics` under the RAG application [folder](https://github.ibm.com/samkwan/wxgov-gcp-vertexai/tree/main/GenAI%20Model/notebook/RAG%20application). Adding [Human Rating](https://github.ibm.com/samkwan/wxgov-gcp-vertexai/blob/main/GenAI%20Model/notebook/RAG%20application/Custom_Metrics_Provider_for_Human_Rating.ipynb) and [LLM as a Judge](https://github.ibm.com/samkwan/wxgov-gcp-vertexai/blob/main/GenAI%20Model/notebook/RAG%20application/Custom_Metrics_Provider_for_LLM_as_judge.ipynb) metrics to OpenScale for RAG monitoring. The notebook provide a dummy score but you can add your own logic or other metrics if needed.


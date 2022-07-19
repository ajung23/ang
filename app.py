import streamlit as st
import boto3
import json

# Create a low-level client representing Amazon SageMaker Runtime
session = boto3.Session()
sagemaker_runtime = session.client('sagemaker-runtime', region_name="us-east-1")

# The name of the endpoint. The name must be unique within an AWS Region in your AWS account. 
endpoint_name='sttmodel-2022'


def generate_text(audio):
    payload = {"inputs": audio}
    response = sagemaker_runtime.invoke_endpoint(
                                EndpointName=endpoint_name, 
                                ContentType='application/json',
                                Body=json.dumps(payload)
                                )
                                
    result = json.loads(response['Body'].read().decode())
    text = result[0]['generated_text']
    return text


st.header("Audio to Text")
audio = st.file_uploader("Choose a file")
if audio is not None:
    bytes_data = audio.getvalue()
    st.write(audio)

if st.button("Run"):
    generated_text = generate_text(audio)
    st.write(generated_text)
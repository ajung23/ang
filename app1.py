import streamlit as st
import boto3
import json





# Create a low-level client representing Amazon SageMaker Runtime
session = boto3.Session(
    aws_access_key_id="ASIAQNCGA2HA3WD7ZT4I",
    aws_secret_access_key="WPJbYzJsbiKmcNM6WerwPjbXTZZFpkJayrSVpg2B",
    aws_session_token="IQoJb3JpZ2luX2VjENP//////////wEaCXVzLWVhc3QtMSJIMEYCIQC5pS3gNjgCX/qkICgnPdVoN7OCZxBd5919OGAhg//a9QIhAOS8AuOTJgG2d3ow/GsuKTVlaKa/XRH/m9kqTgRJ98c+KusBCBwQABoMMDI4MDY0MTQxNzYxIgxZMIPMs+WGlo/kVTcqyAGkNuWnzgUjx0zfgS8aCq0LuV6hmXTmbofu8BmE8YbO9CrBLfClMdh4QiAwi/CPqVGyIboHow4o+zfvhcpviM6OFlMcBzn7XKrtB2lwMpIXla2RFz/nNvrZ/YTHnWRpQwVUXCeIXA45xkj73MSTmo8hdXIIWFyqK+dmKYFNF3+igc+VCKMR2oovFKMs6NFJKrV3lVX7TezA1WILsgCBjgsbfC6lkaIW0UMxE7N5sbkLQ4+3EoPdG+nLfE9id/VKH37bpzU35uAZkzDT9tuWBjqXAZt1jDYEibWU3xYKANveqYfuz6nU1QsRSg8BvwAb+VTLyVMEFl+SsE1aIR71XaE06EaFy3t2cTl+NCBkqWDwaIEqez3cXq4EuxbrITTVM8RFHw15ZPCYNEyfFZirkwsU+bhn1w7QfsYXGnmGrmj3sdcaoWBlx7q93fVOFrtmtyyCi+a2SOkAfYO8eNmtmWZa8ECACAjpFUc=")
sagemaker_runtime = session.client('sagemaker-runtime', region_name="us-east-1")

# The name of the endpoint. The name must be unique within an AWS Region in your AWS account. 
endpoint_name='sttmodel-2022'

def generate_text(audio):
    #with open(audio, "rb") as data_file:
    payload = audio
    response = sagemaker_runtime.invoke_endpoint(
                                EndpointName=endpoint_name, 
                                ContentType='audio/x-audio',
                                Body=payload
                                               )
    result = response['Body'].read()
    #json.loads(response['Body'].read().decode())
    text = result[0]['generated_text']
    return text


st.header("Audio to Text")
audio = st.file_uploader("Choose a file")
#if audio is not None:
#    bytes_data = audio.getvalue()
#    st.write(audio)

if st.button("Run"):
    generated_text = generate_text(audio)
    st.write(generated_text)
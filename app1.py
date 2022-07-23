import streamlit as st
import boto3
import json


session = boto3.Session(
    aws_access_key_id="ASIAQNCGA2HA4ANIOIU3",
    aws_secret_access_key="vcSog5soDBAbW5eAD0qtLyoiNFWh6UO9dkreXa26",
    aws_session_token="IQoJb3JpZ2luX2VjEC8aCXVzLWVhc3QtMSJHMEUCIQCrDyt9mYsAamll2q0euuqIIMGo01kK9T//abgwcRnM0wIgbUxb9JoDrFFhRyHN3CXmBoj7WglMuDcaOywAyykTjNYq6wEIeBAAGgwwMjgwNjQxNDE3NjEiDBqL0WP/jsHZWd2FbirIAcnb/J7rSLTjYtNOi8nmyrXTfrvpbo2P5BHIiiGv5XT2Se3tgEDXvdimZu8woRboQGY7kZyTPiFogzuquBZhQP6O+CibKsVfKtuK/BXs2OmsqlyGsE2RXZxzLEvMcldf6ygQ0sdEEOhJnG+77JElFxIcnqkvAKNJuB0pxF6jSX4kCVVkZK43Q4eLvf0JdSWKm088ZPQI4kovyd81l8BmgS6CII5AG4AWBBSnyPSdCLZU+MoHHJZaT2eZLlQM5sMSC9ao6EXH+MXyMJWM8JYGOpgBNNpZSsTXlt8fOC9GsH/KHaKIu7cTefjT/JezOSCFVkryFdME8sjf92dWY6YMGZRDj1qK943tZLfTQsbYJDOxb1IAiQgkAkDB/d1Twyuz/k22IJ/F9QGpyQuZQ1cztHS6jcnD0QoCMky2sOgzryWsr8xVRJTvbFi9ji3+Ysxy9NH+8TrlXnMOZyesiudf0nhH+w91B6G9erw=")
sagemaker_runtime = session.client('sagemaker-runtime', region_name="us-east-1")

endpoint_name='sttmodel-2022'

def generate_text(audio):
    payload = audio
    response = sagemaker_runtime.invoke_endpoint(
                                EndpointName=endpoint_name, 
                                ContentType='audio/x-audio',
                                Body=payload
                                               )
    result = response['Body'].read()
    text = result
    return text


st.header("Audio to Text")
audio = st.file_uploader("Choose a file")

if st.button("Run"):
    generated_text = generate_text(audio)
    st.write(generated_text)
from flask import Flask, render_template, request, jsonify
import requests
import boto3
import pandas as pd
import boto3
#import pickle
#from isd.exception import isdException
from botocore.exceptions import ClientError
#from mypy_boto3_s3.service_resource import Bucket

s3 = boto3.client('s3')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    blog_topic = request.json.get('blog_topic')
    data = {
        "blog_topic": blog_topic
    }
    print(blog_topic)
    response = requests.post('https://v3rrrnt4k8.execute-api.us-east-1.amazonaws.com/dev/bucket', json=data)

    s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='ghhhgdkgkgdkdkkd',
    aws_secret_access_key='gjdddddddddrij'
    )

    s3.Bucket('awsbedrockcourse54').download_file(Key = "blog-output/t.txt",Filename="t.txt")
    file_path = 't.txt'

    with open(file_path, 'r') as file:
        content = file.read()
#content = re.sub(r'<h2>.*?</h2>', '', content, flags=re.DOTALL)

    print(content)
    formatted_result = content.replace('\n\n', '</p><p>')
    formatted_result = f'<p>{formatted_result}</p>'

    return jsonify({"formatted_result": formatted_result})


    #response = requests.post('https://v3rrrnt4k8.execute-api.us-east-1.amazonaws.com/dev/bucket', json=data)
    #result = response.json()
    #print(result)

    #return  jsonify(content)





if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
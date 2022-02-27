import json
import boto3
newline, bold, unbold = '\n', '\033[1m', '\033[0m'
def query_endpoint(encoded_text):
    endpoint_name = 'jumpstart-ftc-eval-v1'
    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/x-text', Body=encoded_text, Accept='application/json;verbose')
    return response

def parse_response(query_response):
    model_predictions = json.loads(query_response['Body'].read())
    probabilities, labels, predicted_label = model_predictions['probabilities'], model_predictions['labels'], model_predictions['predicted_label']
    return probabilities, labels, predicted_label

def lambda_handler(event, context):
    query_response = query_endpoint(event['text'].encode('utf-8'))
    probabilities, labels, predicted_label = parse_response(query_response)

    return {
        'statusCode': 200,
        'probabilities': json.dumps(probabilities),
        'labels': json.dumps(labels),
        'predicted_label': json.dumps(predicted_label)
    }

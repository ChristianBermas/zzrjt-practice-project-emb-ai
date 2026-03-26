import requests # Import the requests library to handle HTTP requests
import json

def sentiment_analyzer(text_to_analyse):
    url= 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    
    obj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=obj, headers=headers)

    print(response.status_code)

    obj = { "raw_document": { "text": "Testing this application for error handling" } }
    
    response = requests.post(url, json=myobj, headers=headers)

    print(response.status_code)

    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        # If the response status code is 500, set label and score to None elif response.status_code == 500: label = None score = None
        return {'label': label, 'score': score}

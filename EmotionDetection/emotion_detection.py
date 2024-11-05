import requests
import json

def default_emotion_response():
    """
    Returns a JSON-formatted dictionary with None values for each emotion
    and dominant_emotion.
    """
    # Create a dictionary with None values for each emotion
    emotion_dict = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
    # Return the JSON-formatted string
    return json.dumps(emotion_dict, indent=4)

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Check if input is blank
    if not text_to_analyze.strip():
        # Return default response for blank input
        return default_emotion_response()
    
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Sending the POST request to the Watson NLP EmotionPredict function
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the response status code is 400
    if response.status_code == 400:
        # Return default response for server error
        return default_emotion_response()
    
    # If the request is successful, process the response
    if response.status_code == 200:
        response_data = response.json()
        
        # Extract emotion scores from the first element of 'emotionPredictions'
        emotions = response_data['emotionPredictions'][0]['emotion']
        
        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Construct the final dictionary
        emotion_dict = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }
        
        # Return the JSON-formatted dictionary
        return json.dumps(emotion_dict, indent=4)

    # Return a generic error response if the status is not 200 or 400
    return json.dumps({"error": "Unexpected server response."}, indent=4)

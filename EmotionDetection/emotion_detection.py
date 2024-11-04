# final_project/emotion_detection.py
import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Sending the POST request to the Watson NLP EmotionPredict function
    response = requests.post(url, headers=headers, json=data)
    
    # Convert the response to JSON
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
    
    # Return the formatted dictionary
    return json.dumps(emotion_dict, indent=4)
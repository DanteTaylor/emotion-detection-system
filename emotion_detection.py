import requests  # Importing requests to send HTTP requests

def emotion_detector(text_to_analyse):
    """
    Function to detect emotions in the given text using Watson's Emotion Predict function.

    Parameters:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: The emotion analysis results containing the detected emotions and their scores.
    """
    # Define the API URL and Headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Set up the JSON payload
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Send a POST request to the Emotion Predict endpoint
    response = requests.post(url, headers=headers, json=input_json)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response if successful
    else:
        # Return an error message if the request fails
        return {"error": f"Request failed with status code {response.status_code}"}

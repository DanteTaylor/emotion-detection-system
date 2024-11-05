from flask import Flask, request, jsonify, render_template, Response
from EmotionDetection import emotion_detector
import json

app = Flask("Emotion Detector")

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    # Retrieve the text input
    text_to_analyze = request.args.get('textToAnalyze') if request.method == 'GET' else request.get_json().get('textToAnalyze')

    # Check if text is provided
    if not text_to_analyze:
        return jsonify({"error": "No text provided for analysis."}), 400

    # Call the emotion detector function
    result_json = emotion_detector(text_to_analyze)
    result = json.loads(result_json)

    # Check if dominant_emotion is None
    if result['dominant_emotion'] is None:
        # Set formatted_response to the error message
        formatted_response = "Invalid text! Please try again!"

    else:
        # Format the response for valid input
        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )

    return Response(formatted_response, content_type='text/plain')

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

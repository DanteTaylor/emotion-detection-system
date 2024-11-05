# test_emotion_detection.py
import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy_emotion(self):
        result = emotion_detector("I am glad this happened")
        self.assertIn('"dominant_emotion": "joy"', result, "Expected dominant emotion to be 'joy'.")

    def test_anger_emotion(self):
        result = emotion_detector("I am really mad about this")
        self.assertIn('"dominant_emotion": "anger"', result, "Expected dominant emotion to be 'anger'.")

    def test_disgust_emotion(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertIn('"dominant_emotion": "disgust"', result, "Expected dominant emotion to be 'disgust'.")

    def test_sadness_emotion(self):
        result = emotion_detector("I am so sad about this")
        self.assertIn('"dominant_emotion": "sadness"', result, "Expected dominant emotion to be 'sadness'.")

    def test_fear_emotion(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertIn('"dominant_emotion": "fear"', result, "Expected dominant emotion to be 'fear'.")

if __name__ == "__main__":
    unittest.main()

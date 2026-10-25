
import unittest
from unittest.mock import patch, Mock

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy_is_dominant(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.01,
                        "fear": 0.02,
                        "joy": 0.90,
                        "sadness": 0.06
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am happy")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_required_keys(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.10,
                        "disgust": 0.10,
                        "fear": 0.10,
                        "joy": 0.60,
                        "sadness": 0.10
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("This is a test")

        expected_keys = {
            "anger", "disgust", "fear",
            "joy", "sadness", "dominant_emotion"
        }
        self.assertEqual(set(result.keys()), expected_keys)


if __name__ == "__main__":
    unittest.main()

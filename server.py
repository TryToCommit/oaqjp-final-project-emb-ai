'''Deploy a flask application which functions to analyze a string of text given by the user,
and measure sentiment. Emotions are scored, the prevailing emotion is identified
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_analysis():
    """A string of text can be entered by the user which is then passed as the argument
    for the emotion_detector function. The text is analyzed and subsequently scored
    based on different emotions,
    for example joy or fear. One emotion is determined as the most dominant based on score
    and is labelled as such."""

    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route('/')
def index():
    """Displays the index page to the user allowing for capture of user text and
    display of analysis results"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

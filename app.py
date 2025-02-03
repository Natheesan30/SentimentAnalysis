from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        sentiment = analyze_sentiment(text)
        return render_template("index.html", sentiment=sentiment, text=text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
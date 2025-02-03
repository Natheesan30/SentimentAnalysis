from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get sentiment polarity (-1 to 1, where -1 is negative, 1 is positive)
    polarity = blob.sentiment.polarity
    
    # Determine sentiment based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    # Test the function
    text = input("Enter a sentence: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")
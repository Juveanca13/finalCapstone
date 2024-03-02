# Import the necessary libraries
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Download the dataset of product reviews
df = pd.read_csv("amazon_product_reviews.csv")

# Load the en_core_web_sm spaCy model
nlp = spacy.load("en_core_web_sm")

# Add the SpacyTextBlob component to the pipeline
nlp.add_pipe("spacytextblob")

# Select the 'reviews.text' column from the dataset and retrieve its data
reviews_data = df["reviews.text"]

# Remove all missing values from this column
clean_data = df.dropna(subset=["reviews.text"])

# Define a function for sentiment analysis
def sentiment_analysis(review):
  # Create a spaCy document object
  doc = nlp(review)
  # Return the polarity score and the sentiment label
  polarity = doc._.polarity
  if polarity > 0:
    sentiment = "positive"
  elif polarity < 0:
    sentiment = "negative"
  else:
    sentiment = "neutral"
  return polarity, sentiment

# Test the model on sample product reviews
# You can choose any reviews from the dataset or write your own
sample_reviews = [
  "I love this product. It works great and has many useful features.",
  "This product is terrible. It broke after one week and the customer service was awful.",
  "This product is okay. It does what it is supposed to do, but nothing more."
]

# Loop through the sample reviews and print the results
for review in sample_reviews:
  polarity, sentiment = sentiment_analysis(review)
  print(f"Review: {review}")
  print(f"Polarity: {polarity}")
  print(f"Sentiment: {sentiment}")
  print()

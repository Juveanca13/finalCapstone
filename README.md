# finalCapstone
Overview
This repository contains a sentiment analysis project focusing on Amazon product reviews. The goal of this project is to analyze the sentiment expressed in consumer reviews using natural language processing techniques.

Dataset
The dataset utilized for this project is the Consumer Reviews of Amazon Products obtained from Datafiniti. It comprises over 34,000 reviews of various Amazon products including Kindle, Fire TV, etc. The dataset encompasses 24 columns, encompassing essential information such as product name, manufacturer, review title, review text, rating, and more. You can access the dataset here.

Preprocessing
Prior to sentiment analysis, several preprocessing steps were carried out. These steps included selecting the 'reviews.text' column from the dataset, handling missing values, removal of stopwords, and basic text cleaning utilizing methods like lower(), strip(), and str().

Sentiment Analysis Model
The sentiment analysis model was built using spaCy, a Python library for natural language processing. Specifically, the model employed the en_core_web_sm spaCy model and integrated the SpacyTextBlob component, which facilitates sentiment analysis as a spaCy pipeline component. The model is capable of predicting sentiment polarity scores ranging from -1 (very negative) to 1 (very positive), along with sentiment labels categorized as positive, negative, or neutral.

Evaluation
The model was rigorously evaluated on a diverse set of product reviews, encompassing positive, negative, and neutral sentiments. The evaluation showcased the model's ability to accurately predict sentiment polarity scores and labels. Sample reviews and their corresponding predictions are detailed below:

Review: I love this product. It works great and has many useful features.

Polarity: 0.5
Sentiment: Positive
Review: This product is terrible. It broke after one week and the customer service was awful.

Polarity: -0.9167
Sentiment: Negative
Review: This product is okay. It does what it is supposed to do, but nothing more.

Polarity: 0.0
Sentiment: Neutral
Insights
While the model exhibits strengths in terms of simplicity, efficiency, and accuracy for straightforward product reviews, it does have its limitations. It may struggle to capture the subtleties of human language such as sarcasm, irony, or humor. Additionally, biases inherent in the choice of the spaCy model and the SpacyTextBlob component could affect the model's performance, potentially leading to skewed results. Future enhancements could involve the utilization of more sophisticated spaCy models or the development of custom sentiment classifiers trained on the dataset to mitigate these limitations.

Contributions
Contributions to this project are welcome! If you're interested in improving the sentiment analysis model or have suggestions for enhancements, feel free to submit a pull request.

License
This project is licensed under the MIT License. Feel free to use and modify this code for your own purposes.

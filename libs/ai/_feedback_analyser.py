from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
	sid = SentimentIntensityAnalyzer()
	sentiment_dict = sid.polarity_scores(sentence)
	
	if sentiment_dict['compound'] >= 0.1 :
		print("Positive")

	elif sentiment_dict['compound'] <= - 0.1 :
		print("Negative")

	else :
		print("Neutral")




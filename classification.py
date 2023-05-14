from sklearn.datasets import fetch_20newsgroups
import pandas as pd
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

categories = ['rec.sport.baseball', 'rec.sport.hockey']
sports_dataset = fetch_20newsgroups(subset='train', shuffle=True, random_state=42, categories=categories)
print('oK')
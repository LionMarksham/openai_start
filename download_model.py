import openai
import os
openai.api_key="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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

result=response.choices[0].text
print(result)
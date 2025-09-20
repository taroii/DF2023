import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL_cat = "https://api-inference.huggingface.co/models/taroii/datafest_category"
headers_cat = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}"}


def query_cat(payload):
  response = requests.post(API_URL_cat, headers=headers_cat, json=payload)
  return response.json()


API_URL_sub = "https://api-inference.huggingface.co/models/taroii/datafest_subcategory"
headers_sub = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}"}


def query_sub(payload):
  response = requests.post(API_URL_sub, headers=headers_sub, json=payload)
  return response.json()

warmup = query_cat({
  "inputs": "I like you. I love you",
})

print(warmup)

warmup2 = query_sub({
  "inputs": "I like you. I love you",
})
print(warmup2)

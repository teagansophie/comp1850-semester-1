"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object
print(f"Status code: {response.status_code}")

if response.status_code == 200:
    print(response.json())      # response object, json() method
else: 
    print(f"Status code is {response.status_code} not 200.")

#!/usr/bin/env python3
import requests
import json

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    """Authenticate and return API key."""
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth=authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Auth failed: {r.status_code} - {r.text}")

def deleteBook(book_id, apiKey):
    """Delete a book by ID using DELETE request."""
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{book_id}",
        headers={
            "accept": "application/json",
            "X-API-KEY": apiKey
        }
    )
    if r.status_code == 200:
        print(f"✅ Book with ID {book_id} deleted successfully.")
    elif r.status_code == 404:
        print(f"⚠️  Book with ID {book_id} not found.")
    else:
        print(f"❌ Error deleting book {book_id}: {r.status_code} - {r.text}")

# Get authentication token
apiKey = getAuthToken()

# Loop through the same range of book IDs you added earlier
for i in range(4, 105):
    deleteBook(i, apiKey)

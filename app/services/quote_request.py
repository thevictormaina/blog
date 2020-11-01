import json
import urllib.request

api_url = None

def configure_request(app):
    global api_url
    api_url = app.config["QUOTE_URL"]

def request_quote():
    with urllib.request.urlopen(api_url) as url:
        api_return = url.read()
        api_response = json.loads(api_return)

        quote = {"author":None, "quote":None}

        if api_response["quote"]:
            quote["author"] = api_response["author"]
            quote["quote"] = api_response["quote"]

    return quote

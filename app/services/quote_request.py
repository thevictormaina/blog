def configure_request(app):
    global api_key, base_url
    api_key = app.config["QUOTES_API_KEY"]
    base_url = app.config["QUOTES_BASE_URL"]
def configure_request(app):
    global api_key, base_url
    api_key = app.config["QUOTE_API_KEY"]
    base_url = app.config["QUOTE_BASE_URL"]
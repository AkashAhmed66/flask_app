def format_response(data, message="Success"):
    return {
        "status": "ok",
        "message": message,
        "data": data
    }

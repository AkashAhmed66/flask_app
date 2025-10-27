from flask import request, jsonify

def register_middlewares(app):

    @app.before_request
    def check_auth():
        if request.endpoint == 'user.create_user':  # Example: protect route
            token = request.headers.get('Authorization')
            if not token or token != 'Bearer mysecrettoken':
                return jsonify({"error": "Unauthorized"}), 401

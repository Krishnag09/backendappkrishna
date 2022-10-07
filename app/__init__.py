from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.api.routes import back

    # init blueprints
    app.register_blueprint(back)

    return app

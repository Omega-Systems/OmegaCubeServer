from flask import Flask, render_template, request, session, redirect

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "5303a2a95729ab962cdd8ff7d4216dc3b7904703078ed3c6bab85f7cff9e02ff"
    
    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
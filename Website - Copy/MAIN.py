from flask import Flask
from views import views




Main = Flask(__name__)
Main.register_blueprint(views, url_prefix="/")


if __name__ == "__main__":
    Main.run(debug=True, port=6400)

import os
from flask_migrate import Migrate
from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")

app.config["SECRET_KEY"] = "abcdefg123456"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

login_manager.init_app(app)

cfg_name = os.environ.get("CONFIG_NAME") or 'DevConfig'
app.config.from_object(f"blog.configs.{cfg_name}")

migrate = Migrate(app, db)

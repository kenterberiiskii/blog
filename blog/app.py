import os
from flask_migrate import Migrate
from flask import Flask, render_template

from blog.security import flask_bcrypt
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app
from blog.views.users import users_app


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

flask_bcrypt.init_app(app)


@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    from blog.models import User

    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"

    db.session.add(admin)
    db.session.commit()

    print("created admin:", admin)

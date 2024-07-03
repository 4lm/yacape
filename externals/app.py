from flask import Flask

from externals.db import db
from externals.use_cases.user_register.routes import user_register_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(user_register_routes)

if __name__ == '__main__':
    app.run(debug=True)

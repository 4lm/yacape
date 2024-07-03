from flask import Flask, request, jsonify, render_template
from externals.db import db

from externals.views.register_user_view import register_user_view

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def html_register_user():
    if request.method == 'POST':
        data = request.form
        view = register_user_view(data)
        if view.error:
            return render_template('user_register.html', error=view.error)
        return render_template('user_register_success.html', name=view.name, creation_time=view.creation_time)
    return render_template('user_register.html')

@app.route('/api/user/register', methods=['POST'])
def api_register_user():
    data = request.get_json()
    view = register_user_view(data)
    if view.error:
        return jsonify({'error': view.error}), 409
    return jsonify({'name': view.name, 'creation_time': view.creation_time}), 200

if __name__ == '__main__':
    app.run(debug=True)

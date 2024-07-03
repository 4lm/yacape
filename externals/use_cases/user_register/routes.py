from flask import Blueprint, request, jsonify, render_template

from externals.use_cases.user_register.view import user_register_view

user_register_routes = Blueprint(
    'user_register',
    __name__,
    template_folder='templates'
)

@user_register_routes.route('/', methods=['GET', 'POST'])
def html_user_register():
    if request.method == 'POST':
        data = request.form
        view = user_register_view(data)
        if view.error:
            return render_template('user_register.html', error=view.error)
        return render_template('user_register_success.html', name=view.name, creation_time=view.creation_time)
    return render_template('user_register.html')

@user_register_routes.route('/api/user/register', methods=['POST'])
def api_user_register():
    data = request.get_json()
    view = user_register_view(data)
    if view.error:
        return jsonify({'error': view.error}), 409
    return jsonify({'name': view.name, 'creation_time': view.creation_time}), 200

from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
import pdb # debug

# Enable HTTPS
# Hot Reload: app.run(debug=True)
# Debugger
# Mock HTTP(S) responses
# Sessions
# Database Setup
# Database Migrations
# Return response:
#   200, 404 etc, minetype, headers etc
# Redirects
# Authorization
# OAuth client (Google etc)
# Payments

app = Flask(__name__)

@app.route('/')
def hello():
    #pdb.set_trace()
    #raise
    return 'Hi There'

def _get_users():
    return [
        {
            'id': '42',
            'username': 'bob'
        },
        {
            'id': '88',
            'username': 'john'
        }
    ]

@app.route('/users')
def users():
    users = _get_users()
    return make_response(jsonify(users))

def _lookup_user(id):
    users = _get_users()
    result = None
    for user in users:
        if user['id'] == id:
            result = user
            break
    return result

def _error_not_found():
    return {'error': 'resource not found'}

@app.route('/users/<id>')
def user(id):
    user = _lookup_user(id)
    error = _error_not_found()
    if user:
        data, status = user, 200
    else:
        data, status = error, 404
    return make_response(jsonify(data), status)

if __name__ == '__main__':
    app.run(debug=True)


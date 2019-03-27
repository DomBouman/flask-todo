from flask import Flask, request


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return 'This is a flask-boilerplate project, not to be used in production.'

    @app.route('/hello')
    def hello():
        name = request.args.get('name', 'World')
        return f"Hello {name}"

    @app.route('/number/<n>')
    def number_route(n):
        return f"Number: {n}"

    @app.route('/method', methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
    def method_route():
        if request.method == 'GET':
            return f'HTTP Method: GET'
        elif request.method == 'POST':
            return f'HTTP Method: POST'
        elif request.method == 'PATCH':
            return f'HTTP Method: PATCH'
        elif request.method == 'PUT':
            return f'HTTP Method: PUT'
        elif request.method == 'DELETE':
            return f'HTTP Method: DELETE'

    @app.route('/status')
    def status_route():
        code = request.args.get('c', 200)
        resposnse = make_response(f"status: {code}", code)

    return app

from flask import Flask
from flask_sslify import SSLify

def create_app(test_config=None):

    app = Flask(__name__)
    print(f'app.debug: {app.debug}')
    print(f'app.testing: {app.testing}')
    print(f'app.config: {app.config}')
    sslify = SSLify(app, age=300)
    print(f'Application has been SSLified')

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

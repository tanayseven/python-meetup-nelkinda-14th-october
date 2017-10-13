def load_config(app, env='dev'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' if env == 'dev' else 'sqlite:///app_test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

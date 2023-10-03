from blueprints.buku_controller import bukuApi

def register_blueprints(app):
    app.register_blueprint(bukuApi, url_prefix='/')

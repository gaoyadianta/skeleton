from name.api import name_bp

# register blueprint
def register(app):
    print('name register')
    app.register_blueprint(name_bp)

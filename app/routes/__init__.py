from .student import student_router
from .auth import auth_router

def init_routes(app):
    app.register_blueprint(student_router, url_prefix='/students')
    app.register_blueprint(auth_router, url_prefix='/auth')

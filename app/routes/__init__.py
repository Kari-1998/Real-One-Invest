from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__)
property_bp = Blueprint('property_bp', __name__)
investment_bp = Blueprint('investment_bp', __name__)

def setup_routes(app):
    from app.routes.auth_routes import auth_bp
    from app.routes.property_routes import property_bp
    from app.routes.investment_routes import investment_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(property_bp, url_prefix='/api/properties')
    app.register_blueprint(investment_bp, url_prefix='/api/investments')

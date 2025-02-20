from flask import Blueprint

property_bp = Blueprint('property', __name__)

@property_bp.route('/', methods=['GET'])
def get_properties():
    return {"message": "List of properties"}

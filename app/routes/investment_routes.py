from flask import Blueprint

investment_bp = Blueprint('investment', __name__)

@investment_bp.route('/', methods=['GET'])
def get_investments():
    return {"message": "List of investments"}

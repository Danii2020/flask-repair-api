from flask import Blueprint

teapot_bp = Blueprint('teapot_bp', __name__)

@teapot_bp.route('', methods=['GET'])
def status():
    return "I'm a teapot", 418
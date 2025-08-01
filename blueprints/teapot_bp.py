from flask import Blueprint

teapot_bp = Blueprint('teapot_bp', __name__)

@teapot_bp.route('', methods=['POST'])
def status():
    return "I'm a teapot", 418
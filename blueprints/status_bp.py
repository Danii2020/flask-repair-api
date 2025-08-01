from flask import Blueprint, jsonify, current_app

status_bp = Blueprint('status_bp', __name__)

@status_bp.route('', methods=['GET'])
def status():
    return jsonify({"damaged_system": current_app.config["DAMAGED_SYSTEM"]})
from flask import Blueprint, request, jsonify
from data import saturation_table

phase_bp = Blueprint('phase_bp', __name__)

@phase_bp.route('', methods=['GET'])
def phase_change():
    p = request.args.get('pressure', type=float)
    if p is None:
        return jsonify({"description": "Missing or invalid 'pressure' parameter"}), 400
    props = saturation_table.get(p)
    if not props:
        return jsonify({"description": f"No data for pressure = {p} MPa"}), 404
    v_l, v_v = props
    return jsonify({
        "specific_volume_liquid": v_l,
        "specific_volume_vapor": v_v
    })

from flask import Blueprint, render_template_string, current_app
from data import repair_codes

repair_bay_bp = Blueprint('repair_bay_bp', __name__)

@repair_bay_bp.route('', methods=['GET'])
def repair_bay():
    code = repair_codes[current_app.config["DAMAGED_SYSTEM"]]
    html = render_template_string(
        """
        <!DOCTYPE html>
        <html>
        <head><title>Repair Bay</title></head>
        <body>
          <div class=\"anchor-point\">{{ code }}</div>
        </body>
        </html>
        """,
        code=code
    )
    return html, 200, {'Content-Type': 'text/html'}
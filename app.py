from flask import Flask, jsonify, render_template_string
import random
from flask_swagger_ui import get_swaggerui_blueprint

# API version
API_VERSION = 'v1'
API_PREFIX = f'/api/{API_VERSION}'

# Initialize Flask app, serve static files under /api/v1/static
app = Flask(
    __name__,
    static_folder='static',
    static_url_path=f'{API_PREFIX}/static'
)

# Swagger UI configuration
SWAGGER_URL = f'{API_PREFIX}/docs'
API_URL = f'{API_PREFIX}/static/swagger.yaml'  # swagger spec served from static/swagger.yaml
swaggerui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Flask Repair API"}
)
app.register_blueprint(swaggerui_bp, url_prefix=SWAGGER_URL)

# List of possible damaged systems
damaged_systems = [
    "navigation",
    "communications",
    "life_support",
    "engines",
    "deflector_shield"
]

# Mapping of repair codes
repair_codes = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Randomly pick a damaged system on startup
damaged_system = random.choice(damaged_systems)

@app.route(f'{API_PREFIX}/status', methods=['GET'])
def status():
    """
    Returns currently damaged system in JSON:
    { "damaged_system": "<system_name>" }
    """
    return jsonify({"damaged_system": damaged_system})

@app.route(f'{API_PREFIX}/repair-bay', methods=['GET'])
def repair_bay():
    """
    Serves HTML page with repair code:
    <div class="anchor-point">REPAIR_CODE</div>
    """
    code = repair_codes[damaged_system]
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

@app.route(f'{API_PREFIX}/teapot', methods=['POST'])
def teapot():
    """
    Returns HTTP 418 I'm a teapot
    """
    return "I'm a teapot", 418

@app.route(f'{API_PREFIX}/', methods=['GET'])
def home():
    html = render_template_string(
    """
    <!DOCTYPE html>
    <html>
    <head><title>Repair Bay</title></head>
    <body>
        <h1>Hey, hope you are having a great day in space!</h1>
    </body>
    </html>
    """
    )
    return html, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    app.run(debug=True)

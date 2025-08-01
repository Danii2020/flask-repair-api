from flask import Flask, render_template_string
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from data import damaged_systems
from blueprints.status_bp import status_bp
from blueprints.repair_bay_bp import repair_bay_bp
from blueprints.phase_change_bp import phase_bp
from blueprints.teapot_bp import teapot_bp
import random

# API version
API_VERSION = 'v1'
API_PREFIX = f'/api/{API_VERSION}'

# Initialize Flask app, serve static files under /api/v1/static
app = Flask(
    __name__,
    static_folder='static',
    static_url_path=f'{API_PREFIX}/static'
)
CORS(app)

# Swagger UI configuration
SWAGGER_URL = f'{API_PREFIX}/docs'
API_URL = f'{API_PREFIX}/static/swagger.yaml'  # swagger spec served from static/swagger.yaml
swaggerui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Flask Repair API"}
)

# pick damaged system once
app.config['DAMAGED_SYSTEM'] = random.choice(damaged_systems)

# register blueprints
app.register_blueprint(swaggerui_bp, url_prefix=SWAGGER_URL)
app.register_blueprint(status_bp, url_prefix="/status")
app.register_blueprint(repair_bay_bp, url_prefix="/repair-bay")
app.register_blueprint(phase_bp, url_prefix="/phase-change-diagram")
app.register_blueprint(teapot_bp, url_prefix="/teapot")

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

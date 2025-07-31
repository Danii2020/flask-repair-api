from flask import Flask, jsonify, render_template_string, abort
import random

app = Flask(__name__)

# List of possible damaged systems
damaged_systems = [
    "navigation",
    "communications",
    "life_support",
    "engines",
    "deflector_shield"
]

# Codes for repair-bay
repair_codes = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Random choice of the damaged system
damaged_system = random.choice(damaged_systems)

@app.route('/status', methods=['GET'])
def status():
    """
    Returns the state of the system.
    { "damaged_system": "<system>" }
    """
    return jsonify({"damaged_system": damaged_system})

@app.route('/repair-bay', methods=['GET'])
def repair_bay():
    """
    Generates the HTML with <div class="anchor-point">CODE</div>
    where CODE is the table.
    """
    code = repair_codes.get(damaged_system)
    html = render_template_string(
        """
        <!DOCTYPE html>
        <html>
        <head><title>Repair</title></head>
        <body>
        <div class="anchor-point">{{ code }}</div>
        </body>
        </html>
        """,
        code=code
    )
    return html, 200, {'Content-Type': 'text/html'}

@app.route('/teapot', methods=['POST'])
def teapot():
    """
    Returns HTTP 418 I'm a teapot
    """
    return "I'm a teapot", 418

if __name__ == '__main__':
    # Run the app
    app.run()

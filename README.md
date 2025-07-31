# Flask Repair API

**Flask Repair API** is a lightweight Python application built with Flask that simulates a spaceship diagnostics and repair system. It provides three endpoints to:

* Check system status (
  GET `/status`)
* Retrieve an HTML repair code page (GET `/repair-bay`)
* Demonstrate a playful HTTP 418 response (POST `/teapot`)

---

## Features

* **Random Damage Simulation**: On startup, a random system is marked as damaged.
* **JSON Status Endpoint**: `/status` returns the damaged system in JSON.
* **Dynamic Repair Page**: `/repair-bay` serves an HTML page with a `<div class="anchor-point">REPAIR_CODE</div>` containing the repair code.
* **HTTP 418 Teapot**: `/teapot` returns HTTP status 418 "I'm a teapot".

---

## Prerequisites

* **Python**: Version 3.7 or higher.
* **Flask**: Installed via `pip install flask`.

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/flask-repair-api.git
   cd flask-repair-api
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Start the Flask application:

```bash
python app.py
```

By default, Flask listens on `0.0.0.0:5000`. You can override host and port by editing the `app.run()` call in `app.py`.

---

## Endpoints

### 1. GET `/status`

* **Description**: Returns the currently damaged system.
* **Response**:

  * **Status**: 200 OK
  * **Body** (JSON):

    ```json
    {
      "damaged_system": "<system_name>"
    }
    ```
  * **system\_name** one of:

    * `navigation`
    * `communications`
    * `life_support`
    * `engines`
    * `deflector_shield`

### 2. GET `/repair-bay`

* **Description**: Serves an HTML page with the repair code for the damaged system.
* **Response**:

  * **Status**: 200 OK
  * **Headers**: `Content-Type: text/html`
  * **Body** (HTML):

    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>Repair Bay</title>
    </head>
    <body>
      <div class="anchor-point">REPAIR_CODE</div>
    </body>
    </html>
    ```
  * `REPAIR_CODE` mapping:

    | Damaged System    | Repair Code |
    | ----------------- | ----------- |
    | navigation        | NAV-01      |
    | communications    | COM-02      |
    | life\_support     | LIFE-03     |
    | engines           | ENG-04      |
    | deflector\_shield | SHLD-05     |

### 3. POST `/teapot`

* **Description**: Returns a playful HTTP 418 "I'm a teapot" response.
* **Response**:

  * **Status**: 418 I'm a teapot
  * **Body**: `I'm a teapot`

---

## Project Structure

```
flask-repair-api/
├── app.py             # Main Flask application
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## Best Practices

* **Virtual Environments**: Use `venv` to isolate dependencies.
* **Configuration**: Keep secrets and configuration out of source code (e.g., use environment variables).
* **Docstrings**: Document routes and functions for clarity.
* **Error Handling**: Validate inputs and handle unexpected errors gracefully.
* **Testing**: Write unit and integration tests (not included here).

---

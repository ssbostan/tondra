# Continuous Development on Kubernetes environments.
# With application healthchecks and Zero-downtime deployment model.
# Using Kubernetes, Helm, Skaffold
# Copyright 2021, Saeid Bostandoust <ssbostan@linuxmail.org>

from os import getcwd
from flask import Flask, url_for
from random import randrange

app = Flask(__name__)

app.config["JSONIFY_PRETTYPRINT_REGULAR"] = 1

NUM_REQUESTS = 0
HEALTH_STATUS = 1

RANDOM_TARGET_POINT = randrange(100, 500)

with open(getcwd() + "/.appinfo") as f:
  APP_INFO = f.read().split(":")

@app.before_request
def compute_request():
    global NUM_REQUESTS, HEALTH_STATUS
    if NUM_REQUESTS >= RANDOM_TARGET_POINT:
        HEALTH_STATUS = 0
    NUM_REQUESTS += 1

@app.route("/")
def index():
    return f"""<!DOCTYPE html>
<html>
    <body>
        <div id="main">
            <h1>Available endpoints:</h1>
            <ul>
                <li><a href="{url_for('appinfo')}">/appinfo</a></li>
                <li><a href="{url_for('livez')}">/livez</a></li>
                <li><a href="{url_for('readyz')}">/readyz</a></li>
            </ul>
            <a href="https://github.com/ssbostan/tondra">tondra</a>
        </div>
    </body>
</html>"""

@app.route("/livez")
def livez():
    """
    Endpoint to check application liveness.
    Use this endpoint in Kubernetes livenessProbe property.
    """
    # Write your healthcheck code here.
    if HEALTH_STATUS:
        return "up", 200
    return "down", 500

@app.route("/readyz")
def readyz():
    """
    Endpoint to check application readiness.
    Use this endpoint in Kubernetes readinessProbe property.
    """
    # Write your healthcheck code here.
    if HEALTH_STATUS:
        return "up", 200
    return "down", 500

@app.route("/appinfo")
def appinfo():
    """
    Endpoint of the application info and version.
    Showing current release and application target point and status.
    """
    return {
        "app_version": APP_INFO[0].strip(),
        "git_commit": APP_INFO[1].strip(),
        "target_point": RANDOM_TARGET_POINT,
        "num_requests": NUM_REQUESTS,
        "health_status": HEALTH_STATUS
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

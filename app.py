# Continuous Development on Kubernetes environments.
# With application healthchecks and Zero-downtime deployment model.
# Using Kubernetes, Helm, Skaffold
# Copyright 2021, Saeid Bostandoust <ssbostan@linuxmail.org>

from flask import Flask

app = Flask(__name__)

with open("/opt/app/.appinfo") as f:
  APP_INFO = f.read().split(":")

@app.route("/livez")
def livez():
    """
    Endpoint to check application liveness.
    Use this endpoint in Kubernetes livenessProbe property.
    """
    # Write your healthcheck code here.
    return "", 204

@app.route("/readyz")
def readyz():
    """
    Endpoint to check application readiness.
    Use this endpoint in Kubernetes readinessProbe property.
    """
    # Write your healthcheck code here.
    return "", 204

@app.route("/appinfo")
def appinfo():
    """
    Endpoint of application info and version.
    Showing appVersion and gitCommit of current release.
    """
    return {
        "appVersion": APP_INFO[0].strip(),
        "gitCommit": APP_INFO[1].strip()
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

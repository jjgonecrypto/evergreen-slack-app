import json

from flask import Flask, request, make_response, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Evergreen rulez!"

# handles /jevg in Slack right now
@app.route("/evg", methods=['POST'])
def evg():
    slack_event = request.get_json()
    app.logger.info("test") # not working for some reason
    return "You have started subscribing for patches"

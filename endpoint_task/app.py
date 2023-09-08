from flask import Flask, request
import json
import requests
import datetime


app = Flask(__name__)

@app.route("/api", methods["GET"])
def create_endpoint():
    """GET request query parameter that get the slack name and track"""
    track = request.args.get("track")
    slack_name = request.args.get("slack_name")

    """Get the current day of the week"""
    current_day = datetime.datetime.now().strftime("%A")

    """Get the current UTC time"""
    current_time = datetime.datetime.utcnow()

    """Get the GitHub URL """
    

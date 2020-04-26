from flask import Flask, render_template, send_from_directory
from flask import redirect, url_for, session, request

from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin
import os
import json

app = Flask(__name__, template_folder="build", static_folder="build/static")
cors = CORS(app)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = set()
messages = list()


@app.route('/')
@cross_origin()
def home():
    return redirect(url_for("welcome"))


@app.route('/welcome')
@cross_origin()
def welcome():
    return render_template("login.html")


@app.route("/welcome/submit_name", methods=["GET", "POST"])
@cross_origin()
def welcome_submit_name():

    if request.method == "POST":
        print("in submit")
        name = request.json['username']
        users.add(name)
        return url_for("messenger", username=name)

    return "username denied"


@app.route("/messenger/<username>")
@cross_origin()
def messenger(username):
    print("in message: ", username)
    return render_template("messenger.html")


@app.route("/messenger/<username>/get_name")
@cross_origin()
def messenger_get_name(username):
    return username


@socketio.on("send message")
@cross_origin()
def handle_message(data):
    print("message recieved from ", data["username"], ": ", data["message"])
    username_message_pair = {"username": data["username"], "message": data["message"]}
    messages.append(username_message_pair)
    username_message_pair_json = json.dumps(username_message_pair)
    emit("receive message", {"username_message_pair": username_message_pair_json}, broadcast=True)

    print("message sent to all")

    return "ok"


@socketio.on("fetch init messages")
@cross_origin()
def fetch_init_messages():

    print("fetching all messages...")
    message_json = json.dumps(messages)
    emit("receive init messages", {"username_message_pairs": message_json})
    print("all messages sent")

    return "ok"


@app.route("/manifest.json")
def manifest():
    return send_from_directory('./build', 'manifest.json')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('./build', 'favicon.ico')


@app.route('/logo192.png')
def logo192():
    return send_from_directory('./build', 'logo192.png')


@app.route('/logo512.png')
def logo512():
    return send_from_directory('./build', 'logo512.png')


if __name__ == '__main__':
    socketio.run(app, debug=True)

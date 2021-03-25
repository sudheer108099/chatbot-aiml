from flask import Flask, render_template, request
import src.main as bot

kernel = bot.kernel

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["post"])
def get_bot_response():
    user_msg = request.args.get('msg')
    return kernel.respond(user_msg)

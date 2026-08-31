from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

emotions = ["Happy", "Sad", "Angry", "Surprised", "Neutral"]

@app.route("/")
def index():
    return render_template("index.html")

def generate_emotions():
    while True:
        emotion = random.choice(emotions)

        socketio.emit("emotion_update", {
            "emotion": emotion
        })

        time.sleep(3)

thread = threading.Thread(target=generate_emotions)
thread.daemon = True
thread.start()

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5050)
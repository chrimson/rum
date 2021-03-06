from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route("/")
def index():
    i = random.randint(1, 10000000)
    return render_template("index.html", text = i)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

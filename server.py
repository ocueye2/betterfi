from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

ITEMS = os.listdir("desktop")

print(ITEMS)

@app.route("/")
def index():
    return render_template("index.html", items=ITEMS)

@app.route("/select", methods=["POST"])
def select():
    data = request.json
    selected = data.get("item")
    if selected:
        print(f"Running: {selected}")
        with open(os.path.join("desktop",selected,"run")) as f:

            os.system(f"{f.read()} &")  # Run in background
    return jsonify({"status": "ok", "selected": selected})

if __name__ == "__main__":
    app.run(debug=True)

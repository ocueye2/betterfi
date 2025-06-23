from flask import Flask, render_template, request, jsonify, send_file
import os

app = Flask(__name__,"/static","static")

# cache app list
os.chdir("/home/ocueye/deskman")
ITEMS = os.listdir("desktop")

print(ITEMS)

@app.route("/")
def index():
    return render_template("index.html", items=ITEMS)

# execute app (it probly secure as long as its keeped on localhost, oh well)
@app.route("/select", methods=["POST"])
def select():
    print()
    data = request.json
    selected = data.get("item")
    if selected:
        print(f"Running: {selected}")
        with open(os.path.join("desktop",selected,"run")) as f:
            print(f"running")
            os.system(f"{f.read()} &")  # Run in background
    return jsonify({"status": "ok", "selected": selected})


# pull icon
@app.route("/image/<name>")
def image(name):
    try:
        files = os.listdir(os.path.join("desktop",name))
        for item in files:
            print(files)
            if item.split(".")[0] == "logo":
                if os.path.isfile(os.path.join("desktop",name,item)):
                    return send_file(os.path.join("desktop",name,item),mimetype='image/png')
                else:
                    return send_file("other/icon.png",mimetype='image/png')
    except:
        print(f"{name} img not found")
        return send_file("other/icon.png",mimetype='image/png')
        
if __name__ == "__main__":
    app.run(debug=False,port=2050,host="127.0.0.1")

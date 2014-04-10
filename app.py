from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

json_data = open('phones.json').read()
data = json.loads(json_data)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/questionaire", methods=["GET","POST"])
def questionaire():
	if request.method == "GET":
		return render_template("questionaire.html")
	else:
		return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
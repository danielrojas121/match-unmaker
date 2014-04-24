from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

json_data = open('phones.json').read()
data = json.loads(json_data)

@app.route("/")
def home():
	return render_template("home.html")

def filter_phones(size, os, megapixels):
	return json_data

@app.route("/questionaire", methods=["GET","POST"])
def questionaire():
	if request.method == "GET":
		return render_template("questionaire.html")
	else:
		size = float(request.form['size_in'])
		os = request.form['OS']
        megapixels = float(request.form['camera_mp'])
		phones = filter_phones(size, os, megapixels)
		return render_template("results.html", phones=phones)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
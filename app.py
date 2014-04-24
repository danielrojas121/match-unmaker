from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

json_data = open('phones.json').read()
data = json.loads(json_data)

@app.route("/")
def home():
	return render_template("home.html")

def filter_phones(os, size, megapixels):
	filt_phones1 = []
	for phone in data:
		if phone["OS"] == os:
			filt_phones1.append(phone)
	filt_phones2 = []
	for phone in filt_phones1:
		if phone["size_in"] == size:
			filt_phones2.append(phone)
	filt_phones3 = []
	for phone in filt_phones3:
		if phone["camera_mp"] == megapixels:
			filt_phones3.append(phone)
	return filt_phones2

@app.route("/questionaire", methods=["GET","POST"])
def questionaire():
	if request.method == "GET":
		return render_template("questionaire.html")
	else:
		size = float(request.form['size_in'])
		os = request.form['OS']
		megapixels = float(request.form['camera_mp'])
		phones = filter_phones(os, size, megapixels)
		return render_template("results.html", phones=phones)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
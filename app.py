from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

json_data = open('phones.json').read()
data = json.loads(json_data)
json_data.close()

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/search", methods=["GET","POST"])
def search():
	if request.method == "POST":
		return render_template("results.html", phone=request.form['user_search'])
	else:
		return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
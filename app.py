from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/search", methods=["GET","POST"])
def search():
	if request.method == "POST":
		return render_template("results.html")
	else:
		return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
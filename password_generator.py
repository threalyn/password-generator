from flask import Flask, redirect, url_for, render_template, request
from passwordgenerator import pwgenerator

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("cover.html", pw=pwgenerator.generate()) 

if __name__ == "__main__":
	app.run(debug=True)
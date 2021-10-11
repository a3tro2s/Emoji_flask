from flask import Flask, render_template, request, flash
from datetime import date, datetime
import random
import time


app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"


@app.route("/")
def index():
	flash("¿Que es lo que mas te gusta de nosotros?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	Em = ["\U0001F923","\U0001F604","\U0001F60A","\U0001F60D","\U0001F970","\U0000F60D","\U0001F929","\U0001F618","\U0001F972",
		  "\U0001F61D","\U0001F911","\U0001F92D","\U0001F914","\U0001F928","\U0001F60F","\U0001F644","\U0001F925","\U0001F924",
		  "\U0001F975","\U0001F974","\U0001F635","\U0001F92F","\U0001F973","\U0001F60E","\U0001F632","\U0001F97A","\U0001F628",
		  "\U0001F631","\U0001F616","\U0001F92C","\U0001F921","\U0001F47B","\U0001F47D","\U0001F916","\U0001F44B","\U0001F44C",
		  "\U0000270C","\U0001F918","\U0001F919","\U0001F44D","\U0001F44F","\U0001F4AA","\U0001F933","\U00002714","\U0000274C"]

	R = random.choice(Em)
	flash(R + str(request.form['name_input']) + ", Siguenos en Intagram: https://is.gd/tRa43G")
	return render_template("index.html")

@app.route("/menu")
def menu():


	return render_template("menu.html")



if __name__ == '__main__':
	app.run(debug=True)

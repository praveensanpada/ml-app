from flask import Flask, render_template, redirect, request

#from sklearn.externals import joblib 
#import joblib

from lrep import ans

app = Flask(__name__)

#model = joblib.load("model.pkl")

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/',methods = ['POST'])
def Salary():
	if request.method == 'POST':
		Experences = float(request.form['Experences'])

		Salary = ans(Experences)

	return render_template("index.html",salary = Salary)


if __name__ == '__main__':
	app.run()




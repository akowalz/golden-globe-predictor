from flask import Flask, render_template
import json
app = Flask(__name__)
app.debug = True
with open('../results/winners2015-percents-3.json', 'r') as f:
	winners = json.loads(f.read())

pageScroll = 10


@app.route('/')
def root():
	return render_template('index.html', pageScroll=0)
@app.route('/sentiment')
def sentiment():
	return render_template('index.html', pageScroll=1)
@app.route('/predictor_winner')
def predictors():
	return render_template('index.html', winners=winners)

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template
import json
app = Flask(__name__)
app.debug = True
with open('testwinners.json', 'r') as f:
	winners = json.loads(f.read())
	

@app.route('/')
def root():
	return render_template('index.html', winners=winners)


if __name__ == '__main__':
    app.run()
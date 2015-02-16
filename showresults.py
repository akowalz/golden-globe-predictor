from flask import Flask, render_template
import json
app = Flask(__name__)
app.debug = True
with open('testwinners.json', 'r') as f:
	winners = json.loads(f.read())
	

@app.route('/')
def root():
	return render_template('index.html', winners=winners)
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)




if __name__ == '__main__':
    app.run()
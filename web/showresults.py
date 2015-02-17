from flask import Flask, render_template
import json
app = Flask(__name__)
app.debug = True
with open('../results/winners2015-percents-3.json', 'r') as f:
	winners15 = json.loads(f.read())
with open('../results/winners2013-percents-3.json', 'r') as f:
    winners13 = json.loads(f.read())
with open('../results/snubs2015-3.json', 'r') as f:
	snubs15 = json.loads(f.read())
with open('../results/snubs2013-3.json', 'r') as f:
	snubs13 = json.loads(f.read())

with open('../results/GGOut2013.json', 'r') as f:
    total13 = json.loads(f.read())
# with open('../results/GGOut2015.json', 'r') as f:
#     total15 = json.loads(f.read())

@app.route('/')
def root():
	return render_template('index.html', pageScroll=0)
@app.route('/sentiment')
def sentiment():
	return render_template('index.html', pageScroll=1)
@app.route('/predictor_winner15')
def predictors15():
	return render_template('index.html', winners=winners15)
@app.route('/predictor_winner13')
def predictors13():
    return render_template('index.html', winners=winners13)

# @app.route('/totals_15')
# def predictors13():
#     return render_template('index.html', totals=total15)
@app.route('/totals_13')
def totals13():
    return render_template('index.html', totals=total13)




@app.route('/snubs2015')
def snubs2015():
    snubs15["Best Animated Feature Film"]["article"] = "http://www.deseretnews.com/article/865619824/2015-Oscar-nominees-Why-The-Lego-Movie-snub-might-not-be-such-a-bad-thing.html?pg=all"
    snubs15["Best Actress In A Motion Picture, Musical or Comedy"]["article"] = "https://ca.movies.yahoo.com/photos/oscars-2015-snubs-and-surprises-1421336072-slideshow/snub-emily-blunt-best-actress-photo-1421335740386.html"
    snubs15["Best TV Movie or Mini-Series"]["article"] = "http://variety.com/2014/tv/news/emmys-the-biggest-snubs-and-surprises-1201290509/"
    snubs15["Best Supporting Actor in a Series, Mini-Series or TV Movie"]["article"] = "http://variety.com/2014/tv/news/emmys-the-biggest-snubs-and-surprises-1201290509/"
    snubs15["Best Original Score - Motion Picture"]["article"] = "http://www.cinemablend.com/new/Interstellar-Got-Robbed-Why-It-Deserved-Way-More-Oscar-Nominations-69184.html"
    return render_template('index.html', snubs=snubs15)

@app.route('/snubs2013')
def snubs2013():
    return render_template('index.html', snubs=snubs13)

if __name__ == '__main__':
    app.run()

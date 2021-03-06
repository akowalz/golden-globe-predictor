# Golden Globes Prediction Tool

Project 1 for EECS 337, will determine the outcome of the Golden Globes based on
tweet data.

## Methodology

To find Winners, we first found the subset of tweets from 2015 that contained the word 'Best'.  This allowed us to use the full dataset (instead of the mini dataset) while vastly improving processing speed and filtering only tweets relevant to us.  We stripped newlines out of these tweets, and put only the content on a line-delimited text file (preprocessed files like this live in the `preprocess` directory).  Having the tweets line by line also makes processing much faster, as it saves the time it takes for pythons json parser to parse the structure.

We set up a dictionary to hold the totals for each award, it takes the form:

```json
{
  "Best Motion Picture, Drama": {
    "Nominees": {
      "Birdman": 13,
      "Boyhood": 40,
      ...
    },
    "total": 123
  },
  ...
}
```

With the relevant subset of tweets at hand, we began detection on the list of tweets.  The first thing we do is look for "words of congratulation" in the tweet (see `winners.py` for this list).  If a tweet is congratulatory, we then search within it for the name of one of the nominees.  If it does contain one of the nominees, we check from out metadata what that nominee was nominated for.  If the nominee was only nominated for one award, we increment their score within our results dict, and the total.  If they were nominated for multiple awards, we pass the tweet text and a list of awards to a funciton that will figure (to the best of it's ability) which award the tweet was talking about, using a weighted formula based on matching keywords in the tweet and the award name.  Once this is determined, we incremement the appropriate score accordingly.

### Results

The results are outputed as JSON files : `GGOut2015.json`, `GGOut2013.json` in the results folder.  
The results were dumped by the `Winner.py` function and shown on on a Flask-based framework.
The web app/gui can be accessed by running `showresults.py`.


## Fun Goals

### Sentiment Map

We used [TextBlob](http://textblob.readthedocs.org/en/dev/) (a simplified iterface into the nltk) to do sentiment processing on the   tweets from 2015.  For each minute of the awards, we have a score from -1.0 to 1.0 indicating the average sentiment of viewers during that minute.  We then plotted sentiment vs. time so we could see trends and spikes as the show progressed.  We also did our best to match up large spikes to various events during the show, such as major awards being announced.

###  Who Got "Snubbed"

We were interested in finding out if we could detect which awards people thought would win, but didn't, or that people were upset did not win.  The methodology we used was fairly similar to the methodology used for finding winners, but looking for "snub words" like "snub", "stiffed", "robbed" in place of congratulatory words.  We then used a similar scoring system to see if we could figure out which nominees were poised to win but did not.  After searching online for media about the topic, we found that we did really well at identifying these awards, with our results being corroborated by popular media.

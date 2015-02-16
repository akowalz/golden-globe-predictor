# Golden Globes Prediction Tool

Project 1 for EECS 337, will determine the outcome of the Golden Globes based on
tweet data.

## Methodology

To find Winners, we first found the subset of tweets from 2015 that contained the word 'Best'.  This allowed us to use the fully dataset while vastly improving processing speed and narrowingly only tweets relevant to us.  We stripped newlines out of these tweets, and put only the content on a line-delimited text file (preprocessed files like this live in the `preprocess` directory).

We set up a dictionary to hold the totals for each award, it takes the form:

```json
{
  "Best Motion Picture, Drama": {
    "Nominees": {
      "Birdman": 13,
      "Boyhood": 40,
      ...
    } 
    "total": 123
  }
  ...
}
```

With the relevant subset of tweets at hand, we began detection in the list of tweets.  The first thing we do is look for "words of congratulation" in the tweet (see winners.py for this list).  If a tweet is congratulatory, we then search within it for the name of one of the nominees.  If it does contain one of the nominees, we check from out metadata what that nominee was nominated for.  If the nominee was only nominated for one award, we increment their score within our results dict, and the total.  If they were nominated for multiple awards, we pass the tweet text and a list of awards to a funciton that will figure (to the best of it's ability) which award the tweet was talking about, using a weighted formula based on matching keywords in the tweet and the award name.  Once this is determined, we incremement the appropriate score accordingly.

## Fun Goals

### Sentiment Map

We used [TextBlob](http://textblob.readthedocs.org/en/dev/) (a simplified iterface into the nltk) to do sentiment processing on the tweets from 2015.  For each minute of the awards, we have a score from -1.0 to 1.0 indicating the average sentiment of watches during that minute.  We then plotted this graph so we could see trends and spikes.  We also did our best to match up large spikes to various events during the show, such as major awards being announced.

###  Who Got "Snubbed"

We were interested in finding out if we could detect which awards got "snubbed" in each category.  The methodology we used was fairly similar to the methodology used for finding winners, but looking for "snub words" like "snub", "stiffed", "robbed" in place of congratulatory words.  We then used a similar scoring system to see if we could figure out which nominees were poised to win but did not, and did so with large success identifying snubs that we confirmed with various popular media articles.
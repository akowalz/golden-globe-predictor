# Golden Globes Prediction Tool

Project 1 for EECS 337, will determine the outcome of the Golden Globes based on
tweet data.

## Strategies

### Winners

#### General strategy

For each award category, first find subset of tweets about that category.  This can be
done using a seed list of award categories and searching through all the tweets that
"match" that award.  Criteria for "match" TBD.

Once these tweets are found, search through the tweets looking for names of
nominess (including aliases + twitter handle).  If possible determine if the tweet was
congratulatory or bitter, use this to weigh score.

Score = `number of tweets about particular a nominee / all tweets about category
with any nominee`

If tweet is determined congratulatory, increase it's weight by N (for example,
pretend it was in the dataset 5 times)

If the tweet is determined bitter, weight it by half or don't include it.

Sentiment processing may also be used to figure out weight of the tweet.

#### Data

*Nominee*
- full name
- twitter handler
- aliases (maybe can generate automatically)
- movie/show nominated for (if person)

*Award Category*
- full name
- keywords
- short name (Best Actress - Motion Picture for Musical or Comedy => Best Actress)
- type (tv or motion picture)

*Congratulatory Words*
- 'congratulations'
- 'congrats'
- 'grats'
- 'good job'
- 'wins'
- 'winner'
- 'won'
- 'win'
- 'awarded'
- ....

*"Snub" Words*
- 'snubbed'
- 'stiffed'
- 'robbed'
- 'shame'
- 'too bad'
- 'unfortunate'
- ...

#### Output format

For each category, the output can be a python dict of the form

```python

best_picture = {
  "Best Motion Picture – Drama": {
    "Boyhood": 0.78,
    "Foxcatcher": .11,
    ...
  }
}

```

Ideally, we would have all the awards with their full names inside of an array.


## Stuff we need

- List of categories and their nominees
- all nominees' twitter handles
- short names or keywords for each category, something to search against
- full list of congratulatory words
- full list of snub words

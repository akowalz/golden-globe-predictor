from textblob import TextBlob
import codecs, json

TIME_WINDOW = 60000 # one minute


def collect_data(in_path, out_path):
    sentiments = []
    outfile = open(out_path, 'w')
    first_time = 1421014813010

    with codecs.open(in_path, 'r', 'utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            text = tweet["text"]
            timestamp = int(tweet["timestamp_ms"])
            sentiment = TextBlob(text).sentiment.polarity
            sentiments.append(sentiment)
            if (timestamp - first_time) > TIME_WINDOW:
                outfile.write("%f,%d\n" % (mean(sentiments), first_time))
                print "%f,%d" % (mean(sentiments), first_time)
                sentiments = []
                timestamps = []
                first_time = timestamp

def mean(ns):
    return sum(ns) / float(len(ns))

# collect_data("data/goldenglobes2015.json", "sentiments.csv")

def find_events(in_path, t):
    with codecs.open(in_path, 'r', 'utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            text = tweet["text"]
            timestamp = int(tweet["timestamp_ms"])
            if timestamp > (t - 60000) and timestamp < (t + 60000):
                print text
            else:
                print (timestamp - t)

find_events("data/goldenglobes2015.json", 1421034899453)

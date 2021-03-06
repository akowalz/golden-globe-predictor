import sys
import json
import string
import tweet
import codecs


def search_tweets(source_path, out_path, searchterm_list, arg):	# arg = 0: Search for tweets containing any search terms.
	count = 0													# arg = 1: Search for tweets containing all search terms.
	with codecs.open(source_path, 'r', 'utf-8') as f:					# Return number of tweets with positive match.
		outfile = codecs.open(out_path, 'w', 'utf-8')
		for line in f:
			add = "True"
			content = line
                        t = tweet.Tweet(content)
			if arg == '0':
                                if t.tweet_contains_word_in(searchterm_list):
                                        count += 1
                                        if count % 10 == 0:
                                            print "Wrote %d tweets" % count
                                        outfile.write(content)
			elif arg == '1':
				for element in searchterm_list:
					if element not in tweet_list:
						add = "False"
                                                break
				if add == "True":
					count += 1
					outfile.write(content)
	return count


def write_tweets(source_path, outpath):
    """
    for use with 2015 data, which has line-delimited json
    Writes tweet text to line on text file
    """
    written = 0
    with codecs.open(source_path, 'r', 'utf-8') as f:
        outfile = codecs.open(outpath, 'w', 'utf-8')
        for obj in f:
            content = json.loads(obj)["text"]
            content = string.replace(content, "\n", " ")
            outfile.write(content)
            outfile.write("\n")
            written += 1
            if written % 1000 == 0:
                print "Wrote %d tweets" % written
        outfile.close()

def write_tweets_json(json_path, outpath):
    """
    For use with 2013 data and mini 2015 data
    Loads whole object into a dictionary, writes only the content (stripped of
    newlines) to a file
    """
    written = 0
    print "Writing to", outpath
    with codecs.open(json_path, 'r', 'utf-8') as f:
        outfile = codecs.open(outpath, 'w', 'utf-8')
        data = json.loads(f.read())
        for tweet in data:
            text = tweet["text"]
            stripped_tweet = string.replace(text, "\n", " ")
            outfile.write(stripped_tweet)
            outfile.write("\n")
            written += 1
            if written % 1000 == 0:
                print "Wrote %d tweets" % written
        outfile.close()
    print "Done, wrote %d tweets to %s" % (written, outpath)


def main():
        # sys.argv[1] = String of search terms separated by spaces.
        # sys.argv[2] = 0 or 1 depending on search preferences.
	search_tweets("tweets.txt", "presenting.txt", ["presenting", "presents"], sys.argv[1])
	return

write_tweets('../data/goldenglobes2015.json', 'gg2015.txt')

import sys
import json
import string
import tweet
import codecs

def write_tweets(source_path, out_path, attr):
    written = 0
    with codecs.open(source_path, 'r', 'utf-8') as json_file:
        outfile = codecs.open(out_path, 'w', 'utf-8')
        for line in json_file:
            content = json.loads(line)[attr]
            content = string.replace(content, "\n", " ")
            outfile.write(content.encode('utf-8') + "\n")
            written += 1
            if written % 1000 == 0:
                print "Wrote %d tweets" % written

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
	
def check_award(tweet, award_list):
	tweet_list = tweet.split()
	best = award_list[0].split()
	best_count = 0
	for element in award_list:
		list_new = [itm for itm in element.split() if itm in tweet_list]
		count = len(list_new)
		if float(count)/float(len(element.split())) > float(best_count)/float(len(best)):
			best = element.split()
	print best
	return

def main():		# sys.argv[1] = String of search terms separated by spaces.
				# sys.argv[2] = 0 or 1 depending on search preferences.
	# write_tweets("../data/goldenglobes2015.json", "tweets.txt", "text")
	search_tweets("tweets.txt", "presenting.txt", ["presenting", "presents"], sys.argv[1])
	with open("presenting.txt", 'r') as f:
		for line in f:
			check_award(line, award_lst)
	return

main()

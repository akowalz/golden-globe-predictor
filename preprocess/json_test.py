import sys
import json
import string

def write_tweets(source_path, out_path, attr):
    written = 0
    with open(source_path, 'r') as json_file:
        outfile = open(out_path, 'w')
        for line in json_file:
            content = json.loads(line)[attr]
            content = string.replace(content, "\n", " ")
            outfile.write(content.encode('utf-8') + "\n".encode('utf-8'))
            written += 1
            if written % 1000 == 0:
                print "Wrote %d tweets" % written

def search_tweets(source_path, out_path, searchterm_s, arg):	# arg = 0: Search for tweets containing any search terms.
	count = 0													# arg = 1: Search for tweets containing all search terms.
	with open(source_path, 'r') as json_file:					# Return number of tweets with positive match.
		outfile = open(out_path, 'w')
		for line in json_file:
			add = "True"
			content = line
			tweet_list = content.split()
			searchterm_list = searchterm_s.split()
			if arg == '0':
				for element in searchterm_list:
					if element in tweet_list:
						count += 1
						outfile.write(content + "\n".encode('utf-8'))
						break
			if arg == '1':
				for element in searchterm_list:
					if element not in tweet_list:
						add = "False"
						break
				if add == "True":
					count += 1
					outfile.write(content + "\n".encode('utf-8'))
	return count

def main():		# sys.argv[1] = String of search terms separated by spaces.
				# sys.argv[2] = 0 or 1 depending on search preferences.
	#write_tweets("goldenglobes2015.json", "tweets.json", "text")
	print search_tweets("tweets.json", "searched_tweets.json", sys.argv[1], sys.argv[2])
	return

main()

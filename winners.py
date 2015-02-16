import codecs, json, re

CONGRATULATORY_WORDS = [
    'congratulations',
    'congrats',
    'grats',
    'good job',
    'wins',
    'winner',
    'won',
    'win',
    'wins',
    'awarded' ]

SNUB_WORDS = [
    'snubbed',
    'stiffed',
    'robbed',
    'shame',
    'unfortunate' ]

def pretty_print_dict(dict):
    print json.dumps(dict, indent=4)

def load_data(json_path):
    with codecs.open(json_path, 'r', 'utf-8') as f:
        return json.loads(f.read())

def nominated_for(awards):
    """
    returns dictionary of nominees mapped to awards they were nominated for
    awards is python dict of raw data
    """
    nominees = {}
    for award, data in awards.iteritems():
        for nom in data["Nominees"]:
            if nom in nominees:
                nominees[nom].append(award)
            nominees[nom] = [award]
    return nominees

def find_best_award(tweet, award_list):
	tweet_list = tweet.split()
	best = award_list[0].split()
	best_count = 0
	for award in award_list:
            list_new = [itm for itm in award.split() if itm in tweet_list]
            count = len(list_new)
            print best
            print award.split()
            if float(count)/float(len(award.split())) > float(best_count)/float(len(best)):
                best = award
                best_count = count

        return best

def all_nominees(awards):
    nominees = []
    for award, data, in awards.iteritems():
        for nom in data["Nominees"]:
            if nom not in nominees:
                nominees.append(nom)
    return nominees

def nominee_aliases(nominees):
    """
    takes a list of nominees (without repeats) and does simple computation for
    their aliases
    Bill Murray => Murray, BillMurray
    """
    aliases = {}
    for nominee in nominees:
        """ FIGURE OUT A BETTER WAY TO FIND ALIASES """
        if len(nominee.split()) == 2:
            names = []
            names.append(nominee)
            nominee_parts = nominee.split()
            names.append(nominee_parts[-1]) # last name
            names.append(''.join(nominee_parts))
            aliases[nominee] = names
        else:
            aliases[nominee] = [nominee]

    return aliases

def initialize_winners(awards):
    """
    initializes hash for each award, each winner to 0, total to 0
    awards is python dict of raw data
    """
    winners = {}
    for award, data in awards.iteritems():
        winners[award] = {}
        winners[award]["Nominees"] = {}
        winners[award]["total"] = 0
        for nom in data["Nominees"]:
            winners[award]["Nominees"][nom] = 0

    return winners


def find_winners(data, tweet_path):
    """
    Returns dict of awards mapped to values for how many tweets indicated each
    nominee won
    data is our raw data, scrapped and hardcoded
    tweet_path is the path to a line-deliminted list of tweets
    """
    nominees = all_nominees(data)
    winners = initialize_winners(data)
    nominations = nominated_for(data)
    aliases = nominee_aliases(nominees)

    tc = 0
    with codecs.open(tweet_path, 'r', 'utf-8') as f:
        for tweet in f:
            tc += 1
            for nom in nominees:
                if tweet_contains_word_in(tweet, [nom]):
                    if len(nominations[nom]) > 1:
                        award_for_nom = find_best_award(tweet, nominations[nom])
                    else:
                        award_for_nom = nominations[nom][0]
                    if is_congratulatory(tweet):
                        weight = 3
                    else:
                        weight = 1
                    winners[award_for_nom]["Nominees"][nom] += weight
                    winners[award_for_nom]["total"] += weight
            if tc % 1000 == 0:
                print "Processed %d tweets for winners" % tc
                print pretty_print_dict(winners)

    return winners

def find_snubs(data, tweet_path):
    """
    data: hardcoded data
    tweet_path: path to line-delimited list of tweets
    """

    nominees = all_nominees(data)
    nominations = nominated_for(data)
    snubs = initialize_winners(data)
    tc = 0
    with codecs.open(tweet_path, 'r', 'utf-8') as f:
        for tweet in f:
            tc += 1
            if tweet_contains_word_in(tweet, SNUB_WORDS):
                for nom in nominees:
                    if tweet_contains_word_in(tweet, [nom]):
                        if len(nominations[nom]) > 1:
                            award = find_best_award(tweet, nominations[nom])
                        else:
                            award = nominations[nom][0]
                        snubs[award]["Nominees"][nom] += 1
                        snubs[award]["total"] += 1
            if (tc % 10000) == 0:
                print "Processed %d tweets for snubs" % tc

        return snubs

def process_winners(winners):
    """
    takes output from find_winners and calculates percentages, confidences
    """
    output = {}
    for award, data in winners.iteritems():
        highest = 0
        output[award] = {}
        output[award]["Nominees"] = {}
        for nom in data["Nominees"]:
            if data["total"] > 0:
                score = data["Nominees"][nom] / float(data["total"])
            else:
                score = 0
            output[award]["Nominees"][nom] = score
            if score > highest:
                highest = score
                output[award]["winner"] = nom

    return output

def tweet_contains_word_in(tweet, words):
    """
    Check for word in the argument list with regexes
    May be more efficient but less accurate (see test cases)
    """
    for word in words:
        matches = re.search(word, tweet, re.I)
        if matches is not None:
            return True
    return False

def is_congratulatory(tweet):
    return tweet_contains_word_in(tweet, CONGRATULATORY_WORDS)

def process_and_write_winners(data_path, tweet_path, outpath, outpath_percents):
    """
    A nice wrapper to help use process and write all the winners
    data_path: path to hardcoded data
    tweet_path: path to line-delimited tweets
    outpath: to write results to
    outpath_percents: path to write results with percentages to
    """
    data = load_data(data_path)
    winners = find_winners(data, tweet_path)

    print "Found winners"
    print "Writing winners to ", outpath
    with codecs.open(outpath, 'w', 'utf-8') as file:
        file.write(json.dumps(winners, indent=4))

    processed_winners = process_winners(winners)
    print "Processed winners"
    print "Writing processed winners to ", outpath_percents
    with codecs.open(outpath_percents, 'w', 'utf-8') as file:
        file.write(json.dumps(processed_winners, indent=4))

    print "All done :)"

def process_and_write_snubs(data_path, tweet_path, outpath):
    """
    Similar to above function
    """

    data = load_data(data_path)

    print "Calculating Snubs from using data from %s and tweets from %s" % (data_path, tweet_path)
    snubs = find_snubs(data, tweet_path)
    with codecs.open(outpath, 'w', 'utf-8') as file:
        print "Writing snubs results to", outpath
        file.write(json.dumps(snubs, indent=4))

    print "All done :)"


"""
Here we Go!
"""

DATA_FILE_2015 = 'hardcode/GG15json.json'
FULL_TWEET_FILE_2015 = 'preprocess/gg2015.txt'
BEST_TWEET_FILE_2015 = 'preprocess/gg2015_best.txt'

DATA_FILE_2013 = 'hardcode/GG13json.json'
FULL_TWEET_FILE_2013 = 'preprocess/gg2013.txt'

TEST_PATH = 'preprocess/tiny_test.txt'


## 2015
process_and_write_winners(DATA_FILE_2015,
                          BEST_TWEET_FILE_2015,
                          'results/winners2015-2.json',
                          'results/winners2015-percents-2.json')

process_and_write_snubs(DATA_FILE_2015,
                        FULL_TWEET_FILE_2015,
                        'results/snubs2015-2.json')

# 2013
process_and_write_winners(DATA_FILE_2013,
                          FULL_TWEET_FILE_2013,
                          'results/winners2013-2.json')

process_and_write_snubs(DATA_FILE_2013,
                        FULL_TWEET_FILE_2013,
                        'results/snubs2013-2.json')

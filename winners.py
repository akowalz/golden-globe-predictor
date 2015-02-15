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
                nominess[nom].append(award)
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
    pretty_print_dict(nominees)
    winners = initialize_winners(data)
    pretty_print_dict(winners)
    nominations = nominated_for(data)
    pretty_print_dict(nominations)
    aliases = nominee_aliases(nominees)
    pretty_print_dict(aliases)

    tc = 0
    with codecs.open(tweet_path, 'r', 'utf-8') as f:
        for tweet in f:
            tc += 1
            for nom in nominees:
                if tweet_contains_word_in(tweet, aliases[nom]):
                    # This is where we need to disambiguate awards!
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
                print "Processed %d tweets" % tc
    return winners

def process_winners(winners):
    """
    takes output from find_winners and calculates percentages, confidences
    """
    output = {}
    for award, data in winners.iteritems():
        output[award] = {}
        for nom in data["Nominees"]:
            output[award][nom] = data["Nominees"][nom] / float(data["total"])
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



data = load_data('ggdump.json')
pretty_print_dict(find_winners(data, 'data/best_tweets_regex.txt'))
# pretty_print_dict(process_winners(json.loads(open("test_output.json","r").read())))

from textblob import TextBlob
import re

class Tweet(object):

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

    def __init__(self, text):
        self.text = text

        # used for caching
        self.textblob = None
        self.token_words = None

    def blob(self):
        """ Returns TextBlob representation of tweet text, cached if available """
        if self.textblob is None:
            self.textblob = TextBlob(self.text)
            return self.textblob
        else:
            return self.textblob

    def tokens(self):
        """ Returns list of tokens for the object, all lowercased """
        if self.token_words is None:
            self.token_words = map(lambda(s): s.lower(), self.blob().words)
            return self.token_words
        else:
            return self.token_words

    def is_congratulatory(self):
        return self.tweet_contains_token_in(self.CONGRATULATORY_WORDS)

    def is_snub(self):
        return self.tweet_contains_token_in(self.SNUB_WORDS)

    def mentions(self):
        """
        Returns all @ mentions in a tweet
        """
        return re.findall(r'@\w{1,15}', self.text)

    def tweet_contains_word_in(self, words):
        """
        Check for word in the argument list with regexes
        May be more efficient but less accurate (see test cases)
        """
        return any(map(lambda(word): re.search(word, self.text, re.I) is not None,
                                     words))

    def tweet_contains_token_in(self, words):
        """
        Check for word in the argument list with tokenization
        May be more accurate but less efficient
        """
        return any(map(lambda(word): word in self.tokens(),
                                     words))

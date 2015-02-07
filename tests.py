import unittest
import tweet
import nominee
from textblob import TextBlob

class TweetTest(unittest.TestCase):

    def setUp(self):
        self.tweet = tweet.Tweet("foobar")

    def test_initialization(self):
        self.assertEqual(self.tweet.text, "foobar")

    def test_caches_textblob(self):
        self.tweet.blob()
        self.assertIsInstance(self.tweet.textblob, TextBlob)

    def test_tokens(self):
        t = tweet.Tweet("COOL a new! WaY! to #GOTOSCHOOl")
        self.assertEqual(t.tokens(), ['cool', 'a', 'new', 'way', 'to', 'gotoschool'])

    def test_congratulatory(self):
        grats_tweets = [
                tweet.Tweet("congratulations to kevin spacey!"),
                tweet.Tweet("Congrats! you rock"),
                tweet.Tweet("kevin WINS!")
                ]
        not_grats_tweets = [
                tweet.Tweet("boo to kevin spacey!"),
                tweet.Tweet("kevin spacey got robbed!"),
                tweet.Tweet("wonderful that kevin lost!")
                ]

        for t in grats_tweets:
            self.assertTrue(t.is_congratulatory())
        for t in not_grats_tweets:
            self.assertFalse(t.is_congratulatory())

    def test_is_snub(self):
        grats_tweets = [
                tweet.Tweet("kevin spacey got snubbed!"),
                tweet.Tweet("boyhood got robbed!"),
                tweet.Tweet("it's a shame boyhood lost")
                ]
        not_grats_tweets = [
                tweet.Tweet("congrats to kevin spacey!")
                ]

        for t in grats_tweets:
            self.assertTrue(t.is_snub())
        for t in not_grats_tweets:
            self.assertFalse(t.is_snub())

    def test_mentions(self):
        self.assertListEqual(tweet.Tweet("@danaKStew @50ShadesWorldcm @ScarletteDrake Also Red Carpet um 12").mentions(),
                    ['@danaKStew','@50ShadesWorldcm', '@ScarletteDrake'])
        self.assertListEqual(tweet.Tweet("going to bed @ 2 o'clock").mentions(), [])

class NomineeTest(unittest.TestCase):

    def test_initialization(self):
        nat = nominee.Nominee("Natalie Portman", "@natalie")
        self.assertEqual(nat.name, "Natalie Portman")
        self.assertEqual(nat.handle, "@natalie")
        self.assertEqual(nat.fname, "Natalie")
        self.assertEqual(nat.lname, "Portman")
        self.assertListEqual(nat.known_aliases, [])

    def test_all_aliases(self):
        nat = nominee.Nominee("Natalie Portman", "@natalie", ["npo"])
        self.assertListEqual(nat.all_aliases(), [
            "Natalie Portman",
            "Natalie",
            "Portman",
            "@natalie",
            "natalieportman",
            "nportman",
            "npo"
            ])



unittest.main()

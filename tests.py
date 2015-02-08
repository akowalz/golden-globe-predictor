import unittest
import tweet
import nominee
import award
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

    def test_person_initialization(self):
        nat = nominee.NomineePerson("Natalie Portman")
        self.assertEqual(nat.name, "Natalie Portman")
        self.assertEqual(nat.fname, "Natalie")
        self.assertEqual(nat.lname, "Portman")
        self.assertListEqual(nat.known_aliases, [])

    def test_person_all_aliases(self):
        nat = nominee.NomineePerson("Natalie Portman", ["@natalie", "npo"])
        self.assertListEqual(nat.all_aliases(), [
            "Natalie Portman",
            "Natalie",
            "Portman",
            "natalieportman",
            "nportman",
            "@natalie",
            "npo"
            ])


class Awardtest(unittest.TestCase):

    def test_motion_pitcure_awards(self):
        motion_picture_awards = [
            "Best Motion Picture - Drama",
            "Best Motion Picture - Musical or Comedy",
            "Best Director",
            "Best Actor - Motion Picture Drama",
            "Best Actor - Motion Picture Musical or Comedy",
            "Best Actress - Motion Picture Drama",
            "Best Actress - Motion Picture Musical or Comedy",
            "Best Supporting Actor - Motion Picture",
            "Best Supporting Actress - Motion Picture",
            "Best Screenplay",
            "Best Original Score",
            "Best Original Song",
            "Best Foreign Language Film",
            "Best Animated Feature Film",
            "Cecil B. DeMille Award for Lifetime Achievement in Motion Pictures"
        ]

        for awrd in motion_picture_awards:
            self.assertTrue(award.Award(awrd).for_motion_picture())
            self.assertFalse(award.Award(awrd).for_television())

    def test_television_awards(self):
        television_awards = [
            "Best Drama Series",
            "Best Comedy Series",
            "Best Actor in a Television Drama Series",
            "Best Actor in a Television Comedy Series",
            "Best Actress in a Television Drama Series",
            "Best Actress in a Television Comedy Series",
            "Best Limited Series or Motion Picture made for Television",
            "Best Actor in a Limited Series or Motion Picture made for Television",
            "Best Actress in a Limited Series or Motion Picture made for Television",
            "Best Supporting Actor in a Series, Limited Series or Motion Picture made for Television",
            "Best Supporting Actress in a Series, Limited Series or Motion Picture made for Television"
        ]

        for tv_award in television_awards:
            self.assertTrue(award.Award(tv_award).for_television())
            self.assertFalse(award.Award(tv_award).for_motion_picture())

    def test_acting_award(self):
        acting_awards = [
            "Best Actor in a Television Drama Series",
            "Best Actor in a Television Comedy Series",
            "Best Actress in a Television Drama Series",
            "Best Actress in a Television Comedy Series",
            "Best Actor in a Limited Series or Motion Picture made for Television",
            "Best Actress in a Limited Series or Motion Picture made for Television",
            "Best Supporting Actor in a Series, Limited Series or Motion Picture made for Television",
            "Best Supporting Actress in a Series, Limited Series or Motion Picture made for Television"
            "Best Actor - Motion Picture Drama",
            "Best Actor - Motion Picture Musical or Comedy",
            "Best Actress - Motion Picture Drama",
            "Best Actress - Motion Picture Musical or Comedy",
            "Best Supporting Actor - Motion Picture",
            "Best Supporting Actress - Motion Picture"
        ]

        for acting_award in acting_awards:
            self.assertTrue(award.Award(acting_award).for_acting())

unittest.main()

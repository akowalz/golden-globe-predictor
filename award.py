import re

class Award(object):

    MOTION_PICTURE_WORDS = [
        # this list currently unused
        "Motion",
        "Picture",
        "Film",
        "Score",
        "Song",
        "Screenplay",
        "Director"
    ]

    TELEVISION_WORDS = [
        "Series",
        "Television"
    ]

    ACTING_WORDS = [
        "Actor",
        "Actress"
    ]

    PERSON_WORDS = [
        "Actor",
        "Actree",
        "Director"
    ]

    def __init__(self, name, aliases=[], nominees=[]):
        self.name = name
        self.short_names = short_names

        # nominees should all be NOMINEE OBJECTS!
        self.nominees = nominees

    def for_motion_picture(self):
        return not self.contains_word_in(self.TELEVISION_WORDS)

    def for_television(self):
        return self.contains_word_in(self.TELEVISION_WORDS)

    def for_acting(self):
        return self.contains_word_in(self.ACTING_WORDS)

    def contains_word_in(self, words):
        for word in words:
            if re.search(word, self.name, re.I) is not None:
                return True
        return False

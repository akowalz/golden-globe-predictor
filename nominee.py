class Nominee(object):
    def __init__(self, name, handle, known_aliases=[]):
        self.name = name
        self.handle = handle
        self.fname = name.split(' ')[0]
        self.lname = name.split(' ')[1]
        self.known_aliases = known_aliases

    def all_aliases(self):
        return [
            self.name,
            self.fname,
            self.lname,
            self.handle,
            (self.fname + self.lname).lower(),
            (self.fname[0] + self.lname).lower()
                ] + (self.known_aliases)


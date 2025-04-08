from genverb import GenVerb
from db import Database

def readApiKey():
    try:
        with open(".apikey", mode="r") as f:
            return f.readline()
    except IOError as e:
        return None
    
class FrontEnd:
    def __init__(self, backend):
        self.backend = backend
    
    def addVerb(self, verb):
        self.backend.addVerb(verb)

    def addVerbFromFile(self, list_file):
        pass

class BackEnd:
    def __init__(self, apikey):
        self.apikey = apikey
        self.db = Database()

    def init(self):
        with self.db.connect():
            self.db.runSqlFile("schema.sql")

    def is_reflexive(self, verb):
        return verb.endswith("arsi") or verb.endswith("ersi") or verb.endswith("irsi")

    def regular_form(self, verb):
        if self.is_reflexive(verb):
            return verb[:-3] + "re"
        return verb

    def addVerb(self, verb):
        is_reflexive = self.is_reflexive(verb)
        regular_form = self.regular_form(verb)

        self.db.connect()
        if is_reflexive and not self.db.hasVerb(regular_form):
            self.db.close()
            self.addVerb(regular_form)
        
        print("addVerb: ", verb)

        if is_reflexive:
            with self.db.connect():
                self.db.addReflexiveVerb(verb, regular_form)
        else:
            itaverb = GenVerb(self.apikey).gen_verb_data(regular_form)
            with self.db.connect():
                self.db.addVerb(itaverb)

def main():
    apikey=readApiKey()
    if (apikey == None):
        print(".apikey not found")
        exit()

    backend = BackEnd(apikey)
    backend.init()

    frontend = FrontEnd(backend)

    verb = "svegliarsi"
    frontend.addVerb(verb)

if __name__ == "__main__":
    main()
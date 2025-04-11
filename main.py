from genai import GenAi
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

    def addVerbFromFile(self, list_file, count):
        try:
            with open(list_file, mode="r") as f:
                i = 0
                for line in f:
                    self.addVerb(line.strip())
                    i += 1
                    if count > 0 and i >= count:
                        break
        except IOError as e:
            print(e)

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

        if is_reflexive and self.db.hasReflexiveVerb(verb):
            print("Skip: ", verb)

        self.db.connect()
        if is_reflexive and not self.db.hasVerb(regular_form):
            self.db.close()
            self.addVerb(regular_form)

        if is_reflexive:
            with self.db.connect():
                print("addVerb: ", verb)
                self.db.addReflexiveVerb(verb, regular_form)
        else:
            if not self.db.hasVerb(verb):
                print("addVerb: ", verb)
                itaverb = GenAi(self.apikey).gen_verb_data(regular_form)
                with self.db.connect():
                    self.db.addVerb(itaverb)
            else:
                print("Skip: ", verb)

def main():
    apikey=readApiKey()
    if (apikey == None):
        print(".apikey not found")
        exit()

    # backend = BackEnd(apikey)
    # backend.init()

    # frontend = FrontEnd(backend)
    # frontend.addVerbFromFile("verb_list/ita/top20.txt", 5)
    # frontend.addVerbFromFile("verb_list/ita/top10_ref.txt", 5)

    genAi = GenAi(apikey).gen_sentences("chiedere", "Congiuntivo Presente", "3st singular", 3)
    print(genAi)

if __name__ == "__main__":
    main()
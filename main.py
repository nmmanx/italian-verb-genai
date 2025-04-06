from genverb import GenVerb
from db import Database

def main():
    try:
        apikey=""
        with open(".apikey", mode="r") as f:
            apikey = f.readline()

        res = GenVerb(apikey).gen_verb_data("chiedere")
        db = Database()

        db.connect()
        db.runSqlFile("schema.sql")
        print(res.parsed)
        db.addVerb(res.parsed)
        db.close()

    except IOError as e:
        print(".apikey not found")
        exit()

if __name__ == "__main__":
    main()
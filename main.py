from genverb import GenVerb

def main():
    try:
        apikey=""
        with open(".apikey", mode="r") as f:
            apikey = f.readline()

        # test
        res = GenVerb(apikey).gen_verb_data("cavalcare")
        print(res.parsed)

    except IOError as e:
        print(".apikey not found")
        exit()

if __name__ == "__main__":
    main()
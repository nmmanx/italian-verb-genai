from google import genai
from google.genai import types
from pydantic import BaseModel

MODEL = "gemini-2.0-flash"

PROMPT_GEN_VERB="""Generate verb conjugations for the italian verb \"{}\" with the following requirements:
- Only giving the conjugated verb, no need pronouns.
- The conjugation list must have 6 elements and be ordered: 1st-person singular, 2nd-person singular, 3rd-person singular, 1st-person plural, 2nd-person plural, 3rd-person plural.
- For imperativo, list all conjugations except 1st-person (leave it bank).
"""

PROMPT_GEN_EXAMPLE="""Generate {} Italian sentences using the verb \"{}\" conjugated for {} pronoun in the tense \"{}\". Following:
- The sentenses are medium-length and easy to understand.
- The sentences contain contextual information (time, place, etc) to determine the verb tense.
- Highlight the conjugated verbs by putting them within [ ].
"""

PRONOUNS = [ "1st singular", "2nd singular", "3rd singular", "1st plural", "2nd plural", "3rd plural" ]

class Conjugation(BaseModel):
    infinito_presente: str
    gerundio_presente: str
    participio_presente: str
    participio_passato: str
    indicativo_presente: list[str]
    indicativo_imperfetto: list[str]
    indicativo_passato_prossimo: list[str]
    indicativo_passato_remoto: list[str]
    indicativo_trapassato_prossimo: list[str]
    indicativo_trapassato_remoto: list[str]
    indicativo_futuro_semplice: list[str]
    indicativo_futuro_anteriore: list[str]
    congiuntivo_presente: list[str]
    congiuntivo_passato: list[str]
    congiuntivo_imperfetto: list[str]
    congiuntivo_trapassato: list[str]
    condizionale_presente: list[str]
    condizionale_passato: list[str]
    imperativo_presente: list[str]

class ItaVerb(BaseModel):
    name: str
    english: str
    auxiliary_verb: str
    has_irregular_conjugations: bool
    conjugations: Conjugation

config_gen_verb = types.GenerateContentConfig(
    system_instruction="Your are a native Italian language teacher",
    response_mime_type="application/json",
    response_schema=ItaVerb)

config_gen_example = types.GenerateContentConfig(
    system_instruction="Your are a native Italian language teacher",
    response_mime_type="application/json",
    response_schema=list[str])

class GenAi:
    def __init__(self, apikey):
        self.client = genai.Client(api_key=apikey)

    def gen_verb_data(self, verb) -> ItaVerb:
        genVerb = self.client.models.generate_content(model=MODEL,
            config=config_gen_verb,
            contents=PROMPT_GEN_VERB.format(verb))
        
        return genVerb.parsed
    
    def gen_sentences(self, verb, tense, pronoun, count) -> list[str]:
        genExample = self.client.models.generate_content(model=MODEL,
            config=config_gen_example,
            contents=PROMPT_GEN_EXAMPLE.format(str(count), verb, tense, pronoun))
        
        return genExample.parsed

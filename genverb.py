from google import genai
from google.genai import types
from pydantic import BaseModel

MODEL = "gemini-2.0-flash"
PROMPT="""Generate verb conjugations for the italian verb \"{}\" with the following requirements:
- Only giving the conjugated verb, no need pronouns.
- The conjugation list must have 6 elements and be ordered: 1st-person singular (leave empty for imperativo), 2nd-person singular, 3rd-person singular, 1st-person plural, 2nd-person plural, 3rd-person plural.
- Prefix @ to all irregular conjugations, including irregular participio(s).
- Don't miss any conjugation, especially the imperativo.
"""

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
    is_reflexive: bool
    conjugations: Conjugation

config = types.GenerateContentConfig(
    system_instruction="Your are a native Italian language teacher",
    response_mime_type="application/json",
    response_schema=ItaVerb)

class GenVerb:
    def __init__(self, apikey):
        self.client = genai.Client(api_key=apikey)

    def gen_verb_data(self, verb):
        return self.client.models.generate_content(model=MODEL,
            config=config,
            contents=PROMPT.format(verb))

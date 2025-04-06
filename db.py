import sqlite3
from genverb import ItaVerb

DB_NAME = "itaverb.db"

COLUMNS_TABLE_VERB = [
    'verb',
    'eng',
    'aux_verb',
    'is_irregular',
    'is_reflexive',
    'inf_pre',
    'ger_pre',
    'par_pre',
    'par_pas',
    'ind_pre',
    'ind_imp',
    'ind_pas_pro',
    'ind_pas_rem',
    'ind_tra_pro',
    'ind_tra_rem',
    'ind_fut_sem',
    'ind_fut_ant',
    'cong_pre',
    'cong_pas',
    'cong_imp',
    'cong_tra',
    'cond_pre',
    'cond_pas',
    'imp_pre'
]

class Database:
    # def __init__(self):
    #     self.conn = sqlite3.connect(DB_NAME)

    def connect(self):
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn

    def close(self):
        self.conn.close()

    def runSqlFile(self, file):
        cursor = self.conn.cursor()
        try:
            with open(file, mode="r") as f:
                sql = f.read()
                cursor.execute(sql)
                self.conn.commit()
        except IOError:
            pass

    def addVerb(self, verb: ItaVerb):
        columns_str = ",".join(COLUMNS_TABLE_VERB)
        placeholders = ",".join(["?"] * len(COLUMNS_TABLE_VERB))
        query = f"INSERT INTO verbs ({columns_str}) VALUES ({placeholders})"

        values = []
        for c in COLUMNS_TABLE_VERB:
            if c == "verb":
                values.append(verb.name)
            elif c == "eng":
                values.append(verb.english)
            elif c == "aux_verb":
                values.append(verb.auxiliary_verb)
            elif c == "is_irregular":
                values.append(str(verb.has_irregular_conjugations))
            elif c == "is_reflexive":
                values.append(str(verb.is_reflexive))
            elif c == "inf_pre":
                values.append(verb.conjugations.infinito_presente)
            elif c == "ger_pre":
                values.append(verb.conjugations.gerundio_presente)
            elif c == "par_pre":
                values.append(verb.conjugations.participio_presente)
            elif c == "par_pas":
                values.append(verb.conjugations.participio_passato)
            elif c == "ind_pre":
                values.append(",".join(verb.conjugations.indicativo_presente))
            elif c == "ind_imp":
                values.append(",".join(verb.conjugations.indicativo_imperfetto))
            elif c == "ind_pas_pro":
                values.append(",".join(verb.conjugations.indicativo_passato_prossimo))
            elif c == "ind_pas_rem":
                values.append(",".join(verb.conjugations.indicativo_passato_remoto))
            elif c == "ind_tra_pro":
                values.append(",".join(verb.conjugations.indicativo_trapassato_prossimo))
            elif c == "ind_tra_rem":
                values.append(",".join(verb.conjugations.indicativo_trapassato_remoto))
            elif c == "ind_fut_sem":
                values.append(",".join(verb.conjugations.indicativo_futuro_semplice))
            elif c == "ind_fut_ant":
                values.append(",".join(verb.conjugations.indicativo_futuro_anteriore))
            elif c == "cong_pre":
                values.append(",".join(verb.conjugations.congiuntivo_presente))
            elif c == "cong_pas":
                values.append(",".join(verb.conjugations.congiuntivo_passato))
            elif c == "cong_imp":
                values.append(",".join(verb.conjugations.congiuntivo_imperfetto))
            elif c == "cong_tra":
                values.append(",".join(verb.conjugations.congiuntivo_trapassato))
            elif c == "cond_pre":
                values.append(",".join(verb.conjugations.condizionale_presente))
            elif c == "cond_pas":
                values.append(",".join(verb.conjugations.condizionale_passato))
            elif c == "imp_pre":
                values.append(",".join(verb.conjugations.imperativo_presente))

        cursor = self.conn.cursor()
        cursor.execute(query, tuple(values))
        self.conn.commit()

CREATE TABLE IF NOT EXISTS verb (
    inf_pre VARCHAR(50) PRIMARY KEY,
    eng VARCHAR(150),
    aux_verb VARCHAR(20),
    is_irregular BOOLEAN,

    -- Gerundio
    ger_pre VARCHAR(50),

    -- Participiio
    par_pre VARCHAR(50),
    par_pas VARCHAR(50),

    -- Indicativo
    ind_pre VARCHAR(255),
    ind_imp VARCHAR(255),
    ind_pas_pro VARCHAR(255),
    ind_pas_rem VARCHAR(255),
    ind_tra_pro VARCHAR(255),
    ind_tra_rem VARCHAR(255),
    ind_fut_sem VARCHAR(255),
    ind_fut_ant VARCHAR(255),

    -- Congiuntivo
    cong_pre VARCHAR(255),
    cong_pas VARCHAR(255),
    cong_imp VARCHAR(255),
    cong_tra VARCHAR(255),

    -- Condizionale
    cond_pre VARCHAR(255),
    cond_pas VARCHAR(255),

    -- Imperativo
    imp_pre VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS reflexive_verb (
    inf_pre VARCHAR(50) PRIMARY KEY,
    regular_form VARCHAR(50),
    FOREIGN KEY (regular_form) REFERENCES verbs(inf_pre)
);

CREATE TABLE IF NOT EXISTS verb_list (
    list_id VARCHAR(50) PRIMARY KEY,
    list_name VARCHAR(255),
    list_desc VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS verb_list_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id VARCHAR(50),
    verb VARCHAR(50),
    reflexive_verb VARCHAR(50),
    FOREIGN KEY (list_id) REFERENCES verb_list(id),
    FOREIGN KEY (verb) REFERENCES verb(inf_pre),
    FOREIGN KEY (reflexive_verb) REFERENCES reflexive_verb(inf_pre)
);

INSERT OR IGNORE INTO verb_list (list_id, list_name, list_desc)
VALUES ('reflexive', 'Reflexive verbs', 'Collection of reflexive verbs');

CREATE TRIGGER IF NOT EXISTS add_reflexive_verb AFTER INSERT ON reflexive_verb
FOR EACH ROW
BEGIN
    INSERT INTO verb_list_item (list_id, verb, reflexive_verb)
    VALUES ('reflexive', NULL, NEW.inf_pre);
END;

CREATE TRIGGER IF NOT EXISTS remove_reflexive_verb BEFORE DELETE ON reflexive_verb
FOR EACH ROW
BEGIN
    DELETE FROM verb_list_item WHERE reflexive_verb = OLD.inf_pre;
END;

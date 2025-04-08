CREATE TABLE IF NOT EXISTS verbs (
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

CREATE TABLE IF NOT EXISTS reflexive_verbs (
    inf_pre VARCHAR(50) PRIMARY KEY,
    regular_form VARCHAR(50),
    FOREIGN KEY (regular_form) REFERENCES verbs(inf_pre)
);

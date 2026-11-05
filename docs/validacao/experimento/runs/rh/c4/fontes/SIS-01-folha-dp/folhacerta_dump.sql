--
-- PostgreSQL database dump
-- Sistema: FolhaCerta (Folha/DP) - Drogarias Caliandra S.A.
-- Dumped from database version 15.6
-- Data do dump: 2026-10-20 02:00 (rotina noturna)
-- Amostra de dados: filiais 147, 205, 288 e 312
--

SET client_encoding = 'UTF8';
CREATE SCHEMA folha;
SET search_path = folha;

CREATE ROLE dp_analista NOLOGIN;
CREATE ROLE rh_loja NOLOGIN;
COMMENT ON ROLE rh_loja IS 'Perfil do portal do gestor: gerentes de loja e assistentes administrativos';

CREATE TABLE filial (
    cod_filial  INTEGER PRIMARY KEY,
    nome        VARCHAR(60) NOT NULL,
    cidade      VARCHAR(60) NOT NULL,
    uf          CHAR(2) NOT NULL,
    cnpj        CHAR(14) NOT NULL
);

CREATE TABLE cargo (
    cargo_cod       VARCHAR(10) PRIMARY KEY,
    descricao       VARCHAR(60) NOT NULL,
    jornada_mensal  SMALLINT NOT NULL DEFAULT 220,
    exige_crf       BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE cargo_piso (
    cargo_cod    VARCHAR(10) REFERENCES cargo,
    uf           CHAR(2) NOT NULL,
    piso         NUMERIC(10,2) NOT NULL,
    vigencia     DATE NOT NULL,
    origem       VARCHAR(40),
    PRIMARY KEY (cargo_cod, uf, vigencia)
);

CREATE TABLE beneficio_regra (
    cargo_cod            VARCHAR(10) PRIMARY KEY REFERENCES cargo,
    plano_carencia_dias  SMALLINT NOT NULL
);

CREATE TABLE colaborador (
    matricula        SERIAL PRIMARY KEY,
    cpf              CHAR(11) NOT NULL UNIQUE,
    nome             VARCHAR(120) NOT NULL,
    data_nascimento  DATE NOT NULL,
    rg               VARCHAR(20),
    nome_mae         VARCHAR(120),
    email_pessoal    VARCHAR(120)
);

CREATE TABLE contrato (
    id                SERIAL PRIMARY KEY,
    matricula         INTEGER NOT NULL REFERENCES colaborador,
    cod_filial        INTEGER NOT NULL REFERENCES filial,
    cargo_cod         VARCHAR(10) NOT NULL REFERENCES cargo,
    tipo_contrato     VARCHAR(10) NOT NULL
                      CONSTRAINT chk_tipo_contrato CHECK (tipo_contrato IN ('CLT_EXP','CLT_IND','ESTAGIO')),
    data_admissao     DATE NOT NULL,
    dias_experiencia  SMALLINT DEFAULT 45,
    fim_experiencia   DATE,
    salario           NUMERIC(10,2) NOT NULL,
    crf_numero        VARCHAR(20),
    status            VARCHAR(10) NOT NULL DEFAULT 'PRE'
                      CONSTRAINT chk_status CHECK (status IN ('PRE','ATIVO','DESLIGADO'))
);
COMMENT ON COLUMN contrato.status IS 'PRE: em preparação no DP. ATIVO: admissão efetivada pelo DP com contrato assinado e ASO validado; gera eventos eSocial.';

CREATE TABLE exame_admissional (
    id                  SERIAL PRIMARY KEY,
    matricula           INTEGER NOT NULL REFERENCES colaborador,
    dt_emissao          DATE NOT NULL,
    resultado           VARCHAR(10) NOT NULL CHECK (resultado IN ('APTO','INAPTO')),
    medico_crm          VARCHAR(20),
    cid_restricao       VARCHAR(8),
    observacao_clinica  TEXT
);

CREATE TABLE esocial_prazo (
    evento     VARCHAR(10) PRIMARY KEY,
    regra      VARCHAR(30) NOT NULL,
    descricao  VARCHAR(120)
);

CREATE TABLE evento_esocial (
    id         SERIAL PRIMARY KEY,
    matricula  INTEGER NOT NULL REFERENCES colaborador,
    evento     VARCHAR(10) NOT NULL REFERENCES esocial_prazo,
    dt_limite  DATE NOT NULL,
    dt_envio   DATE,
    recibo     VARCHAR(30)
);

-- Validação de contrato
CREATE FUNCTION fn_valida_contrato() RETURNS trigger AS $$
DECLARE
    v_nasc DATE;
    v_uf   CHAR(2);
    v_piso NUMERIC(10,2);
BEGIN
    SELECT data_nascimento INTO v_nasc FROM colaborador WHERE matricula = NEW.matricula;
    IF NEW.data_admissao < v_nasc + INTERVAL '18 years' THEN
        RAISE EXCEPTION 'Colaborador deve ter ao menos 18 anos na admissao';
    END IF;

    SELECT uf INTO v_uf FROM filial WHERE cod_filial = NEW.cod_filial;
    SELECT piso INTO v_piso FROM cargo_piso
     WHERE cargo_cod = NEW.cargo_cod AND uf = v_uf AND vigencia <= NEW.data_admissao
     ORDER BY vigencia DESC LIMIT 1;
    IF NEW.salario < v_piso THEN
        RAISE EXCEPTION 'Salario % abaixo do piso % (%/%)', NEW.salario, v_piso, NEW.cargo_cod, v_uf;
    END IF;

    IF NEW.cargo_cod = 'FARM' AND NEW.crf_numero IS NULL THEN
        RAISE EXCEPTION 'Numero do CRF obrigatorio para farmaceutico';
    END IF;

    IF NEW.tipo_contrato = 'CLT_EXP' AND NEW.fim_experiencia IS NULL THEN
        NEW.fim_experiencia := NEW.data_admissao + COALESCE(NEW.dias_experiencia, 45);
    END IF;

    IF NEW.status = 'ATIVO' AND NOT EXISTS (
        SELECT 1 FROM exame_admissional e
         WHERE e.matricula = NEW.matricula
           AND e.resultado = 'APTO'
           AND e.dt_emissao >= NEW.data_admissao - 90
    ) THEN
        RAISE EXCEPTION 'ASO apto nao encontrado para ativacao do contrato';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_valida_contrato
    BEFORE INSERT OR UPDATE ON contrato
    FOR EACH ROW EXECUTE FUNCTION fn_valida_contrato();

-- Geração dos eventos de admissão
CREATE FUNCTION fn_gera_esocial() RETURNS trigger AS $$
BEGIN
    IF NEW.status = 'ATIVO' AND (TG_OP = 'INSERT' OR OLD.status <> 'ATIVO') THEN
        INSERT INTO evento_esocial (matricula, evento, dt_limite)
        VALUES (NEW.matricula, 'S-2190', NEW.data_admissao - 1),
               (NEW.matricula, 'S-2200',
                (date_trunc('month', NEW.data_admissao) + INTERVAL '1 month' + INTERVAL '14 days')::date);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_gera_esocial
    AFTER INSERT OR UPDATE OF status ON contrato
    FOR EACH ROW EXECUTE FUNCTION fn_gera_esocial();

GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA folha TO dp_analista;
GRANT SELECT ON colaborador, contrato, exame_admissional, filial, cargo TO rh_loja;

--
-- Data
--
ALTER TABLE contrato DISABLE TRIGGER ALL;

COPY filial (cod_filial, nome, cidade, uf, cnpj) FROM stdin;
147	Savassi	Belo Horizonte	MG	00000000014700
205	Eldorado	Contagem	MG	00000000020500
288	Cambuí	Campinas	SP	00000000028800
312	Pinheiros	São Paulo	SP	00000000031200
\.

COPY cargo (cargo_cod, descricao, jornada_mensal, exige_crf) FROM stdin;
BALC	Balconista de farmácia	220	f
CAIXA	Operador de caixa	220	f
FARM	Farmacêutico	220	t
FARM_RT	Farmacêutico responsável técnico	220	t
\.

COPY cargo_piso (cargo_cod, uf, piso, vigencia, origem) FROM stdin;
BALC	MG	1690.00	2026-02-01	CCT MG 2026
BALC	SP	1820.00	2026-03-01	CCT SP 2026
CAIXA	MG	1690.00	2026-02-01	CCT MG 2026
CAIXA	SP	1820.00	2026-03-01	CCT SP 2026
FARM	MG	5600.00	2026-02-01	CCT Farmacêuticos MG 2026
FARM	SP	6100.00	2026-03-01	CCT Farmacêuticos SP 2026
FARM_RT	MG	5600.00	2026-02-01	CCT Farmacêuticos MG 2026
FARM_RT	SP	6100.00	2026-03-01	CCT Farmacêuticos SP 2026
\.

COPY beneficio_regra (cargo_cod, plano_carencia_dias) FROM stdin;
BALC	90
CAIXA	90
FARM	30
FARM_RT	30
\.

COPY esocial_prazo (evento, regra, descricao) FROM stdin;
S-2190	VESPERA_INICIO	Registro preliminar de trabalhador
S-2200	DIA_15_MES_SEGUINTE	Cadastramento inicial do vínculo e admissão
\.

COPY colaborador (matricula, cpf, nome, data_nascimento, rg, nome_mae, email_pessoal) FROM stdin;
50211	00000000202	Carlos Eduardo Lima	1985-03-11	MG-00.000.202	Teresa Lima	carlos.lima85.fic@exemplo.com
58801	00000000303	Carlos Eduardo Lima	1999-07-22	SP-00.000.303	Rosângela Lima	carloseduardo.lima.fic@exemplo.com
58902	00000000505	Renato Alves Pires	1990-05-30	MG-00.000.505	Lúcia Alves	renato.pires.fic@exemplo.com
58933	00000000101	Ana Beatriz Moura	1998-11-02	MG-00.000.101	Sônia Moura	ana.moura.fic@exemplo.com
58940	00000000011	Bruno Cardoso Neves	2001-01-19	MG-00.000.011	Márcia Cardoso	bruno.neves.fic@exemplo.com
58977	00000000404	Juliana Prado Nogueira	1993-08-14	SP-00.000.404	Elisa Prado	juliana.prado.fic@exemplo.com
58978	00000000606	Thiago Mendes Rocha	2002-04-09	SP-00.000.606	Vera Mendes	thiago.rocha.fic@exemplo.com
58985	00000000707	Larissa Campos Freitas	1996-12-21	MG-00.000.707	Cida Campos	larissa.freitas.fic@exemplo.com
58991	00000001212	Fernanda Dias Couto	1994-06-03	SP-00.001.212	Neide Dias	fernanda.couto.fic@exemplo.com
\.

COPY contrato (id, matricula, cod_filial, cargo_cod, tipo_contrato, data_admissao, dias_experiencia, fim_experiencia, salario, crf_numero, status) FROM stdin;
7102	50211	147	BALC	CLT_IND	2024-02-05	\N	\N	1690.00	\N	ATIVO
9140	58801	312	BALC	CLT_EXP	2026-08-03	45	2026-09-17	1820.00	\N	ATIVO
9177	58902	205	FARM	CLT_EXP	2026-09-01	45	2026-10-16	5600.00	CRF-MG 00001	ATIVO
9201	58933	147	BALC	CLT_EXP	2026-09-14	45	2026-10-29	1690.00	\N	ATIVO
9208	58940	147	BALC	CLT_EXP	2026-09-21	45	2026-11-05	1690.00	\N	ATIVO
9233	58977	288	FARM_RT	CLT_EXP	2026-10-05	45	2026-11-19	6100.00	\N	ATIVO
9234	58978	312	BALC	CLT_EXP	2026-10-05	45	2026-11-19	1820.00	\N	ATIVO
9240	58985	205	BALC	CLT_EXP	2026-10-06	45	2026-11-20	1690.00	\N	ATIVO
9251	58991	288	BALC	CLT_EXP	2026-10-19	45	2026-12-03	1820.00	\N	ATIVO
\.

COPY exame_admissional (id, matricula, dt_emissao, resultado, medico_crm, cid_restricao, observacao_clinica) FROM stdin;
3301	58801	2026-07-22	APTO	CRM-SP 00011	\N	\N
3320	58902	2026-08-19	APTO	CRM-MG 00022	\N	\N
3344	58933	2026-09-01	APTO	CRM-MG 00022	\N	\N
3345	58940	2026-07-20	APTO	CRM-MG 00022	\N	\N
3371	58977	2026-09-23	APTO	CRM-SP 00033	\N	\N
3372	58978	2026-09-24	APTO	CRM-SP 00011	\N	\N
3380	58985	2026-10-09	APTO	CRM-MG 00022	E11	Diabetes tipo 2 controlada; evitar jejum prolongado
3381	58991	2026-09-04	APTO	CRM-SP 00033	\N	\N
\.

COPY evento_esocial (id, matricula, evento, dt_limite, dt_envio, recibo) FROM stdin;
80101	58933	S-2190	2026-09-13	2026-09-11	1.2.0000000000000000101
80102	58933	S-2200	2026-10-15	2026-10-02	1.2.0000000000000000102
80103	58985	S-2190	2026-10-05	2026-10-05	1.2.0000000000000000103
80104	58985	S-2200	2026-11-15	\N	\N
\.

ALTER TABLE contrato ENABLE TRIGGER ALL;
-- PostgreSQL database dump complete

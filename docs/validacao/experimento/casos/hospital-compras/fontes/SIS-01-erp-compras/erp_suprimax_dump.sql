--
-- PostgreSQL database dump -- SupriMax ERP (módulo Compras e Contratos)
-- Rede Hospitalar Aurora do Vale -- BASE FICTÍCIA, CNPJs e pessoas inventados
-- Extração: 2026-09-30 02:00
-- Recorte: categoria 'MANUT_EQUIP'. contrato: todas as linhas da categoria.
--          contrato_item, medicao, requisicao e ordem_compra: amostra.
--

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

CREATE FUNCTION fn_valida_alcada_oc() RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE v_nivel smallint;
BEGIN
    IF NEW.tipo = 'EMERGENCIAL' OR NEW.aprovador_id IS NULL THEN
        RETURN NEW;
    END IF;
    SELECT nivel_alcada INTO v_nivel FROM usuario WHERE id = NEW.aprovador_id;
    IF NEW.valor_total > 250000 AND v_nivel < 3 THEN
        RAISE EXCEPTION 'OC % exige aprovador nivel 3', NEW.numero;
    ELSIF NEW.valor_total > 80000 AND v_nivel < 2 THEN
        RAISE EXCEPTION 'OC % exige aprovador nivel 2', NEW.numero;
    ELSIF v_nivel < 1 THEN
        RAISE EXCEPTION 'Usuario sem alcada para aprovar OC %', NEW.numero;
    END IF;
    RETURN NEW;
END $$;

CREATE FUNCTION fn_valida_cotacoes() RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE v_qtd integer;
BEGIN
    SELECT count(*) INTO v_qtd FROM cotacao WHERE requisicao_id = NEW.requisicao_id;
    IF NEW.tipo = 'REGULAR' AND NEW.valor_total >= 25000 AND v_qtd < 3 THEN
        RAISE EXCEPTION 'OC % exige 3 cotacoes (encontradas %)', NEW.numero, v_qtd;
    END IF;
    RETURN NEW;
END $$;

CREATE FUNCTION fn_valida_alcada_contrato() RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE v_nivel smallint;
BEGIN
    IF NEW.aprovado_por IS NULL THEN
        RETURN NEW;
    END IF;
    SELECT nivel_alcada INTO v_nivel FROM usuario WHERE id = NEW.aprovado_por;
    IF NEW.valor_mensal > 250000 AND v_nivel < 3 THEN
        RAISE EXCEPTION 'Contrato % exige aprovador nivel 3', NEW.numero;
    ELSIF NEW.valor_mensal > 80000 AND v_nivel < 2 THEN
        RAISE EXCEPTION 'Contrato % exige aprovador nivel 2', NEW.numero;
    ELSIF v_nivel < 1 THEN
        RAISE EXCEPTION 'Usuario sem alcada para aprovar contrato %', NEW.numero;
    END IF;
    RETURN NEW;
END $$;

CREATE FUNCTION fn_libera_medicao() RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE v_status varchar(10);
BEGIN
    IF NEW.status = 'LIBERADA' THEN
        SELECT status INTO v_status FROM contrato WHERE id = NEW.contrato_id;
        IF v_status <> 'ATIVO' THEN
            RAISE EXCEPTION 'Contrato da medicao % nao esta ativo', NEW.id;
        END IF;
    END IF;
    RETURN NEW;
END $$;

CREATE TABLE filial (
    id        char(2) PRIMARY KEY,
    nome      varchar(60) NOT NULL
);

CREATE TABLE usuario (
    id            integer PRIMARY KEY,
    nome          varchar(60) NOT NULL,
    perfil        varchar(40) NOT NULL,
    nivel_alcada  smallint NOT NULL DEFAULT 0
);

CREATE TABLE fornecedor (
    id            integer PRIMARY KEY,
    razao_social  varchar(120) NOT NULL,
    cnpj          char(14) NOT NULL UNIQUE,
    ativo         boolean NOT NULL DEFAULT true
);

CREATE TABLE contrato (
    id                  integer PRIMARY KEY,
    numero              varchar(12) NOT NULL UNIQUE,
    filial_id           char(2) NOT NULL,
    fornecedor_id       integer NOT NULL,
    objeto              varchar(120) NOT NULL,
    data_inicio         date NOT NULL,
    data_fim            date NOT NULL,
    moeda               char(3) NOT NULL DEFAULT 'BRL' CHECK (moeda IN ('BRL','USD')),
    valor_mensal        numeric(12,2) NOT NULL,
    indice_reajuste     varchar(6) NOT NULL DEFAULT 'IGPM' CHECK (indice_reajuste IN ('IGPM','IPCA','NENHUM')),
    dt_ultimo_reajuste  date,
    ultimo_aditivo_em   date,
    status              varchar(10) NOT NULL DEFAULT 'ATIVO' CHECK (status IN ('ATIVO','SUSPENSO','ENCERRADO')),
    aprovado_por        integer
);

CREATE TABLE contrato_item (
    contrato_id  integer NOT NULL,
    patrimonio   varchar(10) NOT NULL,
    PRIMARY KEY (contrato_id, patrimonio)
);

CREATE TABLE medicao (
    id            integer PRIMARY KEY,
    contrato_id   integer NOT NULL,
    competencia   char(7) NOT NULL,
    valor         numeric(12,2) NOT NULL,
    glosa         numeric(12,2) NOT NULL DEFAULT 0,
    ateste_por    integer,
    ateste_em     date,
    status        varchar(10) NOT NULL DEFAULT 'ABERTA' CHECK (status IN ('ABERTA','LIBERADA','PAGA')),
    pago_em       date
);

CREATE TABLE requisicao (
    id              integer PRIMARY KEY,
    filial_id       char(2) NOT NULL,
    solicitante_id  integer NOT NULL,
    criada_em       date NOT NULL,
    descricao       varchar(120) NOT NULL,
    valor_estimado  numeric(12,2) NOT NULL,
    origem_os       varchar(20)
);

CREATE TABLE cotacao (
    id             integer PRIMARY KEY,
    requisicao_id  integer NOT NULL,
    fornecedor_id  integer NOT NULL,
    valor          numeric(12,2) NOT NULL
);

CREATE TABLE ordem_compra (
    numero                varchar(13) PRIMARY KEY,
    requisicao_id         integer NOT NULL,
    filial_id             char(2) NOT NULL,
    fornecedor_id         integer NOT NULL,
    contrato_id           integer,
    tipo                  varchar(12) NOT NULL DEFAULT 'REGULAR' CHECK (tipo IN ('REGULAR','EMERGENCIAL','AVULSA')),
    valor_total           numeric(12,2) NOT NULL,
    solicitante_id        integer NOT NULL,
    aprovador_id          integer,
    emitida_em            date NOT NULL,
    aprovada_em           date,
    prazo_pagamento_dias  smallint NOT NULL DEFAULT 30,
    CONSTRAINT chk_prazo_pagamento CHECK (prazo_pagamento_dias BETWEEN 15 AND 30)
);

INSERT INTO filial VALUES ('01','Hospital Aurora Central'),('02','Hospital Aurora Norte'),('03','Hospital Aurora Litoral'),('04','Centro de Diagnostico Aurora Sul');

INSERT INTO usuario VALUES
 (1,'Renata Gaspar','Diretora Geral',3),
 (2,'Luis Mota','Diretor Financeiro',2),
 (3,'Claudia Freitas','Gerente de Suprimentos',1),
 (4,'Paulo Neri','Analista de Compras',0),
 (5,'Helio Sampaio','Diretor Tecnico',2),
 (6,'Beatriz Tavares','Gerente de Engenharia Clinica',0),
 (7,'Marta Quintela','Advogada',0);

INSERT INTO fornecedor (id, razao_social, cnpj) VALUES
 (10,'MTS Engenharia Biomedica Ltda','00111222000101'),
 (11,'Helvion Medical do Brasil Ltda','00333444000102'),
 (12,'Clarivent Servicos Hospitalares S.A.','00555666000103'),
 (13,'Termolab Calibracoes Ltda','00777888000104'),
 (14,'NorteGas Engenharia de Gases Ltda','00999000000105'),
 (15,'Litoral Eletromedica ME','00123456000106'),
 (16,'Hemofix Servicos ME','00246810000107');

INSERT INTO contrato VALUES
 (101,'CT-2022-0055','03',15,'Monitores e desfibriladores','2022-09-01','2025-08-31','BRL',7480.00,'IGPM','2024-09-01',NULL,'ATIVO',3),
 (102,'CT-2023-0019','01',12,'Ventiladores pulmonares','2023-03-01','2027-02-28','BRL',31500.00,'IGPM','2024-03-01',NULL,'ATIVO',2),
 (103,'CT-2023-0088','01',10,'Monitores multiparametricos e desfibriladores','2023-07-01','2026-12-31','BRL',14200.00,'IGPM','2024-07-01','2026-05-20','ATIVO',3),
 (104,'CT-2024-0117','02',10,'Monitores e desfibriladores','2024-05-01','2027-04-30','BRL',11040.00,'IPCA','2026-05-01',NULL,'ATIVO',3),
 (105,'CT-2025-0031','01',11,'Tomografo e ressonancia','2025-04-01','2028-03-31','USD',9800.00,'NENHUM',NULL,NULL,'ATIVO',1),
 (106,'CT-2025-0064','02',14,'Usina de oxigenio e central de gases','2025-02-01','2027-01-31','BRL',22000.00,'IGPM',NULL,NULL,'ATIVO',3),
 (107,'CT-2025-0102','01',13,'Calibracao de instrumentos','2025-03-01','2027-02-28','BRL',6800.00,'IPCA',NULL,NULL,'ATIVO',3);

INSERT INTO contrato_item VALUES
 (101,'PAT-015530'),(102,'PAT-004512'),(102,'PAT-004513'),(103,'PAT-007731'),
 (104,'PAT-011208'),(104,'PAT-011340'),(105,'PAT-020077'),(106,'PAT-012900');

INSERT INTO medicao VALUES
 (9001,101,'2026-08',7480.00,0,6,'2026-09-03','PAGA','2026-09-15'),
 (9002,103,'2026-08',14200.00,0,NULL,NULL,'PAGA','2026-09-15'),
 (9003,104,'2026-08',11040.00,0,6,'2026-09-04','PAGA','2026-09-15'),
 (9004,105,'2026-08',9800.00,0,6,'2026-09-04','PAGA','2026-09-18'),
 (9005,106,'2026-08',22000.00,0,6,'2026-09-04','PAGA','2026-09-15');

INSERT INTO requisicao VALUES
 (501,'01',4,'2026-03-02','Pecas de reposicao para desfibriladores',149300.00,NULL),
 (502,'02',4,'2026-05-20','Revisao geral dos compressores da usina',72500.00,NULL),
 (503,'03',4,'2026-07-01','Manutencao de autoclaves CME - competencia junho',4900.00,NULL),
 (504,'01',6,'2026-07-14','Modulos de turbina para ventiladores UTI',92000.00,NULL),
 (505,'04',3,'2026-07-20','Calibracao avulsa de instrumentos do CDI',8400.00,NULL),
 (506,'03',4,'2026-08-01','Manutencao de autoclaves CME - competencia julho',4900.00,NULL),
 (507,'03',4,'2026-08-12','Placa de potencia de monitor',19800.00,'OS 88190'),
 (508,'03',4,'2026-09-01','Manutencao de autoclaves CME - competencia agosto',4900.00,NULL);

INSERT INTO cotacao VALUES
 (7001,501,10,149300.00),(7002,501,11,158000.00),(7003,501,15,162400.00),
 (7004,502,14,72500.00),(7005,502,10,78100.00),(7006,502,13,81000.00),
 (7007,504,12,92000.00),
 (7008,505,13,8400.00),(7009,505,10,9150.00),
 (7010,507,15,19800.00);

INSERT INTO ordem_compra VALUES
 ('OC-2026-00301',501,'01',10,NULL,'REGULAR',49800.00,4,3,'2026-03-10','2026-03-10',30),
 ('OC-2026-00302',501,'01',10,NULL,'REGULAR',49700.00,4,3,'2026-03-10','2026-03-10',30),
 ('OC-2026-00303',501,'01',10,NULL,'REGULAR',49800.00,4,3,'2026-03-10','2026-03-10',30),
 ('OC-2026-00388',502,'02',14,106,'REGULAR',72500.00,4,3,'2026-06-09','2026-06-11',30),
 ('OC-2026-00409',503,'03',16,NULL,'AVULSA',4900.00,4,3,'2026-07-06','2026-07-06',30),
 ('OC-2026-00412',504,'01',12,102,'EMERGENCIAL',92000.00,6,5,'2026-07-14','2026-07-16',15),
 ('OC-2026-00420',505,'04',13,NULL,'REGULAR',8400.00,3,3,'2026-07-28','2026-07-28',30),
 ('OC-2026-00431',506,'03',16,NULL,'AVULSA',4900.00,4,3,'2026-08-05','2026-08-05',30),
 ('OC-2026-00440',507,'03',15,101,'REGULAR',19800.00,4,3,'2026-08-18','2026-08-18',28),
 ('OC-2026-00452',508,'03',16,NULL,'AVULSA',4900.00,4,3,'2026-09-04','2026-09-04',30);

ALTER TABLE contrato ADD CONSTRAINT fk_contrato_filial FOREIGN KEY (filial_id) REFERENCES filial(id);
ALTER TABLE contrato ADD CONSTRAINT fk_contrato_fornecedor FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id);
ALTER TABLE contrato ADD CONSTRAINT fk_contrato_aprovador FOREIGN KEY (aprovado_por) REFERENCES usuario(id);
ALTER TABLE contrato_item ADD CONSTRAINT fk_item_contrato FOREIGN KEY (contrato_id) REFERENCES contrato(id);
ALTER TABLE medicao ADD CONSTRAINT fk_medicao_contrato FOREIGN KEY (contrato_id) REFERENCES contrato(id);
ALTER TABLE cotacao ADD CONSTRAINT fk_cotacao_req FOREIGN KEY (requisicao_id) REFERENCES requisicao(id);
ALTER TABLE ordem_compra ADD CONSTRAINT fk_oc_req FOREIGN KEY (requisicao_id) REFERENCES requisicao(id);
ALTER TABLE ordem_compra ADD CONSTRAINT fk_oc_fornecedor FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id);
ALTER TABLE ordem_compra ADD CONSTRAINT fk_oc_contrato FOREIGN KEY (contrato_id) REFERENCES contrato(id);

CREATE TRIGGER trg_oc_alcada BEFORE INSERT OR UPDATE OF aprovador_id ON ordem_compra
    FOR EACH ROW EXECUTE FUNCTION fn_valida_alcada_oc();
CREATE TRIGGER trg_oc_cotacoes BEFORE INSERT ON ordem_compra
    FOR EACH ROW EXECUTE FUNCTION fn_valida_cotacoes();
CREATE TRIGGER trg_contrato_alcada BEFORE INSERT OR UPDATE OF aprovado_por ON contrato
    FOR EACH ROW EXECUTE FUNCTION fn_valida_alcada_contrato();
CREATE TRIGGER trg_medicao_libera BEFORE UPDATE OF status ON medicao
    FOR EACH ROW EXECUTE FUNCTION fn_libera_medicao();

--
-- PostgreSQL database dump complete
--

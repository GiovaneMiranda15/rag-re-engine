-- VendaMax ERP — dump de estrutura e dados (PostgreSQL 13)
-- Gerado em 2026-10-01 03:00

CREATE TABLE cliente (
    id            SERIAL PRIMARY KEY,
    razao_social  VARCHAR(150) NOT NULL,
    cnpj          CHAR(14) NOT NULL UNIQUE,
    limite_credito NUMERIC(12,2) NOT NULL DEFAULT 0,
    bloqueado     BOOLEAN NOT NULL DEFAULT FALSE,
    vendedor_id   INT
);
COMMENT ON COLUMN cliente.limite_credito IS 'Definido manualmente pelo financeiro; revisado a cada 6 meses';

CREATE TABLE vendedor (
    id        SERIAL PRIMARY KEY,
    nome      VARCHAR(100) NOT NULL,
    tipo      VARCHAR(20) NOT NULL CHECK (tipo IN ('interno', 'representante')),
    meta_mensal NUMERIC(12,2)
);

CREATE TABLE produto (
    id          SERIAL PRIMARY KEY,
    sku         VARCHAR(30) NOT NULL UNIQUE,
    descricao   VARCHAR(200) NOT NULL,
    preco_tabela NUMERIC(12,2) NOT NULL,
    estoque     INT NOT NULL DEFAULT 0
);

CREATE TABLE pedido (
    id            SERIAL PRIMARY KEY,
    cliente_id    INT NOT NULL REFERENCES cliente(id),
    vendedor_id   INT REFERENCES vendedor(id),
    origem        VARCHAR(10) NOT NULL DEFAULT 'erp' CHECK (origem IN ('erp', 'loja')),
    status        VARCHAR(20) NOT NULL DEFAULT 'digitado'
                  CHECK (status IN ('digitado', 'aguardando_credito', 'aprovado', 'faturado', 'cancelado')),
    desconto_pct  NUMERIC(5,2) NOT NULL DEFAULT 0,
    total         NUMERIC(12,2) NOT NULL,
    criado_em     TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE pedido_item (
    pedido_id   INT NOT NULL REFERENCES pedido(id),
    produto_id  INT NOT NULL REFERENCES produto(id),
    quantidade  INT NOT NULL CHECK (quantidade > 0),
    preco_unit  NUMERIC(12,2) NOT NULL,
    PRIMARY KEY (pedido_id, produto_id)
);

CREATE TABLE comissao (
    pedido_id    INT PRIMARY KEY REFERENCES pedido(id),
    vendedor_id  INT NOT NULL REFERENCES vendedor(id),
    valor        NUMERIC(12,2) NOT NULL,
    calculada_em TIMESTAMP NOT NULL DEFAULT now()
);

-- Regra: desconto acima de 10% é recusado no ERP
CREATE OR REPLACE FUNCTION fn_valida_desconto() RETURNS trigger AS $$
BEGIN
    IF NEW.desconto_pct > 10 THEN
        RAISE EXCEPTION 'Desconto máximo permitido é 10%%';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_valida_desconto
    BEFORE INSERT OR UPDATE ON pedido
    FOR EACH ROW EXECUTE FUNCTION fn_valida_desconto();

-- Regra: pedido acima do limite de crédito vai para aprovação manual
CREATE OR REPLACE FUNCTION fn_checa_credito() RETURNS trigger AS $$
DECLARE lim NUMERIC;
BEGIN
    SELECT limite_credito INTO lim FROM cliente WHERE id = NEW.cliente_id;
    IF NEW.total > lim THEN
        NEW.status := 'aguardando_credito';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_checa_credito
    BEFORE INSERT ON pedido
    FOR EACH ROW EXECUTE FUNCTION fn_checa_credito();

-- Comissão: 3% sobre o total faturado, gravada ao faturar
CREATE OR REPLACE FUNCTION fn_calcula_comissao() RETURNS trigger AS $$
BEGIN
    IF NEW.status = 'faturado' AND NEW.vendedor_id IS NOT NULL THEN
        INSERT INTO comissao (pedido_id, vendedor_id, valor)
        VALUES (NEW.id, NEW.vendedor_id, NEW.total * 0.03)
        ON CONFLICT (pedido_id) DO NOTHING;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_calcula_comissao
    AFTER UPDATE OF status ON pedido
    FOR EACH ROW EXECUTE FUNCTION fn_calcula_comissao();

COPY public.cliente (id, razao_social, cnpj, limite_credito, bloqueado, vendedor_id) FROM stdin;
1	Eletro Centro Ltda	11222333000144	50000.00	f	1
2	Construtora Pioneira SA	55666777000188	120000.00	f	2
\.

INSERT INTO vendedor VALUES (1, 'Marcos Lima', 'interno', 80000.00);
INSERT INTO vendedor VALUES (2, 'Rep. Sul Distribuição', 'representante', 150000.00);

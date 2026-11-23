-- LojaB2B — estrutura (MySQL 8)

CREATE TABLE clientes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(150) NOT NULL,
  cpf_cnpj VARCHAR(18) NOT NULL,          -- com máscara, aceita CPF ou CNPJ
  email VARCHAR(120) NOT NULL UNIQUE,
  senha_hash VARCHAR(255) NOT NULL,
  aceita_marketing TINYINT(1) NOT NULL DEFAULT 1,
  criado_em DATETIME NOT NULL
);

CREATE TABLE produtos (
  sku VARCHAR(30) PRIMARY KEY,
  nome VARCHAR(200) NOT NULL,
  preco DECIMAL(12,2) NOT NULL,           -- atualizado pelo CSV do ERP 1x por dia
  estoque_disponivel INT NOT NULL         -- atualizado pelo CSV do ERP 1x por dia
);

CREATE TABLE cupons (
  codigo VARCHAR(20) PRIMARY KEY,
  desconto_pct DECIMAL(5,2) NOT NULL CHECK (desconto_pct <= 15),
  valido_ate DATE NOT NULL
);

CREATE TABLE pedidos_web (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT NOT NULL,
  cupom VARCHAR(20),
  total DECIMAL(12,2) NOT NULL,
  forma_pagamento ENUM('boleto','pix','cartao') NOT NULL,
  exportado_erp TINYINT(1) NOT NULL DEFAULT 0,
  criado_em DATETIME NOT NULL,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id),
  FOREIGN KEY (cupom) REFERENCES cupons(codigo)
);

CREATE TABLE itens_pedido_web (
  pedido_id INT NOT NULL,
  sku VARCHAR(30) NOT NULL,
  qtd INT NOT NULL,
  preco DECIMAL(12,2) NOT NULL,
  PRIMARY KEY (pedido_id, sku),
  FOREIGN KEY (pedido_id) REFERENCES pedidos_web(id)
);

LOCK TABLES `cupons` WRITE;
INSERT INTO `cupons` VALUES ('BLACK15',15.00,'2026-11-30'),('PRIMEIRA10',10.00,'2026-12-31');
UNLOCK TABLES;

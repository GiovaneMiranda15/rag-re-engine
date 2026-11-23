-- MySQL dump 10.13 -- ManutClin 4.2 (gestão de ordens de serviço da Engenharia Clínica)
-- Rede Hospitalar Aurora do Vale -- BASE FICTÍCIA, pessoas e pacientes inventados
-- Host: manutclin-db    Database: manutclin
-- Dump completed on 2026-09-30  02:30:00
-- Recorte: prestador e contrato_ref completos; equipamento e ordem_servico: amostra.

CREATE TABLE `site` (
  `codigo` char(3) NOT NULL,
  `nome` varchar(40) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `site` VALUES ('CEN','Aurora Central'),('LIT','Aurora Litoral'),('NOR','Aurora Norte'),('SUL','CDI Aurora Sul');

CREATE TABLE `prestador` (
  `id` int NOT NULL,
  `nome` varchar(60) NOT NULL,
  `cnpj` char(14) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `prestador` VALUES
(1,'BioVolt','00111222000101'),
(2,'Helvion','00333444000102'),
(3,'Clarivent','00555666000103'),
(4,'Termolab','00777888000104'),
(5,'NorteGas','00999000000105'),
(6,'Litoral Eletromedica','00123456000106'),
(7,'Hemofix','00246810000107');

CREATE TABLE `contrato_ref` (
  `numero` varchar(12) NOT NULL,
  `prestador_id` int NOT NULL,
  `sla_atendimento_h` smallint NOT NULL,
  `sla_solucao_h` smallint NOT NULL,
  PRIMARY KEY (`numero`),
  CONSTRAINT `fk_ref_prestador` FOREIGN KEY (`prestador_id`) REFERENCES `prestador` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `contrato_ref` VALUES
('CT-2022-0055',6,12,72),
('CT-2023-0019',3,4,24),
('CT-2023-0088',1,8,48),
('CT-2024-0117',1,8,48),
('CT-2025-0031',2,6,48),
('CT-2025-0064',5,2,12),
('CT-2025-0102',4,48,120),
('CT-2026-0021',7,24,72);

CREATE TABLE `equipamento` (
  `tag` varchar(10) NOT NULL,
  `site` char(3) NOT NULL,
  `descricao` varchar(60) NOT NULL,
  `classe` char(3) NOT NULL,
  `criticidade` enum('A','B','C') NOT NULL,
  `status` enum('EM_USO','MANUTENCAO','RESERVA','BAIXADO') NOT NULL DEFAULT 'EM_USO',
  `dt_ultima_calibracao` date DEFAULT NULL,
  `validade_calibracao` date DEFAULT NULL,
  `contrato_numero` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`tag`),
  CONSTRAINT `fk_equip_site` FOREIGN KEY (`site`) REFERENCES `site` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `equipamento` VALUES
('PAT-004512','CEN','Ventilador pulmonar UTI-2','VEN','A','EM_USO','2025-03-31','2026-03-31','CT-2023-0019'),
('PAT-004513','CEN','Ventilador pulmonar UTI-3','VEN','A','MANUTENCAO','2026-01-15','2027-01-15','CT-2023-0019'),
('PAT-007731','CEN','Monitor multiparametrico','MON','B','EM_USO','2025-12-10','2026-12-10','CT-2023-0088'),
('PAT-011208','NOR','Desfibrilador','DEF','A','EM_USO','2026-02-20','2027-02-20','CT-2024-0117'),
('PAT-011340','NOR','Monitor multiparametrico','MON','B','EM_USO','2026-04-02','2027-04-02','CT-2024-0117'),
('PAT-012900','NOR','Usina de oxigenio','USI','A','EM_USO','2026-05-11','2027-05-11','CT-2025-0064'),
('PAT-015530','LIT','Monitor multiparametrico','MON','B','EM_USO','2025-11-19','2026-11-19','CT-2022-0055'),
('PAT-016002','LIT','Autoclave CME','AUT','B','EM_USO',NULL,NULL,'CT-2026-0021'),
('PAT-020077','CEN','Tomografo','TOM','B','EM_USO','2026-06-30','2027-06-30','CT-2025-0031');

CREATE TABLE `plano_preventivo` (
  `classe` char(3) NOT NULL,
  `site` char(3) NOT NULL,
  `periodicidade_dias` smallint NOT NULL,
  PRIMARY KEY (`classe`,`site`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `plano_preventivo` VALUES
('AUT','LIT',90),('DEF','NOR',180),('MON','CEN',180),('MON','LIT',180),('MON','NOR',180),
('TOM','CEN',90),('USI','NOR',90),('VEN','CEN',365);

CREATE TABLE `ordem_servico` (
  `id` int NOT NULL,
  `tag` varchar(10) NOT NULL,
  `tipo` enum('CORRETIVA','PREVENTIVA','CALIBRACAO') NOT NULL,
  `abertura` datetime NOT NULL,
  `atendimento` datetime DEFAULT NULL,
  `fechamento` datetime DEFAULT NULL,
  `status` enum('ABERTA','EM_ATENDIMENTO','AGUARDANDO_PECA','AGUARDANDO_COMPRA','FECHADA') NOT NULL DEFAULT 'ABERTA',
  `contrato_numero` varchar(12) DEFAULT NULL,
  `requisicao_erp` varchar(20) DEFAULT NULL,
  `descricao` varchar(160) NOT NULL,
  `teste_seg_eletrica` enum('APROVADO','REPROVADO') DEFAULT NULL,
  `liberado_por` varchar(40) DEFAULT NULL,
  `evento_adverso` tinyint(1) NOT NULL DEFAULT '0',
  `paciente_nome` varchar(80) DEFAULT NULL,
  `paciente_prontuario` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_os_equip` FOREIGN KEY (`tag`) REFERENCES `equipamento` (`tag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `ordem_servico` VALUES
(88170,'PAT-011340','CORRETIVA','2026-08-04 08:00:00','2026-08-04 22:10:00','2026-08-05 17:00:00','FECHADA','CT-2024-0117',NULL,'Tela sem curva de SpO2','APROVADO','B.Tavares',0,NULL,NULL),
(88190,'PAT-015530','CORRETIVA','2026-08-11 09:20:00','2026-08-11 18:00:00','2026-09-02 15:00:00','FECHADA','CT-2022-0055','REQ 507','Placa de potencia queimada; aguardou compra da placa','APROVADO','B.Tavares',0,NULL,NULL),
(88213,'PAT-004512','CORRETIVA','2026-08-20 02:15:00','2026-08-20 05:40:00','2026-08-20 11:00:00','FECHADA','CT-2023-0019',NULL,'Alarme de desconexao nao disparou em uso na UTI-2, paciente dessaturou; sensor trocado',NULL,NULL,1,'Paciente Ficticio Um','PR-0004471'),
(88240,'PAT-004513','CORRETIVA','2026-09-18 10:05:00','2026-09-18 13:30:00',NULL,'AGUARDANDO_COMPRA','CT-2023-0019',NULL,'Valvula expiratoria com vazamento; item nao coberto',NULL,NULL,0,NULL,NULL),
(88255,'PAT-007731','PREVENTIVA','2026-09-02 08:00:00','2026-09-02 09:00:00','2026-09-02 11:40:00','FECHADA','CT-2023-0088',NULL,'Preventiva semestral','APROVADO','B.Tavares',0,NULL,NULL),
(88260,'PAT-016002','CORRETIVA','2026-09-08 07:40:00','2026-09-08 16:20:00','2026-09-09 10:00:00','FECHADA','CT-2026-0021',NULL,'Falha na vedacao da porta','APROVADO','B.Tavares',0,NULL,NULL),
(88271,'PAT-020077','CORRETIVA','2026-09-10 08:00:00','2026-09-10 13:30:00','2026-09-11 16:00:00','FECHADA','CT-2025-0031',NULL,'Erro de refrigeracao do gantry','APROVADO','B.Tavares',0,NULL,NULL);

DELIMITER ;;
CREATE TRIGGER `trg_os_abre` AFTER INSERT ON `ordem_servico` FOR EACH ROW
BEGIN
  IF NEW.tipo = 'CORRETIVA' THEN
    UPDATE equipamento SET status = 'MANUTENCAO' WHERE tag = NEW.tag;
  END IF;
END ;;
CREATE TRIGGER `trg_os_fecha` AFTER UPDATE ON `ordem_servico` FOR EACH ROW
BEGIN
  IF NEW.status = 'FECHADA' AND OLD.status <> 'FECHADA' THEN
    UPDATE equipamento SET status = 'EM_USO' WHERE tag = NEW.tag;
  END IF;
END ;;
DELIMITER ;

-- pt-show-grants (trecho)
CREATE USER IF NOT EXISTS 'prestador_portal'@'%';
GRANT SELECT, UPDATE (`atendimento`, `descricao`) ON `manutclin`.`ordem_servico` TO 'prestador_portal'@'%';
GRANT SELECT ON `manutclin`.`equipamento` TO 'prestador_portal'@'%';

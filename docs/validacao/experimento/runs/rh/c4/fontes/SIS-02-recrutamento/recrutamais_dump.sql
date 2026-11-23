-- MySQL dump 10.13  Distrib 8.0.36
-- Host: recrutamais-caliandra    Database: recrutamais
-- Instância dedicada Recruta+ (fornecedor externo)
-- Dump completed on 2026-10-20 03:10:12
-- Amostra de dados

CREATE TABLE `unidade` (
  `cod_unidade` varchar(8) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `uf` char(2) NOT NULL,
  PRIMARY KEY (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tabela_salarial` (
  `cargo` varchar(30) NOT NULL,
  `uf` char(2) NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  `vigencia_inicio` date NOT NULL,
  PRIMARY KEY (`cargo`,`uf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `candidato` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cpf` varchar(14) NOT NULL,
  `nome` varchar(120) NOT NULL,
  `email` varchar(120) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `nascimento` date DEFAULT NULL,
  `gestante` tinyint(1) DEFAULT NULL,
  `pcd` tinyint(1) DEFAULT '0',
  `pcd_cid` varchar(8) DEFAULT NULL,
  `antecedentes_ok` tinyint(1) DEFAULT NULL,
  `antecedentes_obs` text,
  `status` enum('NOVO','ENTREVISTA','APROVADO','REPROVADO','CONTRATADO') NOT NULL DEFAULT 'NOVO',
  `dt_atualizacao` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_cpf` (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `vaga` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cod_unidade` varchar(8) NOT NULL,
  `cargo` varchar(30) NOT NULL,
  `salario_ref` decimal(10,2) DEFAULT NULL,
  `aberta_em` date NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_vaga_unidade` FOREIGN KEY (`cod_unidade`) REFERENCES `unidade` (`cod_unidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `oferta` (
  `id` int NOT NULL AUTO_INCREMENT,
  `candidato_id` int NOT NULL,
  `vaga_id` int NOT NULL,
  `salario` decimal(10,2) NOT NULL,
  `aprovador_perfil` enum('GERENTE_LOJA','GERENTE_REGIONAL') NOT NULL,
  `aprovador_nome` varchar(120) NOT NULL,
  `dt_aprovacao` date NOT NULL,
  `status` enum('PENDENTE','ACEITA','RECUSADA','CANCELADA') NOT NULL DEFAULT 'PENDENTE',
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_oferta_candidato` FOREIGN KEY (`candidato_id`) REFERENCES `candidato` (`id`),
  CONSTRAINT `fk_oferta_vaga` FOREIGN KEY (`vaga_id`) REFERENCES `vaga` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `candidato_bkp_2022` (
  `id` int NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `nome` varchar(120) NOT NULL,
  `email` varchar(120) DEFAULT NULL,
  `nascimento` date DEFAULT NULL,
  `gestante` tinyint(1) DEFAULT NULL,
  `pcd_cid` varchar(8) DEFAULT NULL,
  `antecedentes_obs` text,
  `status` varchar(12) DEFAULT NULL,
  `dt_atualizacao` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELIMITER ;;
CREATE TRIGGER `trg_oferta_aceita` AFTER UPDATE ON `oferta` FOR EACH ROW
BEGIN
  IF NEW.status = 'ACEITA' AND OLD.status <> 'ACEITA' THEN
    UPDATE candidato SET status = 'CONTRATADO', dt_atualizacao = CURDATE() WHERE id = NEW.candidato_id;
  END IF;
END ;;

CREATE PROCEDURE `sp_expurgo_candidatos`()
BEGIN
  DELETE FROM candidato
   WHERE status = 'REPROVADO'
     AND dt_atualizacao < DATE_SUB(CURDATE(), INTERVAL 24 MONTH);
END ;;
DELIMITER ;

CREATE EVENT `ev_expurgo_mensal`
  ON SCHEDULE EVERY 1 MONTH STARTS '2023-01-01 04:00:00'
  DO CALL sp_expurgo_candidatos();

GRANT SELECT ON `recrutamais`.`candidato` TO 'gerente_loja'@'%';
GRANT SELECT ON `recrutamais`.`vaga` TO 'gerente_loja'@'%';
GRANT SELECT, UPDATE ON `recrutamais`.`oferta` TO 'gerente_loja'@'%';
GRANT SELECT ON `recrutamais`.`candidato_bkp_2022` TO 'gerente_loja'@'%';
GRANT SELECT ON `recrutamais`.`candidato_bkp_2022` TO 'app_relatorios'@'%';

INSERT INTO `unidade` VALUES
('LJ-0147','Savassi','MG'),('LJ-0205','Eldorado','MG'),('LJ-0288','Cambuí','SP'),('LJ-0312','Pinheiros','SP');

INSERT INTO `tabela_salarial` VALUES
('BALCONISTA','MG',1690.00,'2026-02-01'),
('BALCONISTA','SP',1750.00,'2025-03-01'),
('FARMACEUTICO','MG',5600.00,'2026-02-01'),
('FARMACEUTICO','SP',6100.00,'2026-03-01');

INSERT INTO `candidato` VALUES
(1001,'000.000.001-01','Ana Beatriz Moura','ana.moura.fic@exemplo.com','(31) 90000-0101','1998-11-02',0,0,NULL,1,NULL,'CONTRATADO','2026-08-25'),
(1002,'000.000.003-03','Carlos Eduardo Lima','carloseduardo.lima.fic@exemplo.com','(11) 90000-0303','1999-07-22',0,0,NULL,1,NULL,'CONTRATADO','2026-07-14'),
(1003,'000.000.005-05','Renato Alves Pires','renato.pires.fic@exemplo.com','(31) 90000-0505','1990-05-30',0,0,NULL,1,NULL,'CONTRATADO','2026-08-11'),
(1004,'000.000.004-04','Juliana Prado Nogueira','juliana.prado.fic@exemplo.com','(19) 90000-0404','1993-08-14',0,0,NULL,1,NULL,'CONTRATADO','2026-09-16'),
(1005,'000.000.006-06','Thiago Mendes Rocha','thiago.rocha.fic@exemplo.com','(11) 90000-0606','2002-04-09',0,0,NULL,1,NULL,'CONTRATADO','2026-09-16'),
(1006,'000.000.007-07','Larissa Campos Freitas','larissa.freitas.fic@exemplo.com','(31) 90000-0707','1996-12-21',0,0,NULL,1,NULL,'CONTRATADO','2026-09-30'),
(1007,'000.000.011-11','Bruno Cardoso Neves','bruno.neves.fic@exemplo.com','(31) 90000-1111','2001-01-19',0,1,'H54.4',1,NULL,'CONTRATADO','2026-07-14'),
(1008,'000.000.012-12','Fernanda Dias Couto','fernanda.couto.fic@exemplo.com','(19) 90000-1212','1994-06-03',0,0,NULL,1,NULL,'CONTRATADO','2026-08-27'),
(1009,'000.000.010-10','Patrícia Gomes Lemos','patricia.lemos.fic@exemplo.com','(19) 90000-1010','1997-09-25',1,0,NULL,1,NULL,'CONTRATADO','2026-10-14'),
(1010,'000.000.008-08','Vitor Hugo Ramos','vitor.ramos.fic@exemplo.com','(31) 90000-0808','2010-03-02',0,0,NULL,NULL,NULL,'CONTRATADO','2026-09-29'),
(0877,'000.000.009-09','Marcos Vinícius Souto','marcos.souto.fic@exemplo.com','(31) 90000-0909','1988-02-17',0,0,NULL,0,'Consta ação trabalhista contra empregador anterior','REPROVADO','2025-02-10');

INSERT INTO `vaga` VALUES
(501,'LJ-0147','BALCONISTA',1690.00,'2026-07-01'),
(502,'LJ-0312','BALCONISTA',1750.00,'2026-06-20'),
(503,'LJ-0205','FARMACEUTICO',5600.00,'2026-07-20'),
(504,'LJ-0288','FARMACEUTICO',6100.00,'2026-08-28'),
(505,'LJ-0312','BALCONISTA',1750.00,'2026-08-20'),
(506,'LJ-0205','BALCONISTA',1690.00,'2026-09-05'),
(507,'LJ-0288','BALCONISTA',1750.00,'2026-08-01'),
(508,'LJ-0147','APRENDIZ',NULL,'2026-09-01');

INSERT INTO `oferta` VALUES
(7001,1001,501,1690.00,'GERENTE_LOJA','Ricardo Salles','2026-08-24','ACEITA'),
(7002,1002,502,1820.00,'GERENTE_LOJA','Denise Farias','2026-07-13','ACEITA'),
(7003,1003,503,5600.00,'GERENTE_REGIONAL','Paulo Henrique Dutra','2026-08-10','ACEITA'),
(7004,1004,504,6100.00,'GERENTE_REGIONAL','Silvana Moreira','2026-09-15','ACEITA'),
(7005,1005,505,1750.00,'GERENTE_LOJA','Denise Farias','2026-09-08','CANCELADA'),
(7006,1005,505,1820.00,'GERENTE_REGIONAL','Tânia Rezende','2026-09-15','ACEITA'),
(7007,1006,506,1690.00,'GERENTE_LOJA','Murilo Pena','2026-09-29','ACEITA'),
(7008,1007,501,1690.00,'GERENTE_LOJA','Ricardo Salles','2026-07-13','ACEITA'),
(7009,1008,507,1820.00,'GERENTE_LOJA','Aline Teixeira','2026-08-26','ACEITA'),
(7010,1009,507,1820.00,'GERENTE_LOJA','Aline Teixeira','2026-10-13','ACEITA'),
(7011,1010,508,850.00,'GERENTE_LOJA','Ricardo Salles','2026-09-28','ACEITA');

INSERT INTO `candidato_bkp_2022` VALUES
(311,'000.000.020-20','Elaine Martins Vaz','elaine.vaz.fic@exemplo.com','1991-04-12',1,NULL,NULL,'REPROVADO','2021-06-08'),
(344,'000.000.021-21','Jorge Luiz Paiva','jorge.paiva.fic@exemplo.com','1979-10-30',0,'F32.1','Afastamento anterior por saúde','REPROVADO','2021-09-15'),
(402,'000.000.022-22','Simone Alves Tito','simone.tito.fic@exemplo.com','1986-01-05',0,NULL,'Passagem pela polícia informada em entrevista','REPROVADO','2022-02-22');

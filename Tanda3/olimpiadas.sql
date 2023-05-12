DROP SCHEMA IF EXISTS `olimpiadas` ;
CREATE SCHEMA IF NOT EXISTS `olimpiadas` DEFAULT CHARACTER SET latin1 COLLATE latin1_spanish_ci;
USE `olimpiadas`;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;


-- ----------------
-- Tabla `Deporte`
-- -----------------

CREATE TABLE `Deporte` (
	`id_deporte` int(11) NOT NULL AUTO_INCREMENT,
	`nombre` varchar(100)  NOT NULL,
	PRIMARY KEY (`id_deporte`)
) ENGINE = InnoDB AUTO_INCREMENT = 10 DEFAULT CHARACTER SET = latin1 COLLATE = latin1_spanish_ci;

INSERT INTO`Deporte` (`id_deporte`, `nombre`)
VALUES (1, 'Basketball'), (2, 'Judo'), (3, 'Football');


-- --------------------
-- Tabla `Deportista`
-- --------------------

CREATE TABLE `Deportista` (
	`id_deportista` int(11) NOT NULL AUTO_INCREMENT,
	`nombre` varchar(150)  NOT NULL,
	`sexo` enum('M', 'F')  NOT NULL,
	`peso` int(11) DEFAULT NULL,
	`altura` int(11) DEFAULT NULL,
	`foto` blob NULL,
	PRIMARY KEY (`id_deportista`)
) ENGINE = InnoDB AUTO_INCREMENT = 10 DEFAULT CHARACTER SET = latin1 COLLATE = latin1_spanish_ci;

INSERT INTO `Deportista` ( `id_deportista`, `nombre`, `sexo`,`peso`, `altura`)
VALUES (1, 'A Dijiang', 'M', 80, 180), (2, 'A Lamusi', 'M', 60, 170);


-- -------------------
-- Tabla `Equipo`
-- -------------------

CREATE TABLE `Equipo` (
	`id_equipo` int(11) NOT NULL AUTO_INCREMENT,
	`nombre` varchar(50)  NOT NULL,
	`iniciales` varchar(3)  NOT NULL,
	PRIMARY KEY (`id_equipo`)
) ENGINE = InnoDB AUTO_INCREMENT = 10 DEFAULT CHARACTER SET = latin1 COLLATE = latin1_spanish_ci;

INSERT INTO `Equipo` (`id_equipo`,`nombre`,`iniciales`)
VALUES (1, 'China', 'CHN'), (2, 'Denmark', 'DEN');


-- --------------------
-- Tabla `Olimpiada`
-- ---------------------

CREATE TABLE `Olimpiada` (
	`id_olimpiada` int(11) NOT NULL AUTO_INCREMENT,
	`nombre` varchar(11)  NOT NULL,
	`anio` smallint(6) NOT NULL,
	`temporada` enum('Summer', 'Winter')  NOT NULL,
	`ciudad` varchar(50)  NOT NULL ,
    PRIMARY KEY (`id_olimpiada`)
) ENGINE = InnoDB AUTO_INCREMENT = 10 DEFAULT CHARACTER SET = latin1 COLLATE = latin1_spanish_ci;

INSERT INTO `Olimpiada` ( `id_olimpiada`,`nombre`, `anio`, `temporada`,`ciudad`)
VALUES ( 1, '1992 Summer', 1992, 'Summer','Barcelona'), 
	( 2, '2012 Summer',2012, 'Summer', 'London'), 
    (3,'1920 Summer', 1920, 'Summer', 'Antwerpen' );


-- ------------------
-- Tabla `Evento`
-- --------------------

CREATE TABLE `Evento` (
	`id_evento` int(11) NOT NULL AUTO_INCREMENT,
	`nombre` varchar(150) NOT NULL,
	`id_olimpiada` int(11) NOT NULL,
	`id_deporte` int(11) NOT NULL,
	PRIMARY KEY (`id_evento`),
	CONSTRAINT `FK_Evento_Deporte` FOREIGN KEY (`id_deporte`) REFERENCES `Deporte` (`id_deporte`),
	CONSTRAINT `FK_Evento_Olimpiada` FOREIGN KEY (`id_olimpiada`) REFERENCES `Olimpiada` (`id_olimpiada`)
) ENGINE = InnoDB AUTO_INCREMENT = 10 DEFAULT CHARACTER SET = latin1 COLLATE = latin1_spanish_ci;


-- -------------------------
-- Tabla `Participacion`
-- -------------------------

CREATE TABLE `Participacion` (
	`id_deportista` int(11) NOT NULL,
	`id_evento` int(11) NOT NULL,
	`id_equipo` int(11) NOT NULL,
	`edad` tinyint(4) DEFAULT NULL,
	`medalla` varchar(6) DEFAULT NULL,
    PRIMARY KEY (`id_deportista`, `id_evento`),
	CONSTRAINT `FK_Participacion_Deportista` FOREIGN KEY (`id_deportista`) REFERENCES `Deportista` (`id_deportista`),
    CONSTRAINT `FK_Participacion_Equipo` FOREIGN KEY (`id_equipo`) REFERENCES `Equipo` (`id_equipo`),
    CONSTRAINT `FK_Participacion_Evento` FOREIGN KEY (`id_evento`) REFERENCES `Evento` (`id_evento`)
) ENGINE = InnoDB DEFAULT CHARACTER SET = latin1 COLLATE = latin1_spanish_ci;

COMMIT;
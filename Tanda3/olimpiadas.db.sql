BEGIN TRANSACTION;
DROP TABLE IF EXISTS `Participacion`;
CREATE TABLE IF NOT EXISTS `Participacion` (
	`id_deportista`	int ( 11 ) NOT NULL,
	`id_evento`	int ( 11 ) NOT NULL,
	`id_equipo`	int ( 11 ) NOT NULL,
	`edad`	tinyint ( 4 ) DEFAULT NULL,
	`medalla`	varchar ( 6 ) DEFAULT NULL,
	PRIMARY KEY(`id_deportista`,`id_evento`),
	FOREIGN KEY(`id_evento`) REFERENCES `Evento`(`id_evento`),
	FOREIGN KEY(`id_deportista`) REFERENCES `Deportista`(`id_deportista`)
);
DROP TABLE IF EXISTS `Olimpiada`;
CREATE TABLE IF NOT EXISTS `Olimpiada` (
	`id_olimpiada`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`nombre`	varchar ( 11 ) NOT NULL,
	`anio`	smallint ( 6 ) NOT NULL,
	`temporada`	varchar ( 6 ) NOT NULL,
	`ciudad`	varchar ( 50 ) NOT NULL
);
DROP TABLE IF EXISTS `Evento`;
CREATE TABLE IF NOT EXISTS `Evento` (
	`id_evento`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`nombre`	varchar ( 150 ) NOT NULL,
	`id_olimpiada`	int ( 11 ) NOT NULL,
	`id_deporte`	int ( 11 ) NOT NULL,
	FOREIGN KEY(`id_olimpiada`) REFERENCES `Olimpiada`(`id_olimpiada`)
);
DROP TABLE IF EXISTS `Equipo`;
CREATE TABLE IF NOT EXISTS `Equipo` (
	`id_equipo`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`nombre`	varchar ( 50 ) NOT NULL,
	`iniciales`	varchar ( 3 ) NOT NULL
);
DROP TABLE IF EXISTS `Deportista`;
CREATE TABLE IF NOT EXISTS `Deportista` (
	`id_deportista`	int ( 11 ) NOT NULL,
	`nombre`	varchar ( 150 ) NOT NULL,
	`sexo`	varchar ( 1 ) NOT NULL,
	`peso`	int ( 11 ) DEFAULT NULL,
	`altura`	int ( 11 ) DEFAULT NULL,
	PRIMARY KEY(`id_deportista`)
);
DROP TABLE IF EXISTS `Deporte`;
CREATE TABLE IF NOT EXISTS `Deporte` (
	`id_deporte`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`nombre`	varchar ( 100 ) NOT NULL
);
COMMIT;

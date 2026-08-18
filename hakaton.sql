CREATE DATABASE IF NOT EXISTS Hakaton;

USE Hakaton;

CREATE TABLE IF NOT EXISTS Usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS HistoricoConversas (
    id_conversa INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario_fk INT,
    horario DATETIME DEFAULT CURRENT_TIMESTAMP,
    mensagem_usuario TEXT,
    resposta_ia TEXT,
    FOREIGN KEY (id_usuario_fk) REFERENCES Usuarios(id_usuario)
);


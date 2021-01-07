create database if not exists master_python;

use master_python;

create table usuarios(
    id_usuarios  int auto_increment,
    primary key (id_usuarios),
    nombre varchar(100),
    apellidos varchar(255),
    email varchar(255) unique not null,
    password varchar(255) not null,
    fecha date not null

)ENGINE=InnoDb;

create table notas(
    id_notas int auto_increment not null,
    primary key (id_notas),
    id_usuarios int ,
    foreign key (id_usuarios) references usuarios(id_usuarios),
    titulo varchar(255) not null,
    descripcion mediumtext,
    fecha date not null

)ENGINE=InnoDb;

SELECT * FROM usuarios;


drop database if exists babykuna;

create database babykuna;
show databases;
use babykuna;

create table clients(
document_client int not null auto_increment primary key,
name_client varchar(40) not null,
surname_client varchar(50) not null,
adress varchar(100) not null,
city varchar(40) not null,
country varchar(30) not null,
phone varchar(20) not null,
email varchar(30) not null

);

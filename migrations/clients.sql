USE kuna_db;

CREATE TABLE clients (
  id_client INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(64) NOT NULL,
  last_name VARCHAR(64) NOT NULL,
  address_client VARCHAR(128) NOT NULL,
  zip_code VARCHAR(64) NOT NULL,
  city VARCHAR(32) NOT NULL,
  country VARCHAR(32) NOT NULL,
  phone VARCHAR(32) NOT NULL,
  email VARCHAR(64) NOT NULL
);

INSERT INTO clients (id_client, first_name, last_name, address_client, zip_code, city, country, phone, email) 
VALUES (1, 'Alberto', 'Mansilla Yanqui', 'Av Los Faisanes 1040, Santiago de Surco', 'L12', 'Lima','Peru', '987755267', 'mateplus.ciencias@gmail.com'); 

INSERT INTO clients (id_client, first_name, last_name, address_client, zip_code, city, country, phone, email) 
VALUES (2, 'Rosa', 'Mallqui Perez', 'Av Los Faisanes 1040, Santiago de Surco', 'L12', 'Lima','Peru', '922535040', 'rosamallquiperez@gmail.com');
USE kuna_db;

CREATE TABLE client (
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


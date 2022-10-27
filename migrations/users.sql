USE kuna_db;

CREATE TABLE client (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(64) NOT NULL,
  password_hash VARCHAR(64) NOT NULL,
  email VARCHAR(64) NOT NULL,
  country VARCHAR(64) NOT NULL,
  is_blocked BIT NOT NULL,
  is_approved BIT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
);

CREATE TABLE users {
    user_id int(11) AUTO_INCREMENT PRIMARY KEY not null,
    username varchar(255) not null,
    password varchar(255) not null,
    email varchar(255) not null,
};

INSERT INTO users (username, password, email) VALUES ('admin', 'admin', '', 'email');
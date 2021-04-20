DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS service;

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(24) UNIQUE NOT NULL,
    password VARCHAR(24) NOT NULL
);

CREATE TABLE service(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64) UNIQUE NOT NULL,
    email VARCHAR(60) NOT NULL,
    address VARCHAR(60),
    description TEXT
);

CREATE TABLE article(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_written DATETIME,
    author VARCHAR(60),
    source VARCHAR(24) NOT NULL,
    title VARCHAR(60) NOT NULL,
    right_bias INTEGER,
    left_bias INTEGER,
    content TEXT NOT NULL
);

CREATE TABLE comment(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article_id INTEGER NOT NULL,
    date DATETIME,
    user VARCHAR(60),
    right_bias INTEGER,
    left_bias INTEGER,
    content TEXT NOT NULL,
    FOREIGN KEY(article_id) REFERENCES article(id)
);

CREATE TABLE article_rating(
    item_id NOT NULL,
    username VARCHAR(24) NOT NULL,
    rated BOOLEAN,
    PRIMARY KEY(item_id, username),
    FOREIGN KEY(item_id) REFERENCES article(id),
    FOREIGN KEY(username) REFERENCES user(username)
);

CREATE TABLE comment_rating(
    item_id NOT NULL,
    username VARCHAR(24) NOT NULL,
    rated BOOLEAN,
    PRIMARY KEY(item_id, username),
    FOREIGN KEY(item_id) REFERENCES comment(id),
    FOREIGN KEY(username) REFERENCES user(username)
);
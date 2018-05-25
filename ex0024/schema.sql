drop table if exists guestbook;

create table user (
  id integer primary key autoincrement,
  username string not null,
  password string not null
);



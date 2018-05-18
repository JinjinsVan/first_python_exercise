drop table if exists guestbook;

create table user (
  id integer primary key autoincrement,
  username string not null,
  password string not null
);

create table tolist (
  id integer primary key autoincrement,
  title string not null,
  date string not null,
  status string not null,
  user_id integer not null
);


drop table if exists guestbook;
create table guestbook (
  id integer primary key autoincrement,
  username string not null,
  text string not null,
  timestr string not null
);
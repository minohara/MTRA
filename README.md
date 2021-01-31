# MTRA
Movie Theater Reservation Analyzer


## データベース ##

```puml
@startuml
entity "sample" <<データ取得>> {
  +id
  --
  time
}
entity "movie" <<映画>> {
  +id
  --
  title
}
entity "screening" <<上映回>> {
  +id
  --
  # movie_id (FK)
  # screen_id (FK)
  stat_time
  end_time
  url
}
entity "reservation" <<予約>> {
  +id
  --
  # sample_id (FK)
  # screening_id (FK)
  # seat_id (FK)
}
entity "screen" <<上映室>> {
  +id
  --
  name
}
entity "seat" <<座席>> {
  +id
  --
  #screen_id (FK)
  row
  column
  pos_x
  pos_y
  pos_z
}
sample --|{ reservation
movie --o{ screening
screen --|{ seat
screen --o{ screening
screening --|{ reservation
seat --|{ reservation
@enduml
```

```sql
create database `mtra`;

use `mtra`;

create table `sample`(
  `id` int auto_increment not null primary key,
  `time` datetime);

CREATE TABLE `movie` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin

create table `screen`(
  `id` int auto_increment not null primary key,
  `name` text not null);

CREATE TABLE `screening` (
  `id` int NOT NULL AUTO_INCREMENT,
  `movie_id` int NOT NULL,
  `screen_id` int NOT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `url` text,
  PRIMARY KEY (`id`),
  KEY `movie_id` (`movie_id`),
  KEY `screen_id` (`screen_id`),
  CONSTRAINT `screening_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`),
  CONSTRAINT `screening_ibfk_2` FOREIGN KEY (`screen_id`) REFERENCES `screen` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin

create table seat(
  `id` int auto_increment not null primary key,
  `screen_id` int not null,
  `row` char(2),
  `column` int,
  `pos_x` double,
  `pos_y` double,
  `pos_z` double,

  foreign key (`screen_id`)
  references `screen`(`id`));

create table `reservation`(
  `id` bigint auto_increment not null primary key,
  `sample_id` int,
  `screening_id` int,
  `seat_id` int,

  foreign key(`sample_id`)
  references `sample`(`id`),

  foreign key(`screening_id`)
  references `screening`(`id`),

  foreign key(`seat_id`)
  references `seat`(`id`));

insert into screen(name) values ("a studio");

insert into seat(`screen_id`, `row`, `column`, `pos_x`, `pos_y`, `pos_z`) values (1, "B",  5, -13,   1,   0);

```

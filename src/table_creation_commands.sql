create database youtube_database;

use youtube_database;

create table playlist_urls (
	id int primary key auto_increment,
	playlist_name varchar(100),
	playlist_URL varchar(100)
);

create table video_urls (
	id int primary key auto_increment,
	playlist_id int,
	yt_video_id varchar(100),
	video_name varchar(100),
	video_URL varchar(100),
	foreign key (playlist_id) references playlist_urls(id) ON DELETE CASCADE
);

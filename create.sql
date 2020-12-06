-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2020-12-06 00:46:23.497

-- tables
-- Table: Album
CREATE TABLE Album (
    album_id serial  NOT NULL,
    album_name text  NOT NULL,
    release_date date  NOT NULL,
    CONSTRAINT Album_pk PRIMARY KEY (album_id)
);

-- Table: Artist
CREATE TABLE Artist (
    username text  NOT NULL,
    biography text  NOT NULL,
    CONSTRAINT Artist_pk PRIMARY KEY (username)
);

-- Table: Contains
CREATE TABLE Contains (
    playlist_id int  NOT NULL,
    song_id int  NOT NULL,
    CONSTRAINT Contains_pk PRIMARY KEY (playlist_id,song_id)
);

-- Table: Episode
CREATE TABLE Episode (
    episode_id serial  NOT NULL,
    episode_name text  NOT NULL,
    release_date date  NOT NULL,
    runtime int  NOT NULL,
    summary text  NOT NULL,
    podcast_id int  NOT NULL,
    CONSTRAINT Episode_pk PRIMARY KEY (episode_id)
);

-- Table: Listen_Episode
CREATE TABLE Listen_Episode (
    username text  NOT NULL,
    listened_timestamp timestamp  NOT NULL,
    listened_duration int  NOT NULL,
    episode_id int  NOT NULL,
    CONSTRAINT Listen_Episode_pk PRIMARY KEY (username,episode_id)
);

-- Table: Listen_Song
CREATE TABLE Listen_Song (
    username text  NOT NULL,
    listened_timestamp timestamp  NOT NULL,
    listened_duration int  NOT NULL,
    song_id int  NOT NULL,
    CONSTRAINT Listen_Song_pk PRIMARY KEY (username,song_id)
);

-- Table: Listener
CREATE TABLE Listener (
    username text  NOT NULL,
    card_number int  NOT NULL,
    is_premium boolean  NOT NULL,
    CONSTRAINT Listener_pk PRIMARY KEY (username)
);

-- Table: Playlist
CREATE TABLE Playlist (
    playlist_id serial  NOT NULL,
    title text  NOT NULL,
    username text  NOT NULL,
    CONSTRAINT Playlist_pk PRIMARY KEY (playlist_id)
);

-- Table: Podcast
CREATE TABLE Podcast (
    podcast_id serial  NOT NULL,
    podcast_name text  NOT NULL,
    summary text  NOT NULL,
    username text  NOT NULL,
    CONSTRAINT Podcast_pk PRIMARY KEY (podcast_id)
);

-- Table: Podcaster
CREATE TABLE Podcaster (
    username text  NOT NULL,
    CONSTRAINT Podcaster_pk PRIMARY KEY (username)
);

-- Table: Releases
CREATE TABLE Releases (
    username text  NOT NULL,
    album_id int  NOT NULL,
    CONSTRAINT Releases_pk PRIMARY KEY (username,album_id)
);

-- Table: Song
CREATE TABLE Song (
    song_id serial  NOT NULL,
    song_name text  NOT NULL,
    release_date date  NOT NULL,
    runtime int  NOT NULL,
    genre text  NOT NULL,
    lyrics text  NOT NULL,
    album_id int  NOT NULL,
    CONSTRAINT Song_pk PRIMARY KEY (song_id)
);

-- Table: User
CREATE TABLE "User" (
    username text  NOT NULL,
    first_name text  NOT NULL,
    last_name text  NOT NULL,
    email text  NOT NULL,
    region text  NOT NULL,
    CONSTRAINT User_pk PRIMARY KEY (username)
);

-- foreign keys
-- Reference: Album_Releases (table: Releases)
ALTER TABLE Releases ADD CONSTRAINT Album_Releases
    FOREIGN KEY (album_id)
    REFERENCES Album (album_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Album_Song (table: Song)
ALTER TABLE Song ADD CONSTRAINT Album_Song
    FOREIGN KEY (album_id)
    REFERENCES Album (album_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Contains_Playlist (table: Contains)
ALTER TABLE Contains ADD CONSTRAINT Contains_Playlist
    FOREIGN KEY (playlist_id)
    REFERENCES Playlist (playlist_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Episode_Listen_Episode (table: Listen_Episode)
ALTER TABLE Listen_Episode ADD CONSTRAINT Episode_Listen_Episode
    FOREIGN KEY (episode_id)
    REFERENCES Episode (episode_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Episode_Podcast (table: Episode)
ALTER TABLE Episode ADD CONSTRAINT Episode_Podcast
    FOREIGN KEY (podcast_id)
    REFERENCES Podcast (podcast_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Listen_Episode_Listener (table: Listen_Episode)
ALTER TABLE Listen_Episode ADD CONSTRAINT Listen_Episode_Listener
    FOREIGN KEY (username)
    REFERENCES Listener (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Listener_Listen_Song (table: Listen_Song)
ALTER TABLE Listen_Song ADD CONSTRAINT Listener_Listen_Song
    FOREIGN KEY (username)
    REFERENCES Listener (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Listener_User (table: Listener)
ALTER TABLE Listener ADD CONSTRAINT Listener_User
    FOREIGN KEY (username)
    REFERENCES "User" (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Playlist_Listener (table: Playlist)
ALTER TABLE Playlist ADD CONSTRAINT Playlist_Listener
    FOREIGN KEY (username)
    REFERENCES Listener (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Podcast_Podcaster (table: Podcast)
ALTER TABLE Podcast ADD CONSTRAINT Podcast_Podcaster
    FOREIGN KEY (username)
    REFERENCES Podcaster (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Podcaster_User (table: Podcaster)
ALTER TABLE Podcaster ADD CONSTRAINT Podcaster_User
    FOREIGN KEY (username)
    REFERENCES "User" (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Releases_Artist (table: Releases)
ALTER TABLE Releases ADD CONSTRAINT Releases_Artist
    FOREIGN KEY (username)
    REFERENCES Artist (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Song_Contains (table: Contains)
ALTER TABLE Contains ADD CONSTRAINT Song_Contains
    FOREIGN KEY (song_id)
    REFERENCES Song (song_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Song_Listen_Song (table: Listen_Song)
ALTER TABLE Listen_Song ADD CONSTRAINT Song_Listen_Song
    FOREIGN KEY (song_id)
    REFERENCES Song (song_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Artist (table: Artist)
ALTER TABLE Artist ADD CONSTRAINT User_Artist
    FOREIGN KEY (username)
    REFERENCES "User" (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.


\c postgres
DROP DATABASE IF EXISTS spotify;

CREATE database spotify;
\c spotify

\i create.SQL

\copy "User"(username,first_name,last_name,email,region) FROM 'csv/user.csv' csv header
\copy Artist(username,biography) FROM 'csv/artist.csv' csv header
\copy Listener(username,card_number,is_premium) FROM 'csv/listener.csv' csv header 
\copy Podcaster(username) FROM 'csv/podcaster.csv' csv header 
\copy Album(album_name,release_date) FROM 'csv/album.csv' csv header
\copy Album_Upload(username,album_id) FROM 'csv/album_upload.csv' csv header 
\copy Song(song_name,release_date,runtime,genre,lyrics,album_id) FROM 'csv/song.csv' csv header 
\copy Playlist(playlist_id,title,username) FROM 'csv/playlist.csv' csv header 
\copy Playlist_Contains(playlist_id,song_id) FROM 'csv/playlist_contains.csv' csv header
\copy Podcast(podcast_name,summary,username) FROM 'csv/podcast.csv' csv header
\copy Episode(episode_name,release_date,runtime,summary,podcast_id) FROM 'csv/episode.csv' csv header
\copy Listen_Episode(username,listened_timestamp,listened_duration,episode_id) FROM 'csv/listen_episode.csv' csv header
\copy Listen_Song(username,listened_timestamp,listened_duration,song_id) FROM 'csv/listen_song.csv' csv header


\copy Album(album_id,album_name,release_date) FROM 'album.csv' csv header
\copy Artist(username,biography) FROM 'artist.csv' csv header
\copy Contains(playlist_id,song_id) FROM 'contains.csv' csv header
\copy Episode(episode_id,episode_name,release_date,runtime,summary,podcast_id) FROM 'episode.csv' csv header
\copy Listen_Episode(username,listened_timestamp,listened_duration,episode_id) FROM 'listen_episode.csv' csv header
\copy Listen_Song(username,listened_timestamp,listened_duration,song_id) FROM 'listen_song.csv' csv header
\copy Listener(username,card_number,is_premium) FROM 'listener.csv' csv header 
\copy Playlist(playlist_id,title,username) FROM 'playlist.csv' csv header 
\copy Podcast(podcast_id,podcast_name,summary,username) FROM 'podcast.csv' csv header
\copy Podcaster(username) FROM 'podcaster.csv' csv header 
\copy Releases(username,album_id) FROM 'releases.csv' csv header 
\copy Song(song_id,song_name,release_date,runtime,genre,lyrics,album_id) FROM 'song.csv' csv header 
\copy User(username,first_name,last_name,email,region) FROM 'user.csv' csv header
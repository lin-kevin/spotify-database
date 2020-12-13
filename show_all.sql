\c spotify

\echo Album_Upload: Keeps track of the username of the artist corresponding to each album id
SELECT * FROM Album_Upload;

\echo Album: Keeps track of the name and release date corresponding to the album id
SELECT * FROM Album;

\echo Artist: Keeps track of biography corresponding to each artist username
SELECT * FROM Artist;

\echo Episode: Associates an episode_id with each episode, containing information such as, the episode name, release date, runtime, summary, and the podcast id the episode is for
SELECT * FROM Episode;

\echo Listen_Episode: Keeps track of each time a user listens to an episode and for how long and when they listened to it
SELECT * FROM Listen_Episode;

\echo Listen_Song: Keeps track of each time a user listens to a song and for how long and when they listened to it
SELECT * FROM Listen_Song;

\echo Listener: Keeps track of the card number and if the user associated with a username is a premium member, card_number=-1 if they are not a premium memeber
SELECT * FROM Listener;

\echo Playlist_Contains: Keeps track of which song ids are in which playlists with the corresponding playlist id
SELECT * FROM Playlist_Contains;

\echo Playlist: Keeps track of which user owns which playlist and the playlist title corresponding to the playlist id
SELECT * FROM Playlist;

\echo Podcast: Keeps track of the username, podcast name, and summary for each podcast and uniquely identifies it with the podcast id
SELECT * FROM Podcast;

\echo Podcaster: Keeps track of which users are podcasters by their username
SELECT * FROM Podcaster;

\echo Song: Keeps track of the song name, release date, runtime, genre, lyrics, album_id for each song and uniquely identifies it with a song id
SELECT * FROM Song;

\echo "User": Keeps track of the username, first name, last name, email, and region of each Spotify user
SELECT * FROM "User";
import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

print ("As a listener, I want to search for playlists with my favorite artist’s songs inside.")

artist = input("Please enter your favorite artist's username: ")

def query(artist):
  tmp = '''
    DROP TABLE IF EXISTS Artist_Album CASCADE;
    CREATE TABLE Artist_Album AS 
          (SELECT * 
            FROM Album_Upload 
            WHERE username = %s);

    DROP TABLE IF EXISTS Songs_From_Albums CASCADE;
    CREATE TABLE Songs_From_Albums AS 
          (SELECT * 
            FROM Song AS s
            WHERE s.album_id IN (SELECT aa.album_id 
                                FROM Artist_Album AS aa));

    SELECT DISTINCT p.title
      FROM Playlist AS p
           JOIN Playlist_Contains AS pc ON p.playlist_id = pc.playlist_id
     WHERE pc.song_id IN (SELECT sfa.song_id 
                            FROM Songs_From_Albums AS sfa);
  '''
  cmd = cur.mogrify(tmp, (artist, ))
  cur.execute(cmd)
  rows = cur.fetchall()
  print("\nPlaylists with your favorite artists are: ")
  for row in rows:
    print(row[0])

query(artist)
    

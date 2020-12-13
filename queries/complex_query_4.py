import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

def query(username):
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

  cmd = cur.mogrify(tmp, (username,))
  cur.execute(cmd)
  rows = cur.fetchall()

  for row in rows:
    print(row[0])

def main():
  print("US7: As an artist, I want to see which playlists my songs are in so that I know what type of music my songs are being grouped into.")

  username = input("Please enter your username: ")

  query(username)
    
if __name__ == "__main__":
    main()
    

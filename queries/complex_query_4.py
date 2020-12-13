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

    DROP TABLE IF EXISTS Artist_Listeners CASCADE;
    CREATE TABLE Artist_Listeners AS 
          (SELECT * 
            FROM Listen_Song 
            WHERE song_id IN (SELECT sfa.song_id
                                FROM Songs_From_Albums AS sfa));
    

    SELECT DISTINCT p.podcast_name
      FROM Artist_Listeners AS al
            JOIN Listen_Episode AS le ON le.username = al.username
            JOIN Episode AS e ON e.episode_id = le.episode_id
            JOIN Podcast AS p ON p.podcast_id = e.podcast_id;
  '''

  cmd = cur.mogrify(tmp, (username,))
  cur.execute(cmd)
  rows = cur.fetchall()

  for row in rows:
    print(row[0])

def main():
  print("US7: As an artist, I want to see which podcasts my listeners listen to so that I know what else they’re interested in.")

  username = input("Please enter your username: ")

  query(username)
    
if __name__ == "__main__":
    main()
    

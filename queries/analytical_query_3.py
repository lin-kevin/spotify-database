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

    SELECT u.region, COUNT(DISTINCT al.username)
      FROM Artist_Listeners AS al
           JOIN "User" AS u ON al.username = u.username
     GROUP BY u.region
     ORDER BY COUNT(DISTINCT al.username) DESC;
  '''

  cmd = cur.mogrify(tmp, (username, ))
  cur.execute(cmd)
  rows = cur.fetchall()
  print("\nYour listeners are from: ")
  for row in rows:
    print(row)

def main():
  print("US10: As an artist, I want to see how many people listened to my songs in each region so that I can see how broad my global fanbase is.")

  username = input("Please enter your username: ")

  query(username)

if __name__ == "__main__":
    main()

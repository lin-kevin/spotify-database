import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

print ("As an artist, I want to see what other songs my listeners listen to so that I can create music tailored to their liking.")

username = input("Please enter your username: ")

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
       FROM Song
      WHERE album_id IN 
      (SELECT aa.album_id 
         FROM Artist_Album AS aa););
    
    DROP TABLE IF EXISTS Artist_Listeners CASCADE;
    CREATE TABLE Artist_Listeners AS 
    (SELECT * 
       FROM Listen_Song 
      WHERE song_id IN 
      (SELECT sfa.song_id
         FROM Songs_From_Albums AS sfa););
    
    SELECT s.song_name 
      FROM Artist_Listeners AS al 
      JOIN Song AS s ON al.song_id = s.song_id 
     WHERE s.song_id NOT IN 
          (SELECT sfa.song_id
         FROM Songs_From_Albums AS sfa);
  '''

  cur.execute(cmd)
  rows = cur.fetchall()
  print("The other songs your listeners listen to include: \n")
  for row in rows:
    print(row)

query(username)
    
import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

print("US3: As a listener, I want to find the title of song I am listening to on the radio using the lyrics of the song so that I can listen to it later on.")

lyrics = input("Please enter the lyrics you detected: ")

def query(lyrics):
  tmp = '''
    SELECT song_name
      FROM Song 
     WHERE lyrics ILIKE %s
  '''
  cmd = cur.mogrify(tmp, ('%' + lyrics + '%',))
  cur.execute(cmd)
  rows = cur.fetchall()
  print("\n")
  print("The title(s) of the song you're looking for could be ")
  for row in rows:
    print(row[0])

query(lyrics)
    
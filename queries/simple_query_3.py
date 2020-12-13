import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

def query(lyrics):
  tmp = '''
    SELECT song_name
      FROM Song 
     WHERE lyrics ILIKE %s
  '''
  cmd = cur.mogrify(tmp, ('%' + lyrics + '%',))
  cur.execute(cmd)
  rows = cur.fetchall()
  print("The title(s) of the song you're looking for could be ")
  for row in rows:
    print(row[0])
    
def main():
  print("US3: As a listener, I want to find the title of song I am listening to on the radio using the lyrics of the song so that I can listen to it later on.")

  lyrics = input("Please enter the lyrics you detected: ")

  print("\nGetting Song table...")
  print("Filter table for songs with lyrics that have '"+lyrics+"' in them...")
  print("Getting song_names...\n")

  query(lyrics)

if __name__ == "__main__":
    main()
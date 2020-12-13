import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

def query(username):
  tmp = '''
    SELECT s.song_name
      FROM Song AS s
           JOIN Listen_Song AS ls ON s.song_id=ls.song_id
     WHERE ls.username = %s AND YEAR(listened_timestamp) = 2020
     GROUP BY s.song_id 
     ORDER BY COUNT(s.song_id) DESC
     LIMIT 5;
  '''

  cmd = cur.mogrify(tmp, (username, ))
  cur.execute(cmd)
  rows = cur.fetchall()
  print("\nYour top 5 songs of 2020 are: ")
  for row in rows:
    print(row[0])

def main():
  print("US9: As a listener I want to see the 5 songs I listened to the most in 2020 so that I can share my music taste with my Instagram followers.")

  username = input("Please enter your username: ")

  print("\nGetting all the songs you listened to in 2020...")
  print("Counting the number of times you listened to each song...")
  print("Finding the 5 songs you listned to most...\n")

  query(username)

if __name__ == "__main__":
    main()

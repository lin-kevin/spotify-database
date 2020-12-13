import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

def query(username, podcast_name, summary):
  tmp = '''
    INSERT INTO Podcast (username, podcast_name, summary)
    VALUES (%s, %s, %s)
  '''
  cmd = cur.mogrify(tmp, (username, podcast_name, summary))
  cur.execute(cmd)
  print("Your podcast " + podcast_name + " is now on Spotify!")


    

def main():
  print("US2: As a podcaster I want to upload my podcasts so that people can listen to what interests me.")

  username = input("Please enter your username: ")
  podcast_name = input("Please enter your podcast's name: ")
  summary = input("Please enter a summary of your podcast: ")

  query(username, podcast_name, summary)

if __name__ == "__main__":
    main()
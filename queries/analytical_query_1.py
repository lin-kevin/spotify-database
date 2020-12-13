import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

def query(username):
  tmp = '''
    DROP TABLE IF EXISTS Podcasters_Podcasts CASCADE;
    CREATE TABLE Podcasters_Podcasts AS 
    (SELECT * 
       FROM Podcast
      WHERE username = %s);

    DROP TABLE IF EXISTS Podcasters_Episodes CASCADE;
    CREATE TABLE Podcasters_Episodes AS 
    (SELECT * 
       FROM Episode 
      WHERE podcast_id IN 
      (SELECT pp.podcast_id 
         FROM Podcasters_Podcasts AS pp));
    
    DROP TABLE IF EXISTS Listened_Episodes CASCADE;
    CREATE TABLE Listened_Episodes AS 
    (SELECT * 
       FROM Listen_Episode
      WHERE episode_id IN 
    (SELECT pe.episode_id
       FROM Podcasters_Episodes AS pe));
    
    SELECT AVG(listened_duration)
      FROM Listened_Episodes
  '''

  cmd = cur.mogrify(tmp, (username, ))
  cur.execute(cmd)
  rows = cur.fetchall()
  print("The average listening time of your podcasts is ")
  for row in rows:
    print(str(round(row[0], 2)) + " seconds")

def main():
  print("US8: As a podcaster, I want to find the average listening time of my podcasts' episodes so that I can see how engaged my audience is.")

  username = input("Please enter your username: ")

  print("\nGetting podcasts uploaded by podcaster with username=" + username + "...")
  print("\nGetting podcast episodes uploaded by this podcaster...")
  print("\nFinding all listening times of this podcaster's edpisodes...")
  print("\nClaculating the average listening time of this podcaster's episdoes...\n")

  query(username)

if __name__ == "__main__":
    main()

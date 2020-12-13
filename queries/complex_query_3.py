import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

def query(username, podcaster):
  tmp = '''
    DROP TABLE IF EXISTS Episodes_From_Podcaster;
    CREATE TABLE Episodes_From_Podcaster AS 
           (SELECT e.episode_name, e.episode_id
              FROM Podcast AS p
                   JOIN Episode AS e ON p.podcast_id = e.podcast_id
             WHERE p.username = %s);
    
    DROP TABLE IF EXISTS Users_Episodes;
    CREATE TABLE Users_Episodes AS 
          (SELECT episode_id
             FROM Listen_episode
            WHERE username = %s);
    
    SELECT episode_name
      FROM Episodes_From_Podcaster
     WHERE episode_id NOT IN (SELECT * FROM Users_Episodes);
  '''
  cmd = cur.mogrify(tmp, (podcaster,username))
  cur.execute(cmd)
  rows = cur.fetchall()
  if len(rows) == 0:
      print("\nYou have listened to all their podcasts!")
      return;
  print("\nEpisodes you have not listened to from the podcaster are: ")
  for row in rows:
    print(row[0])

def main():
  print("US6: As a listener, I want to see the episodes I have not listened to from a certain podcaster so that I find new episodes to listen to.")

  username = input("Please enter your username: ")
  podcaster = input("Please enter the podcasters username: ")

  print("\nGetting all the episode names and ids where the podcaster username="+podcaster+"...")
  print("Getting all the episode ids where username="+username+" has listened to...")
  print("Selecting all the episode names username="+username+" has not listened to...\n")

  query(username, podcaster)
    
if __name__ == "__main__":
    main()
    

import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

print("As a listener, I want to see the episodes I have not listened to from a certain podcaster so that I find new episodes to listen to.")

username = input("Please enter your username: ")
podcaster = input("Please enter the podcasters username: ")

def query(username, podcaster):
  tmp = '''

  '''
  cmd = cur.mogrify(tmp, (podcaster,username))
  cur.execute(cmd)
  rows = cur.fetchall()

  print("\nEpisodes you have not listened to from the podcaster are: ")
  for row in rows:
    print(row[0])

query(username, podcaster)
    

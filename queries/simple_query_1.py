import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

print("As a listener, I want to buy a premium subscription so that I can avoid ads when listening to music.")

username = input("Please enter your username: ")
card_number = input("Please enter your card number: ")

def query(username):
  tmp = '''
    UPDATE Listener
       SET is_premium = TRUE, card_number = %d
     WHERE username = %s
  '''
  cmd = cur.mogrify(tmp, (card_number, username))
  cur.execute(cmd)
  print(username + " is now a premium Spotify user!")

query(username)
    
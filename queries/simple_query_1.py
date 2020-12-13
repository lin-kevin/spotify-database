import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

def query(username, card_number):
  tmp = '''
    UPDATE Listener
       SET is_premium = TRUE, card_number = %s
     WHERE username = %s
  '''
  cmd = cur.mogrify(tmp, (int(card_number), username))

  cur.execute(cmd)
  print(username + " is now a premium Spotify user!")

def main():
  print("US1: As a listener, I want to buy a premium subscription so that I can avoid ads when listening to music.")

  username = input("Please enter your username: ")
  card_number = input("Please enter your card number: ")

  print("\nUpdating Listener Table...")
  print("Getting user with username="+username+"...")
  print("Setting is_premium to TRUE and setting card_number to "+card_number+"...\n")

  query(username, card_number)

if __name__ == "__main__":
    main()
    
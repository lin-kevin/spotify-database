import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

print ("As a listener, I want to search for playlists with my favorite artist’s songs inside.")


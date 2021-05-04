import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''') #Triple quotes are only to make it easier to read,
#can use any quote '' or "" or '''

cur.execute('''
CREATE TABLE Counts(email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1: fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    peices = line.split()
    email = peices[1]                                           #Python syntax!
    cur.execute('SELECT count FROM Counts Where email = ? ',(email,))#this is a
    #the ? is a place holder, it allows to avoid SQL injection       tuple with
    row = cur.fetchone()                                        #one item in it!
    if row is None:
        cur.execute('''INSERT INTO Counts (email,count)
            VALUES ( ?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
        (email,))
    conn.commit()
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()

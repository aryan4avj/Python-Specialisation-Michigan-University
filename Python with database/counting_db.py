import sqlite3
import re

conn = sqlite3.connect('emaidb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'Python with database\mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    # print(pieces[1])
    x = re.split('@([^ ]*)',pieces[1])
    # line = line.rstrip()
    # x = re.findall('@([^ ]*)',line)
    # print(x[1])
    org = x[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    # count += 1
conn.commit()
# print(count)


sqlstr = 'SELECT * FROM Counts'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)
''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'text'
fh = open(fname)
data = dict()
for line in fh:
    if line.strip().startswith('From: '):
        domain = str(line.strip().split('@')[1])
        if domain in data:
            data[domain] = data[domain] + 1
        else:
            data[domain] = 1

for key, value in data.items():
    cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, ?)''', (key,value))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
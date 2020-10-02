import sqlite3

conn = sqlite3.connect("py4eDB2.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')


fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith("From: "):  continue
    tmp_str1 = line.split()
    domain = tmp_str1[1].split("@")
    # print(domain[1])   #just a debug code
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain[1],))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org,count) VALUES (?,1) ''', (domain[1],))
    else:
        cur.execute('''UPDATE Counts SET count=count+1 WHERE org=?''',(domain[1],))
conn.commit()


sql1 = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sql1):
    print(str(row[0])," ------> ",row[1])



cur.close()    

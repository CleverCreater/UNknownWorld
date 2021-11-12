import sqlite3

main = sqlite3.connect('../main.db')
cursor = main.cursor()
try:
    cursor.execute(
        'create table players (id int(8), name varchar(30), '
        'nation varchar(20), level int(8))'
    )
except sqlite3.OperationalError:
    pass
cursor.close()
main.commit()
main.close()

import sqlite3
import os

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
os.system('cd ../forge-1.17.1-37.0.109-mdk')
os.system('./gradlew setupDecompWorkspace')

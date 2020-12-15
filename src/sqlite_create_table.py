import sqlite3

def table_init(connection, cursor):
    try :
        cursor.execute('DROP TABLE IF EXISTS users')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name VARCHAR, age INTEGER)
        '''
        )
    except sqlite3.Error as e:
        print('error occurred:', e.args[0])

def insert_data(connection, cursor):
    try :
        cursor.execute("INSERT INTO users VALUES(1, '田中', 20)")
        cursor.execute("INSERT INTO users VALUES(2, '宮本', 30)")
        cursor.execute("INSERT INTO users VALUES(3, 'かとう', ?)", (34,))
        cursor.execute("INSERT INTO users VALUES(?, ?, ?)", (4, 'きむら', 40))
        cursor.execute("INSERT INTO users VALUES(:id, :name, :age)"
                        ,{'id' : 5, 'name' : 'スズキ', 'age' : 40}
                    )
        many_users = [
            (6, '石田', 10),
            (7, 'ともり', 11),
            (8, '遠藤', 12)
        ]
        cursor.executemany('INSERT INTO users values(?,?,?)', many_users)
        connection.commit()
        cursor.execute("INSERT INTO users VALUES(1, '田中', 20)")
    except sqlite3.Error as e:
        print('error occurred:', e.args[0])

def fetch_data(connection, cursor):
    cursor.execute("select * from users")
    row = cursor.fetchone();
    print(row)
    row = cursor.fetchone();
    print(row)
    rows = cursor.fetchall()
    print(rows)


def main():
    connection = sqlite3.connect('../db/sample1.db')
    cursor = connection.cursor()
    table_init(connection, cursor)
    insert_data(connection, cursor)
    fetch_data(connection, cursor)
    connection.close()

if __name__ == '__main__':
    main()
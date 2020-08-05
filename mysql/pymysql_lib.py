import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='kbank',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_table():

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "CREATE TABLE users (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(30), account_no VARCHAR(12), age INT(3), balance int(20));"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        

    finally:
        print("Successfully created Database..!!")
        # connection.close()

    return True

def create_logs_table():

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = " create table transaction_logs (transaction_id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, sender_id INT(4), FOREIGN KEY (sender_id) references users(id), reciever_id INT(4), FOREIGN KEY (reciever_id) references users(id), amount int(20),type VARCHAR(10),  transaction_date date, comment varchar (100));"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        

    finally:
        print("Successfully created Database..!!")
        # connection.close()

    return True


def add_user(name, age, password, acct_no):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO users (name, age, password, account_no, balance) VALUES('{name}', {age}, '{password}', '{acct_no}', 0);"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        print("Successfully Added User..!!")

def fetch_user_details(name):

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"SELECT id, name, password, balance FROM users WHERE name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()

        return data

    finally:
        print("Successfully fetched.!!")
        # connection.close()


def get_balance(name):

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"SELECT balance FROM users WHERE name = '{name}';"
            cursor.execute(sql)
        data = cursor.fetchall()
        return data

    finally:
        print("Successfully fetched.!!")


def alter_balance(name, balance):

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"UPDATE users SET balance = {balance} where name = '{name}'"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        print("Successfully updated User balance..!!")
        # connection.close()


def create_log(sender, reciever, amount, comment, type):
    try:
        with connection.cursor() as cursor:
            # Create a new record

            sender_id = fetch_user_details(sender)[0]['id']
            reciever_id = fetch_user_details(reciever)[0]['id']

            sql = f"INSERT INTO transaction_logs (sender_id, reciever_id, amount,  transaction_date , comment, type ) VALUES('{sender_id}', '{reciever_id}', {amount}, '2020-10-02', '{comment}', '{type}');"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        print("Successfully Logged Transaction..!!")

def get_transaction_log():

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"""SELECT T.sender as sender, users.name as reciever, T.type, T.amount, T.comment from 
                        (SELECT users.name as sender , transaction_logs.amount, transaction_logs.comment, transaction_logs.type, reciever_id FROM transaction_logs
                        inner JOIN users on transaction_logs.sender_id = users.id) as T
                        JOIN users
                        ON users.id = T.reciever_id"""
            cursor.execute(sql)
        data = cursor.fetchall()
        return data

    finally:
        print("Successfully fetched.!!")
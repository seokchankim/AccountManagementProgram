import sys;
import uuid;
import mysql.connector;
import json;

def load_db_info():
    with open("./config/dbInfo.json") as file:
        db_info = json.load(file);

    return db_info;

def connect_mysql(host, port, db, user, pw):
    conn = mysql.connector.connect(host=host,
                                   port=port,
                                   database=db,
                                   user=user,
                                   password=pw);

    return conn;

def show_all(host, port, db, user, pw):
    con = mysql.connector.connect(host=host,
                                  port=port,
                                  database=db,
                                  user=user,
                                  password=pw);

    cursor = con.cursor(dictionary=True); # True로 해야 row에서 column 이름으로 값을 불러올 수 있다.

    sql=f"SELECT * FROM tb_account;";

    cursor.execute(sql);

    i = 1;

    for row in cursor:
        print(f"[{i}] SITE : {str(row['site'])}, account : {str(row['account_acc_id'])}, password : {str(row['account_pw'])}, PK : {str(row['account_id'])}");
        i += 1;

    cursor.close();

def create_cursor(connection):
    return connection.cursor(dictionary=True);

def close_connect(connection):
    connection.close();

def gen_uuid32():
    return str(uuid.uuid4()).replace("-","");

def add_account(site, acc_id, acc_pw):
    db_info = load_db_info();

    conn = connect_mysql(db_info['host'], db_info['port'], db_info['database'],
                         db_info['user'], db_info['password']);
    cursor = create_cursor(conn);

    query = "insert into tb_account(account_id, site, account_acc_id, account_pw) values (%s, %s, %s, %s);";

    values = (gen_uuid32(), site, acc_id, acc_pw);

    cursor.execute(query, values);

    conn.commit();

    close_connect(cursor);
    close_connect(conn);

def main():
    args = sys.argv;

    if len(args) == 4:
        site = args[1];
        account = args[2];
        pw = args[3];

        add_account(site, account, pw);

        db_info = load_db_info();

        show_all(db_info['host'], db_info['port'], db_info['database'],
                 db_info['user'], db_info['password']);
    else:
        print("Args : 1 [site] / 2 [acc_id] / 3 [acc_pw] !!");
        print(">>>> Example : python addAccount.py github acc_id acc_pw");

        db_info = load_db_info();

        show_all(db_info['host'], db_info['port'], db_info['database'],
                 db_info['user'], db_info['password']);

if __name__ == "__main__":
    main();
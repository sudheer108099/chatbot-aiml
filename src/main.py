import aiml
import os.path as path
import sqlite3 as sq

SCHEMA = [
    """create table if not exists User (
        id INTEGER PRIMARY KEY NOT NULL,
        name TEXT,
        address TEXT,
        phone TEXT
    );""",
    """CREATE TABLE IF NOT EXISTS Contacts (
        patient INT ,
        name TEXT,
        phone TEXT UNIQUE,
        relation TEXT,
        FOREIGN KEY(patient) REFERENCES User(id)
    );""",
    """create table if not exists Converstation (
        user_req TEXT,
        bot_reply TEXT
    );""",
]

DB_FILE = "db.sqlite3"
DATABASE = sq.connect(DB_FILE)


def create_account():
    """Create a new user account. Asks for a bunch of info and puts it in relevant tables."""
    name = ''
    while not name:
        name = input("What's your name? ")
    address = ''
    while not address:
        address = input("What's your address? ")
    contact = input("What's your phone? ")
    family = []
    while True:
        if input("Do you want to add family contact? ") == 'y':
            family_name = input("Name of your family member? ")
            relation = input("Who is this person to you? ")
            fam_contact = input("What is the person's phone number? ")
            family.append((family_name, relation, fam_contact))
        else:
            break
    sql = "INSERT INTO User (name, address, phone) VALUES (?, ?, ?);"
    cursor = DATABASE.cursor()
    cursor.execute(sql, (name, address, contact))
    id_ = cursor.lastrowid
    sql = "INSERT INTO Contacts (patient, name, relation, phone) VALUES (?, ?, ?, ?);"
    cursor.executemany(sql, [(id_, *i) for i in family])
    DATABASE.commit()


def init():
    cursor = DATABASE.cursor()
    for schema in SCHEMA:
        cursor = cursor.execute(schema)
    cursor.execute("INSERT OR REPLACE INTO User VALUES (0, NULL, NULL, NULL)")
    cursor.execute(
        "INSERT OR REPLACE INTO Contacts VALUES (0, 'Police', '100', 'Policia')"
    )
    cursor.execute(
        "INSERT OR REPLACE INTO Contacts VALUES (0, 'Ambulance', '102', 'Save ME!')"
    )
    cursor.execute(
        "INSERT OR REPLACE INTO Contacts VALUES (0, 'Fire Brigade', '101', 'Fire Fire!')"
    )
    DATABASE.commit()


if __name__ == '__main__':
    init()
    kernel = aiml.Kernel()
    kernel.setTextEncoding(None)

    if path.exists(brain := path.join('botz', 'brain')):
        kernel.bootstrap(brainFile=brain)
    else:
        kernel.bootstrap(learnFiles='startup.xml',
                         commands='LOAD AIML B',
                         chdir=f"{aiml.__path__[0]}/botdata/standard")
    inp = 'hello'
    for _ in range(7):
        bot_res = kernel.respond(inp)
        data = kernel.getSessionData(kernel._globalSessionID)
        print('DATA::', data)
        print('<<<', bot_res)
        inp = input('>>> ')
    kernel.saveBrain('botz/brain')
    # kernel.bootstrap(learnFiles="startup.xml",
    #                  commands="LOAD AIML B",
    #                  chdir=f"{aiml.__path__[0]}/botdata/standard")

    # ans = input(
    #     "Would you like to login or create a new account?\nType 'create' to create and any other key to exit\n"
    # )
    # if ans == 'create':
    #     create_account()

    # while True:
    #     user = input(">>> ")
    #     if user == 'q' or user == 'quit':
    #         break
    #     bot = kernel.respond(user)
    #     print('>>>', bot)
    DATABASE.close()

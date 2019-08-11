import sqlite3
import csv

# open database
connection = sqlite3.connect('db.sqlite3')

# create table #################################################################
create_table_lesson = f"""\
CREATE TABLE IF NOT EXISTS Lesson(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson INTEGER NOT NULL,

    UNIQUE(id) ON CONFLICT IGNORE
);
"""
create_table_level = f"""\
CREATE TABLE IF NOT EXISTS Level(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    level INTEGER NOT NULL,

    UNIQUE(id) ON CONFLICT IGNORE
);
"""
create_table_sentence = f"""\
CREATE TABLE IF NOT EXISTS Sentence(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        japanese TEXT NOT NULL,
        romaji TEXT NOT NULL,
        vietnamese TEXT NOT NULL,
        counter INTEGER DEFAULT 0,
        lesson_id INTEGER,
        level_id INTEGER,

        UNIQUE(id) ON CONFLICT IGNORE
    );    
"""

connection.execute(create_table_lesson)
connection.execute(create_table_level)
connection.execute(create_table_sentence)

# insert data #########################################################
with open('data_level.csv', 'r') as data_level:
    reader = csv.reader(data_level)
    for index, row in enumerate(reader):
        if index == 0:
            pass
        else:
            insert_query = f"""\
                insert OR IGNORE into level(id, level)
                values({row[0]}, {row[1]})
            """
            connection.execute(insert_query)
            print(insert_query)

with open('data_lesson.csv', 'r') as data_lesson:
    reader = csv.reader(data_lesson)
    for index, row in enumerate(reader):
        if index == 0:
            pass
        else:
            insert_query = f"""\
                insert OR IGNORE into lesson(id, lesson)
                values({row[0]}, {row[1]})
            """
            connection.execute(insert_query)
            print(insert_query)

with open('data_sentence.csv', 'r') as data_sentence:
    reader = csv.reader(data_sentence)
    for index, row in enumerate(reader):
        if index == 0:
            pass
        else:
            insert_query = f"""\
                insert OR IGNORE into sentence(id, japanese, romaji, vietnamese, counter, lesson_id, level_id)
                values({row[0]}, "{row[1]}", "{row[2]}", "{row[3]}", {row[4]}, {row[5]}, {row[6]})
            """
            print(insert_query)
            connection.execute(insert_query)
data_sentence.close()
data_lesson.close()
data_level.close()

connection.commit()
connection.close()

print('create success')

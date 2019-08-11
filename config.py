from flask import Flask, escape, render_template, json
import sqlite3

app = Flask(__name__)


def connection():
    return sqlite3.connect('database/db.sqlite3')


query_get_all_sentence = f"""\
    select * from sentence
"""


def convert_to_array_of_dict(data, type):
    """
        conver data when cursor.fetchall() to array of dict

        ⎐ type: one of ['lesson', 'sentence', 'level']

        :🏁 return:     dictionary
    """
    if type == 'sentence':
        result = []
        for row in data:
            new_row = {
                'id': row[0],
                'japanese': row[1],
                'romaji': row[2],
                'vietnamese': row[3],
                'counter': row[4],
                'lesson_id': row[5],
                'level_id': row[6]
            }
            result.append(new_row)

    return result


@app.route('/')
def index():
    conn = connection()
    cursor = conn.execute(query_get_all_sentence)
    data = cursor.fetchall()
    data = convert_to_array_of_dict(data, 'sentence')
    print(json.dumps(data))
    return render_template('index.html', list_sentence=json.dumps(data))


@app.route('/counter/<int:id>/<value>', methods=['POST'])
def counter(id, value):
    conn = connection()
    print("Gias tri", id, str(value))
    sql_query_update_counter = f"""\
        update sentence
        set counter = counter + {value}
        where id = {id}
    """
    print(sql_query_update_counter)
    conn.execute(sql_query_update_counter)
    conn.commit()
    conn.close()
    print("Counter thanh cong", id, value)
    return 'success'

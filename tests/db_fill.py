#!/usr/bin/python

from os import listdir
from fnmatch import fnmatch
import sys
import sqlite3

###########################################################################

def get_tests():
    tests = []
    for file_name in listdir('.'):
        if fnmatch(file_name, '*.tst'):
            tests.append(file_name)

    return tests

###########################################################################

def process_test(db_name, test_name):
    test = open(test_name)
    lines = test.readlines()

    symbols_number = 0
    question_number = len(lines) - 1
    questions = []

    for line in lines[1:]:
        line_length = len(line) - 1 if line[-1] == '\n' else len(line)
        ws_position = line.find(' ')
        weight = int(line[:ws_position])
        text = line[ws_position + 1:line_length]
        symbols_number += len(text.decode("utf-8"))
        questions.append((text, weight))

    table_id = test_name[:-4]
    table_caption = lines[0][:-1]


    drop_command = "DROP TABLE IF EXISTS {0}".format(table_id)
    create_command = "CREATE TABLE {0}(Id INTEGER PRIMARY KEY, Question TEXT, Weight INT)".format(table_id)
    insert_command = "INSERT INTO {0}(Question, Weight) VALUES(?, ?)".format(table_id)

    con = sqlite3.connect(db_name)
    con.text_factory = str

    with con:
        cur = con.cursor()
        cur.execute(drop_command)
        cur.execute(create_command)
        cur.executemany(insert_command, questions)

    return (table_id, table_caption, symbols_number, question_number)

###########################################################################

def process_descriptions(db_name, tests_descs):
    table_name = "description"

    drop_command = "DROP TABLE IF EXISTS {0}".format(table_name)
    create_command = "CREATE TABLE {0}(Id INTEGER PRIMARY KEY, Name TEXT, RName TEXT, Symbols INT, Questions INT)".format(table_name)
    insert_command = "INSERT INTO {0}(Name, RName, Symbols, Questions) VALUES(?, ?, ?, ?)".format(table_name)

    con = sqlite3.connect(db_name)
    con.text_factory = str

    with con:
        cur = con.cursor()
        cur.execute(drop_command)
        cur.execute(create_command)
        cur.executemany(insert_command, tests_descs)

###########################################################################
# Script itself
###########################################################################

if len(sys.argv) < 2:
    print "Usage: {0} [database name]".format(sys.argv[0])
    sys.exit(1)

db_name = sys.argv[1]

tests_names = get_tests()
tests_descriptions = []

for test_name in tests_names:
    tests_descriptions.append(process_test(db_name, test_name))

process_descriptions(db_name, tests_descriptions)



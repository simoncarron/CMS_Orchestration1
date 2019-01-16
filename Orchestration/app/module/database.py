import xml.etree.ElementTree as ET
import sqlite3
import itertools
from flask import Flask, g, session

import os

import config as settings

app = Flask(__name__)

def createDataBase():
    if not os.path.exists(settings.DATABASE_FOLDER_NAME):
        os.makedirs(settings.DATABASE_FOLDER_NAME)

    database = os.path.join(os.getcwd(), settings.DATABASE_FOLDER_NAME, settings.DATABASE_NAME)
    conn = sqlite3.connect(database)

    schema = os.path.join(os.getcwd(), settings.DATABASE_FOLDER_NAME, settings.DATABASE_SCHEMA)

    with app.open_resource(schema, mode='r') as f:
        conn.cursor().executescript(f.read())

def getDataBase():
    if not hasattr(g, os.path.join(os.getcwd(), settings.DATABASE_FOLDER_NAME, settings.DATABASE_NAME)):
        g.sqlite_db = connectDataBase()
    return g.sqlite_db


def connectDataBase():
    rv = sqlite3.connect(os.path.join(os.getcwd(), settings.DATABASE_FOLDER_NAME, settings.DATABASE_NAME))
    rv.row_factory = sqlite3.Row

    return rv

def getEntries(table,*pkID):

    db = getDataBase()
    db.row_factory = dict_factory

    if pkID.__len__() == 1:
        cur = db.execute('select * from ' + table + ' where fkID_created_by = '+str(pkID[0])+' order by pkID desc')
    else:
        cur = db.execute('select * from ' + table + ' order by pkID desc')


    entries = cur.fetchall()
    if table in "user":
        for a in entries:
            a['dependecyNbr'] = getNbrDependencyRecordsUser(table, a['pkID'])
            a['dependecyDic'] = getDicDependencyRecordsUser(table, a['pkID'])
    else:
        for a in entries:
            a['dependecyNbr'] = getNbrDependencyRecords(table, a['pkID'])
            a['dependecyDic'] = getDicDependencyRecords(table, a['pkID'])

    return entries

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def getNbrDependencyRecords(table, pkID):
    db = getDataBase()

    result = ""

    cur = db.execute('select name from sqlite_master where type = "table"')
    for a in cur:
        cursor = db.execute('select * from ' + a[0])
        names = list(map(lambda x: x[0], cursor.description))

        for c in names:
            if c == "fkID_" + table:
                cur = db.execute('select count() from ' + a[0] + ' where fkID_' + table + ' like ' + pkID.__str__())

                result = cur.fetchone()[0]
    if result == "":
        result = 0

    return result

def getNbrEntries(table,*pkID):
    db = getDataBase()
    if pkID.__len__() == 1:
        cur = db.execute('select count() from ' + table + ' where fkID_created_by = '+str(pkID[0]))
    else:
        cur = db.execute('select count() from ' + table)

    current_records = cur.fetchone()
    nbr = int(current_records[0])

    return nbr

def getDicDependencyRecords(table, pkID):
    db = getDataBase()

    result = []

    cur = db.execute('select name from sqlite_master where type = "table"')
    for a in cur:
        cursor = db.execute('select * from ' + a[0])
        names = list(map(lambda x: x[0], cursor.description))
        for c in names:
            if c == "fkID_" + table:
                db.row_factory = dict_factory
                cur = db.execute('select * from ' + a[0] + ' where fkID_' + table + ' like ' + pkID.__str__())

                response = cur.fetchone()
                if response != None:
                    response["table"]=a[0]
                    result.append(response)

                while response is not None:
                    response = cur.fetchone()
                    if response != None:
                        response["table"]=a[0]
                        result.append(response)

    return result
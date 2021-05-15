# -*- coding: utf-8 -*-

import sqlite3
import datetime

class Db:
    def __init__(self):
        database = "agendaDB.sqlite3"
        self.conn = self.create_connection(database)
    
    def create_connection(self, database):
        try:
            conn = sqlite3.connect(database)
            return conn
        except:
            print("Erro ao conectar ao database")
        return None
        
    def create_tables(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS   
                          Contatos (Telefone TEXT 
                          ,Nome TEXT, PRIMARY 
                          KEY(Telefone));""")
        
        self.conn.commit()
    
    def insert_person(self, contato):
        values = (contato.get_telefone(),contato.get_nome())
        command = "INSERT INTO Contatos (Telefone, Nome) VALUES (?, ?);"
        try:
            self.conn.execute(command, values)
        except:
            return 0
        self.conn.commit()
        return 1
        
    def get_contato(self, nome):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Contatos WHERE Nome='%s'" % nome)
        row = cur.fetchall()
        return row[0]
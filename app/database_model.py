import sqlite3

class DatabaseComponent:
    def __init__(self):
        con = sqlite3.connect(":memory:")
        self.conn = con

class DatabaseManager:
    notes_table = "notes"

    def __init__(self):
        self.database = DatabaseComponent()
        self.started = False
        self.message = "Database Components created"

    def setup(self):
        if not self.started:
            try:
                with self.database.conn:
                    self.database.conn.executescript("""
                        create table if not exists notes (id integer primary key, 
                        name text unique, tuning text, chords text, instrument text);
                        create table if not exists users (email text primary key unique, 
                        f_name text unique, l_name text unique);
                        """)
                    self.started = True
                    self.message = "Database setup complete"
            except sqlite3.Error:
                self.message = "Unable to setup the database component"
                self.started = False
        else:
            self.message = "Database setup was already completed"

    def insert_note(self, name: str, tuning: str, chords: str, instrument: str):
        if self.started:
            try:
                with self.database.conn:
                    self.database.conn.\
                        execute("insert into notes (name, tuning, chords, instrument) values (?)"
                                , (name, tuning, chords, instrument))
                    self.database.conn.commit()
            except sqlite3.Error:
                self.message = "Unable to insert note"
        else:
            self.message = "Unable to insert note: database has not been started"

    def insert_user(self, email, f_name, l_name):
        if self.started:
            try:
                with self.database.conn:
                    self.database.conn. \
                        execute("insert into users (email, f_name, l_name) values (?)"
                                , (email, f_name, l_name))
                    self.database.conn.commit()
            except sqlite3.Error:
                self.message = "Unable to insert user"
        else:
            self.message = "Unable to insert user: database has not been started"

    def shutdown(self):
        if self.started:
            try:
                with self.database.conn:
                    self.database.conn.close()
                    self.database = None
                    self.started = False
                    self.message = "Database successfully shutdown"
            except sqlite3.Error:
                self.database = None
                self.started = False
                self.message = "Error closing connection: Database set to None by default"
        else:
            self.database = None
            self.started = False
            self.message = "Database has already been shutdown"

    def restart(self):
        if self.started:
            self.shutdown()
            if not self.started:
                self.database = DatabaseComponent()
                self.started = True
                self.message = "Restarted Connection"
            else:
                self.database = None
                self.started = False
                self.message = "Unable to restart properly"
        else:
            self.database = DatabaseComponent()
            self.started = True
            self.message = "Restarted Connection"


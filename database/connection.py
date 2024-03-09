import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def print_query(query):
    print(f"📃  Running query: {query}")


class QueryExecutionException(Exception):
    pass


class Connection:
    def __init__(self, print_queries=False, database_filename=".sqlite"):
        self.sqlite3_connection = sqlite3.connect(database_filename)
        self.sqlite3_connection.row_factory = dict_factory
        self.sqlite3_connection.set_trace_callback(print_query if print_queries else None)
        self.sqlite3_cursor = self.sqlite3_connection.cursor()
        
    def execute(self, query: str, **query_parameters):
        try:
            self.sqlite3_cursor.execute(query, query_parameters)
            self.sqlite3_connection.commit()
            return self.sqlite3_cursor.fetchall()
        except Exception as e:
            raise QueryExecutionException(f"Could not execute query '{query}', because {e}. Parameters: {query_parameters}")
    
    @property
    def last_id(self):
        return self.sqlite3_cursor.lastrowid
    
    def fetch_first(self, query: str, **query_parameters):
        return next(iter(self.execute(query, **query_parameters)), None)
    
    def close(self):
        self.sqlite3_cursor.close()
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, trace):
        self.close()
        

default_connection = Connection(print_queries=False)

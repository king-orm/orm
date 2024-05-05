import re
from datetime import datetime


column_definition_prefix = 'c_'
where_methods_prefix = 'where_'
with_methods_prefix = 'with_'
first_where_methods_prefix = 'first_where_'
id_column_definition = 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'


def pascal_case_to_snake_case(pascal_case_string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', pascal_case_string).lower()


class time:
    pass


sql_types = {
    str: 'VARCHAR(255)',
    float: 'FLOAT',
    int: 'INTEGER',
    bool: 'BOOLEAN',
    time: 'TIME',
    datetime: 'TIMESTAMP'
}


sql_modifiers = {
    'unique': 'UNIQUE',
    'required': 'NOT NULL',
    'primary': 'PRIMARY KEY',
}


def cut_column_name(column_name):
    return column_name[len(column_definition_prefix):]


class ModelNotFoundException(Exception):
    pass


class MalformedQueryException(Exception):
    pass


def unique(type):
    return ColumnDefinition(type, 'unique')


def column(type, *modifiers, column_name=None):
    return ColumnDefinition(type, *modifiers, column_name=column_name)


class ColumnDefinition:
    @staticmethod
    def create(definition):
        if isinstance(definition, ColumnDefinition):
            return definition
        
        return ColumnDefinition(definition)
    
    @classmethod
    @property
    def id(cls):
        return ColumnDefinition(int, 'primary', 'required')
    
    def __init__(self, column_type, *modifiers, column_name=None):
        self.type = guess_sql_type(column_type)
        self.modifiers = modifiers
        self.foreign_model = column_type if issubclass(column_type, Model) else None
        self.column_name = column_name
    
    def has_modifiers(self):
        return len(self.modifiers) != 0
    
    def has_no_modifiers(self):
        return not self.has_modifiers()
    
    @property
    def sql_expression(self):
        if self.has_no_modifiers():
            return self.type
        
        return f"{self.type} {' '.join([sql_modifiers[modifier] for modifier in self.modifiers])}"
    
    @property
    def foreign_key_expression(self):
        if not self.is_foreign_key():
            raise ValueError(f"Can't get foreign key expression of a non-foreign definition '{self.sql_expression}'")
        
        return f"FOREIGN KEY ({self.foreign_column_name}) REFERENCES {self.foreign_model.table_name}(id)"
    
    @property
    def foreign_column_name(self):
        if not self.is_foreign_key():
            raise ValueError(f"Can't get foreign column name of a non-foreign definition '{self.sql_expression}'")
        
        if self.is_column_name_set():
            return self.column_name
        
        return f'{self.foreign_model.model_name}_id'
    
    def is_foreign_key(self):
        return self.foreign_model is not None
    
    def is_column_name_set(self):
        return self.column_name is not None
    
    def decide_on_column_name(self, class_variable_name):
        if self.is_column_name_set():
            return self.column_name
        
        return self.foreign_column_name if self.is_foreign_key() else class_variable_name
    
    def __str__(self) -> str:
        return f"<ColumnDefinition: type = {self.type}, modifiers = {self.modifiers}, foreign model = {self.foreign_model}, preset column name = {self.column_name}>"


class ModelSelector:
    def __init__(self, model_cls):
        self.model_cls = model_cls
        
    def __getattr__(self, name):
        if name.startswith(where_methods_prefix):
            return lambda value: self.model_cls.where_column_equals(name[len(where_methods_prefix):], value)
        
        if name.startswith(first_where_methods_prefix):
            return lambda value: self.model_cls.first_where_column_equals(name[len(first_where_methods_prefix):], value)
        
        raise AttributeError(f"No such attribute ModelSelector.{name}")
        
    def all(self):
        return self.model_cls.all()


class ModelPicker:
    def __init__(self, model_cls):
        self.model_cls = model_cls
        
    def __getattr__(self, name):
        if name.startswith(with_methods_prefix):
            return lambda value: self.model_cls.first_where_column_equals(name[len(with_methods_prefix):], value)


class Model:
    def __init__(self, **raw_record):
        self.__raw_record__ = raw_record
    
    @classmethod
    def wrap(cls, **raw_record):
        return cls(**raw_record)
    
    @classmethod
    def wrap_all(cls, raw_records):
        return [cls.wrap(**raw_record) for raw_record in raw_records]
    
    @classmethod
    def create(cls, **raw_record):
        model = cls.wrap(**raw_record)
        model.store()
        
        return model
    
    @classmethod
    def create_all(cls, raw_records):
        return [cls.create(**raw_record) for raw_record in raw_records]
    
    @classmethod
    def where_column_equals(self, column_name, value):
        if not self.has_column(column_name):
            raise MalformedQueryException(f"{self.table_name.capitalize()} does not have a {column_name}")
        
        return self.wrap_all(connection.execute(f"SELECT * FROM {self.table_name} WHERE {column_name} = :value;", value=value))
    
    @classmethod
    def first_where_column_equals(self, column_name, value):
        if not self.has_column(column_name):
            raise MalformedQueryException(f"{self.table_name.capitalize()} does not have a {column_name}")
        
        raw_model = connection.fetch_first(f"SELECT * FROM {self.table_name} WHERE {column_name} = :value LIMIT 1;", value=value)
        
        if raw_model is None:
            return None
        
        return self.wrap(**raw_model)
    
    @classmethod
    def all(cls):
        return cls.wrap_all(connection.execute(f"SELECT * FROM {cls.table_name};"))
    
    @classmethod
    def is_class_variable_column_definition(cls, column_name, definition):
        return column_name.startswith(column_definition_prefix)
    
    @classmethod
    @property
    def model_name(cls):
        return pascal_case_to_snake_case(cls.__name__)
    
    @classmethod
    @property
    def table_name(cls):
        return pascal_case_to_snake_case(pluralize(cls.__name__)).lower()
    
    @classmethod
    @property
    def auxiliary_column_definitions(cls):
        return {ColumnDefinition.create(definition).decide_on_column_name(cut_column_name(column_name)): ColumnDefinition.create(definition) 
                for column_name, definition in dict(vars(cls)).items() 
                if cls.is_class_variable_column_definition(column_name, definition)}
    
    @classmethod
    @property
    def column_definitions_sql_list(cls):
        return ", ".join(f'{definition.decide_on_column_name(column_name)} {definition.sql_expression}' 
                         for column_name, definition in cls.column_definitions.items())
    
    @classmethod
    @property
    def column_definitions(cls):
        return {'id': ColumnDefinition.id} | cls.auxiliary_column_definitions
    
    @classmethod
    def get_column_definition(cls, column_name):
        class_variable_name = f'{column_definition_prefix}{column_name}'
        
        if not hasattr(cls, class_variable_name):
            raise ValueError(f'No such column {column_name}')
        
        return getattr(cls, class_variable_name)
    
    @classmethod
    def find(cls, id: int):
        raw_record = connection.fetch_first(f"SELECT * FROM {cls.table_name} WHERE id = :id;", id=id)
        
        if raw_record is None:
            return None
        
        return cls(**raw_record)
        
    @classmethod
    def find_or_fail(cls, id: int):
        model = cls.find(id)
        
        if model is None:
            raise ModelNotFoundException(f"No such {cls.model_name} with id = {id}")
        
        return model
        
    @classmethod
    def reset(cls):
        cls.down()
        cls.up()
        
    @classmethod
    def up(cls):
        connection.execute(f"CREATE TABLE IF NOT EXISTS {cls.table_name} ({cls.column_definitions_sql_list}{cls.foreign_keys_expression});")
        
        if hasattr(cls, 'seed') and type(records := cls.seed()) == list:
            cls.create_all(records)
            
        if hasattr(cls, 'after_seeding'):
            cls.after_seeding()
            
    @classmethod
    def down(cls):
        connection.execute(f"DROP TABLE IF EXISTS {cls.table_name}")
    
    @classmethod
    def clear(cls):
        connection.execute(f"DELETE FROM {cls.table_name}")
    
    @classmethod
    def count(cls) -> int:
        return connection.fetch_first(f"SELECT COUNT(*) AS `count` FROM {cls.table_name};")["count"]
    
    @classmethod
    @property
    def columns(cls):
        return cls.column_definitions.keys()
    
    @classmethod
    @property
    def select(cls):
        return ModelSelector(cls)
    
    @classmethod
    @property
    def pick(cls):
        return ModelPicker(cls)
    
    @classmethod
    def has_column(cls, column_name):
        return column_name in cls.columns
    
    @classmethod
    @property
    def foreign_column_definitions(cls):
        return {column_name: definition for column_name, definition in cls.auxiliary_column_definitions.items() if definition.is_foreign_key()}
    
    @classmethod
    def has_foreign_keys(cls):
        return len(cls.foreign_column_definitions) != 0
    
    @classmethod
    def is_foreign_column(cls, name):
        return name in cls.foreign_column_definitions.keys()
    
    @classmethod
    def is_foreign_model(cls, name):
        return cls.is_foreign_column(f'{name}_id')
    
    @classmethod
    @property
    def foreign_keys_sql_list(cls):
        return ', '.join([definition.foreign_key_expression for definition in cls.foreign_column_definitions.values()])
    
    @classmethod
    @property
    def foreign_keys_expression(cls):
        return f', {cls.foreign_keys_sql_list}' if cls.has_foreign_keys() else ""
    
    @classmethod
    def mass_store(cls, raw_records):
        connection.execute(f"INSERT INTO {cls.table_name} ({', '.join([definition.decide_on_column_name(column_name) for column_name, definition in cls.auxiliary_column_definitions.items()])}) VALUES ({', '.join([f':{definition.decide_on_column_name(column_name)}' for column_name, definition in cls.auxiliary_column_definitions.items()])});", **raw_record)
        
    def store(self):
        connection.execute(f"INSERT INTO {self.table_name} ({', '.join([definition.decide_on_column_name(column_name) for column_name, definition in self.auxiliary_column_definitions.items()])}) VALUES ({', '.join([f':{definition.decide_on_column_name(column_name)}' for column_name, definition in self.auxiliary_column_definitions.items()])});", **self.__raw_record__)
        self.__raw_record__["id"] = connection.last_id
    
    def __getattr__(self, name):
        if self.is_foreign_column(name):
            return self.__raw_record__[name]
        
        if self.is_foreign_model(name):
            foreign_model = self.get_column_definition(name)
            column_definition = ColumnDefinition.create(foreign_model)
            return column_definition.foreign_model.find(getattr(self, column_definition.decide_on_column_name(name)))
            
        if not self.has_column(name):
            raise AttributeError(f"There is no such attribute '{name}'")
            
        return self.__raw_record__[name]
    
    def __str__(self):
        return str(self.__raw_record__)
    
    
def guess_sql_type(python_type):
    if type(python_type) == str:
        return python_type
    
    if issubclass(python_type, Model):
        return guess_sql_type(int)
    
    if python_type not in sql_types:
        raise ValueError(f"Can't guess sql type for {python_type}, {type(python_type).__name__}")

    return sql_types[python_type]
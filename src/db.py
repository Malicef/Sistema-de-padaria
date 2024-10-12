from peewee import SqliteDatabase, Model

db = SqliteDatabase('padaria.db')
class BaseModel(Model):
    class Meta:
        database = db

        

        
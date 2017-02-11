from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
with open('user.txt', 'r') as myfile:
    data = myfile.read()
db = PostgresqlDatabase(data, user=data)



class Sprinter(Model):
    title = TextField()
    story = TextField()
    acceptance_criteria = TextField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()

    """A base model that will use our Postgresql database"""
    class Meta:
        database = db

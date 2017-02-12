from models import *

db.connect()
# List the tables here what you want to create...
db.drop_tables([Sprinter], safe=True)
db.create_tables([Sprinter], safe=True)
Sprinter.create(title="Kutya",story="Szerezni egy kutyát",acceptance_criteria="Legyen nagyon kutya",business_value=1500,estimation=40,status="Planning")
Sprinter.create(title="Sün",story="Szerezni egy sünt",acceptance_criteria="Legyen nagyon sün",business_value=1500,estimation=30,status="Done")
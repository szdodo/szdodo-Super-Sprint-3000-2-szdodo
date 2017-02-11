from models import *

db.connect()
# List the tables here what you want to create...
db.drop_tables([Sprinter], safe=True)
db.create_tables([Sprinter], safe=True)
Sprinter.create(title="Kaki",story="maki",acceptance_criteria="legyen kakis",business_value=30000,estimation=3.4,status="new")
Sprinter.create(title="Kakás",story="makás",acceptance_criteria="már kakis",business_value=50000,estimation=1.2,status="on-going")
from mongoengine import Document, StringField, IntField, ListField


class Employee(Document):
    emp_id = IntField()
    name = StringField()
    age = IntField()
    teams = ListField()

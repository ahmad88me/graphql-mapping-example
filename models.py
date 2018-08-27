from mongoengine import Document
from mongoengine.fields import StringField


class Person(Document):
    meta = {'collection': 'person'}
    name = StringField(required=True)


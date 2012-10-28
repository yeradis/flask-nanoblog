from nanoblog.database import db
from flask import url_for
import datetime


class Post(db.Document):
    content = db.StringField(required=True)
    added = db.DateTimeField(default=datetime.datetime.now, required=True)
    slug = db.StringField(max_length=255, required=True)
    visible = db.BooleanField(required=False,default=False)

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.content

    meta = {
        'allow_inheritance': True,
        'indexes': ['-added', 'slug'],
        'ordering': ['-added']
    }



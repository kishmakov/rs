# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'app-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Description(models.Model):
    id = models.IntegerField(null=False, primary_key=True, db_column=u'Id', blank=True) # Field name made lowercase.
    name = models.TextField(db_column=u'Name', blank=True) # Field name made lowercase.
    rname = models.TextField(db_column=u'RName', blank=True) # Field name made lowercase.
    symbols = models.IntegerField(null=True, db_column=u'Symbols', blank=True) # Field name made lowercase.
    questions = models.IntegerField(null=True, db_column=u'Questions', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'description'

class Politics(models.Model):
    id = models.IntegerField(null=False, primary_key=True, db_column=u'Id', blank=True) # Field name made lowercase.
    question = models.TextField(db_column=u'Question', blank=True) # Field name made lowercase.
    weight = models.IntegerField(null=True, db_column=u'Weight', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'politics'

class Household(models.Model):
    id = models.IntegerField(null=False, primary_key=True, db_column=u'Id', blank=True) # Field name made lowercase.
    question = models.TextField(db_column=u'Question', blank=True) # Field name made lowercase.
    weight = models.IntegerField(null=True, db_column=u'Weight', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'household'

class Religion(models.Model):
    id = models.IntegerField(null=False, primary_key=True, db_column=u'Id', blank=True) # Field name made lowercase.
    question = models.TextField(db_column=u'Question', blank=True) # Field name made lowercase.
    weight = models.IntegerField(null=True, db_column=u'Weight', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'religion'

class Sex(models.Model):
    id = models.IntegerField(null=False, primary_key=True, db_column=u'Id', blank=True) # Field name made lowercase.
    question = models.TextField(db_column=u'Question', blank=True) # Field name made lowercase.
    weight = models.IntegerField(null=True, db_column=u'Weight', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'sex'

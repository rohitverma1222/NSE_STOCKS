# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bhav(models.Model):
    id = models.IntegerField(blank=True,primary_key=True, null=False)
    symbol = models.TextField(db_column='SYMBOL', blank=True, null=True)  # Field name made lowercase.
    series = models.TextField(db_column='SERIES', blank=True, null=True)  # Field name made lowercase.
    date1 = models.TextField(db_column='DATE1', blank=True, null=True)  # Field name made lowercase.
    prev_close = models.IntegerField(db_column='PREV_CLOSE', blank=True, null=True)  # Field name made lowercase.
    open_price = models.IntegerField(db_column='OPEN_PRICE', blank=True, null=True)  # Field name made lowercase.
    high_price = models.IntegerField(db_column='HIGH_PRICE', blank=True, null=True)  # Field name made lowercase.
    low_price = models.IntegerField(db_column='LOW_PRICE', blank=True, null=True)  # Field name made lowercase.
    last_price = models.IntegerField(db_column='LAST_PRICE', blank=True, null=True)  # Field name made lowercase.
    close_price = models.IntegerField(db_column='CLOSE_PRICE', blank=True, null=True)  # Field name made lowercase.
    avg_price = models.IntegerField(db_column='AVG_PRICE', blank=True, null=True)  # Field name made lowercase.
    ttl_trd_qnty = models.IntegerField(db_column='TTL_TRD_QNTY', blank=True, null=True)  # Field name made lowercase.
    turnover_lacs = models.IntegerField(db_column='TURNOVER_LACS', blank=True, null=True)  # Field name made lowercase.
    no_of_trades = models.IntegerField(db_column='NO_OF_TRADES', blank=True, null=True)  # Field name made lowercase.
    deliv_qty = models.IntegerField(db_column='DELIV_QTY', blank=True, null=True)  # Field name made lowercase.
    deliv_per = models.IntegerField(db_column='DELIV_PER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bhav'

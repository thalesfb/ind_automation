# api/models/plc.py

from django.db import models

class PLC(models.Model):
  """
  Model to represent a PLC in database from pymodbus
  """    
  ip_address = models.GenericIPAddressField()
  port = models.IntegerField()
  unit_id = models.IntegerField()
  timeout = models.FloatField()
  retry_on_empty = models.BooleanField()

  def __str__(self):
    return f"{self.ip_address}:{self.port} (Unit ID: {self.unit_id})"
from djongo import models

# Create your models here.
class Dokumentasi(models.Model):    
    picture = models.FileField(upload_to='pic/', blank=True, default="dokumentasi_pic/dummy.jpg")
    
    class Meta:
        abstract = True

class Proposal(models.Model):
    file = models.FileField(upload_to='pic/')
    filename = models.CharField(max_length=500)    
    description = models.CharField(max_length=10000)
    
    class Meta:
        abstract = True

class Pengumuman(models.Model):
    nama = models.CharField(max_length=200) 
    tanggal = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    
    class Meta:
        abstract = True

class EntryDoc(models.Model):
    doc = models.EmbeddedField(
        model_container=Dokumentasi,              
    )    
class EntryProp(models.Model):
    prop = models.EmbeddedField(
        model_container=Proposal
    )
class EntryUm(models.Model):
    umum = models.EmbeddedField(
        model_container=Pengumuman
    )
   
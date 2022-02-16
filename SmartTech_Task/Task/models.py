from tkinter import CASCADE
from venv import create
from django.db import models
from .tools import cleanInput
import re 
# Create your models here.

class common(models.Model):
    content = models.TextField(blank=False)
    createed_Date = models.DateTimeField(auto_now_add=True)
    updated_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    
    def save(self, *args, **kwargs):
        self.content = cleanInput(self.content)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Protein(common):
    protein_id = models.AutoField(primary_key=True)
    aas = models.TextField(blank=False)
    dna = models.TextField(blank=False)
          

    def save(self, *args, **kwargs):
        if len(self.dna) != len(self.aas) * 3:
            raise ValueError("DNA Sequence must be 3 times bigger than Amino Acid Sequence")
        else:
            x = re.findall("[^ACGT]", self.dna)
            y = re.findall("[^ACGT]", self.aas)
            if x or y:
                raise ValueError("DNA Sequence or Amino Acid Sequence has char not valide")
            else:
                self.dna = cleanInput(self.dna)
                self.aas = cleanInput(self.aas)
                super().save(*args, **kwargs)


class Document(common):
    document_id = models.AutoField(primary_key=True)

class Comment(common):
    comment_id = models.AutoField(primary_key=True)
    protein_ref = models.ForeignKey(Protein,on_delete=models.PROTECT,null=True)
    document_ref = models.ForeignKey(Document,on_delete=models.PROTECT,null=True)

NotiType =[
    ('link','link'),
    ('static','static'),
    ('system','system')
]

class Notification(models.Model):
    noti_id = models.AutoField(primary_key=True)
    noti_type = models.CharField(max_length=25,choices=NotiType)
    content_msg = models.CharField(max_length=50)
    # icon = ''
    created_Date = models.DateTimeField(auto_now_add=True)

    protein_ref  = models.ForeignKey(Protein,on_delete=models.PROTECT,null=True,blank=True)
    comment_ref  = models.ForeignKey(Comment,on_delete=models.PROTECT,null=True,blank=True)
    document_ref = models.ForeignKey(Document,on_delete=models.PROTECT,null=True,blank=True)
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
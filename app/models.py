from django.db import models


class Url(models.Model):

    url = models.CharField(max_length=255)
    date = models.DateField()
    time = models.DateTimeField()
    cout = models.IntegerField()

class BlackList(models.Model):
    detection_method = [
        ("manual_review","Manual Review"),
        ("external_database","External Database"),
        ("phishing_detection","Phishing Detection")
    ]    
    url = models.OneToOneField(Url, on_delete=models.CASCADE)
    detection = models.CharField(max_length=25,choices=detection_method, null=True,blank=True)
    threat_type = models.CharField(max_length=255)



class WhiteList(models.Model):
    url = models.OneToOneField(Url, on_delete=models.CASCADE)
    verified_by = models.CharField(max_length=100, null=True, blank=True)
    verified_date = models.DateTimeField(auto_now_add=True)


class Graylist(models.Model):
    url = models.OneToOneField(Url, on_delete=models.CASCADE) 
    suspicion_reason = models.TextField(null=True, blank=True)
    reviewed_date = models.DateTimeField(auto_now_add=True)  # Fecha de última revisión



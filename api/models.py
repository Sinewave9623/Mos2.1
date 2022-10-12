from django.db import models
# Create your models here.
class TranSum(models.Model):
    TYPE=(
        ('Shares','Shares'),
        ('Mutual Funds','Mutual Funds'),
        ('Futures & Options','Futures & Options'),
        ('Day Trading','Day Trading'),
        ('Trading','Trading')
    )
    FY=(
        
        ('2021-2022','2021-2022'),
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),
        ('2025-2026','2025-2026'),
        ('2026-2027','2026-2027'),
        ('2027-2028','2027-2028'),
        ('2028-2029','2028-2029')
    )
    trId = models.BigAutoField(primary_key=True)
    group=models.CharField('customerId',max_length=10)
    code=models.CharField('memberId',max_length=10)
    fy=models.CharField('fy',max_length=9,choices=FY)
    againstType=models.CharField('type',max_length=20,choices=TYPE)
    sp=models.CharField('scriptId',max_length=5)
    part=models.CharField('script',max_length=30)
    sno=models.IntegerField(blank=True,null=True)
    fmr=models.FloatField(null=True, blank=True)
    isinCode=models.CharField(max_length=30,null=True, blank=True)
    trDate=models.DateField('purchaseDate')
    qty=models.IntegerField('quantity')
    rate=models.DecimalField('rate',max_digits=65, decimal_places=2)
    sVal=models.DecimalField('value',max_digits=65, decimal_places=2)
    sttCharges=models.DecimalField('stt',max_digits=65, decimal_places=2,blank=True,null=True)
    otherCharges=models.DecimalField('other',max_digits=65, decimal_places=2,blank=True,null=True)
    noteAdd=models.CharField('note',max_length=200,blank=True)
    marketRate=models.DecimalField(max_digits=65, decimal_places=2,blank=True,null=True)
    marketValue=models.DecimalField(max_digits=65, decimal_places=2,blank=True,null=True)
    HoldingValue=models.DecimalField(max_digits=65, decimal_places=2,blank=True,null=True)
    avgRate=models.DecimalField(max_digits=65, decimal_places=2,blank=True,null=True)
    scriptSno=models.IntegerField(blank=True,null=True)
    empCode=models.CharField(max_length=10,blank=True,null=True)
    clDate=models.DateField(null=True,blank=True)
    clRate=models.DecimalField(max_digits=65, decimal_places=2,blank=True,null=True)
    clQTY=models.IntegerField(blank=True,null=True)
    clValue=models.DecimalField(max_digits=65, decimal_places=2,blank=True,null=True)
    clsttCharges=models.DecimalField(max_digits=65, decimal_places=2,blank=True,null=True)
    clOtherCharges=models.DecimalField(max_digits=65, decimal_places=2,blank=True,null=True)
    balQty=models.IntegerField(blank=True,null=True)
    dayTrade=models.DecimalField(max_digits=65, decimal_places=2,blank=True,null=True)
    strategyDate=models.DateField(null=True,blank=True)
    strategyTrigger=models.DecimalField(max_digits=65, decimal_places=2,blank=True,null=True)

    

    

    def __str__(self):
        return str(self.group)

     


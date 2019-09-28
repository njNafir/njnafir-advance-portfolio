from django.db import models

class Contact(models.Model):
    first_name 			= models.CharField("First name", max_length=255, blank = True, null = True)
    last_name 			= models.CharField("Last name", max_length=255, blank = True, null = True)
    email 				= models.EmailField()
    phone 				= models.CharField(max_length=20, blank = True, null = True)
    address 			= models.TextField(blank=True, null=True)
    message             = models.TextField(blank=True, null=True)
    createdAt 			= models.DateTimeField("Created At", auto_now_add=True)
    isActive 			= models.BooleanField(default=False)

    def __str__(self):
        if self.first_name:
            return self.first_name
        return self.email

    @property
    def get_email(self):
        return self.email

    @property
    def get_phone(self):
        if self.phone:
            return self.phone
        return "Empty"

    @property
    def get_address(self):
        if self.address:
            return self.address
        return "Empty"

    @property
    def get_message(self):
        if self.message:
            return self.message
        return "Empty"
    
    
    
    
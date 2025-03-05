from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
import random
import string
from django.urls import reverse
from django.conf import settings

# Create your models here.

def generate_random_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))

def generate_result_number():
    # Format: YYYYMMDDXXXX where XXXX is a random number
    from datetime import datetime
    date_part = datetime.now().strftime('%Y%m%d')
    random_part = ''.join(random.choices(string.digits, k=4))
    return f"{date_part}{random_part}"

class LabResult(models.Model):
    result_number = models.CharField(max_length=12, primary_key=True, unique=True, editable=False, 
                                   default=generate_result_number)
    date_created = models.DateTimeField(auto_now_add=True)
    result_image = models.ImageField(upload_to='results/')
    password = models.CharField(max_length=6, default=generate_random_password)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.result_number:
            self.result_number = generate_result_number()
        if not self.password:
            self.password = generate_random_password()
        
        # Generate QR code
        if not self.qr_code:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            # Generate URL for result verification with domain
            result_url = settings.SITE_DOMAIN + reverse('verify_result', args=[self.result_number])
            qr.add_data(result_url)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")
            
            buffer = BytesIO()
            qr_image.save(buffer, 'PNG')
            self.qr_code.save(f'qr_{self.result_number}.png',
                            File(buffer), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Result #{self.result_number}"

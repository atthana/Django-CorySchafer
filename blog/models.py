from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Method นี้สร้างขึ้นเพื่อให้หลังจาก post ขึ้นมาใหม่ได้แล้ว มีหน้าโชว์สรุปสิ่งที่เขียนไป แต่ยังไม่กลับ home นะ
        return reverse('post-detail', kwargs={'pk': self.pk})
        # return reverse('blog-home')  # ถ้าอยากให้กลับ home ก้อแทนด้วยอันนี้ได้เลย

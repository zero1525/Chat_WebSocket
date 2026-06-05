from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=266)
    online = models.ManyToManyField(to = User, blank = True)

    def get_online_cont (self):
        return self.online.count()
    
    def join(self, user):
        self.online.add(user)
        self.save

    def join(self, user):
        self.online.remove(user)
        self.seve

    def __str__(self):
        return f'{self.name} ({self.get_online_cont()})'
    
class Message(models.Model):
    user =models.ForeignKey(to = User, on_delete = models.CASCADE)
    room = models.ForeignKey(to = Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]'
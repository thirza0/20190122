from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField('內文')
    creator = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name = '建立者', related_name='posts', blank = True)
    creat_at = models.DateTimeField('建立時間', auto_now_add=True)
    update_at = models.DateTimeField('更新時間', auto_now_add=True)

    likes = models.ManyToManyField(User,related_name='liked_posts',blank=True)
    # commit = models.ManyToManyField(User, related_name='commit_posts')

    def __str__(self):
        return 'Post Create by {}'.format(self.creator.username) 

    class Commits(models.Model):
        post = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name ='文章', related_name='post')
        content = models.TextField('內容')
        creator = models.ForeignKey(User,on_delete=models.PROTECT, verbose_name='建立者', related_name='creator')
        likes = models.ManyToManyField(User,related_name='liked_commits',blank=True)
        creat_at = models.DateTimeField('建立時間', auto_now_add=True)
        update_at = models.DateTimeField('更新時間', auto_now_add=True)

    def __str__(self):
        return 'Commit create by {}'.format(self.creator.username)

    

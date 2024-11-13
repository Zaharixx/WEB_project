from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, default='no-profile-picture-icon.png')

    def __str__(self):
        return self.nickname


class QuestionManager(models.Manager):
    def get_new(self):
        return self.order_by('-created_at')
    
    def get_hot(self):
        return self.order_by('-rating')
    
    def get_by_tag(self, tag):
        return self.filter(tags=tag).order_by('rating')

    
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=4095)
    tags = models.ManyToManyField(Tag)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=4095)

    def __str__(self):
        return self.text

EVALS = [
    ('+', 'like'),
    ('-', 'dislike'),
]

class QuestionEval(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    eval = models.CharField(max_length=1, choices=EVALS)


class AnswerEval(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    eval = models.CharField(max_length=1, choices=EVALS)


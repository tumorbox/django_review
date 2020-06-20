from django.db import models

# Create your models here.
# 객체 생성(클래스 생성) ->  테이블명
# 모델에서는 모델에 관한 내용만 정리하는 것이 좋다
# form은 forms.py를 새로 만들어서 사용

class Musician(models.Model):
    # 맴버 변수
    # name = '이름이란 사람이 가지는 공통특성'
    name = models.CharField(max_length=100)
    age = models.IntegerField()

def __str__(self):
    return f'{self.name} : {self:age}'
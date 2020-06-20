from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician

# Create your views here.
# 함수정의 함수이름(parameter)
def index(request):
    # .all()로 조회하면 querySet형태
    # querySet은 마치 list처럼 사용가능
    musicians = Musician.objects.all()
    context = {
        'musicians': musicians
    }
    return render(request, 'musicians/index.html', context)

def create(request):
    if request.method == "POST":
        # 사용자의 요청 정보를 담아준다.
        form = MusicianForm(request.POST)
        # forms를 상속받았기 때문에 사용가능
        if form.is_valid():
            # Musician가 models에게 받은 메소드
            # ModelForm을 정의할 때 
            # class Meta : model = Musician을 담아줌
            musician = form.save()
            # redireact('app_name:path_name')
            return redirect('musicians:index')
    else:
        # MusicianForm 불러오기
        # form은 MusicianForm 인스턴스
        # MusicianForm이 가진 정보를 가짐
        # MusicianForm은 Musician wjdqh
        # template에 보여줄 tag들
        form = MusicianForm()
        print(form)

    context ={
        'form':form
    }
    return render(request, 'musicians/create.html', context)

# 함수정의 함수이름 (사용자요청저보, url에 작성한 변수명)
def detail(request, musician_pk):
    # Model.objects.get(조건=변수명)
    musician = Musician.objects.get(pk=musician_pk)
    context = {
        'musician' : musician
    }
    return render(request, 'musicians/detail.html', context)

# update 작성시 주의사항
# instance 값 form에게 담아주기
def update(request, musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    if request.method == "POST":
        form = MusicianForm(request.POST , instance=musician)
        if form.is_valid():
            musician = form.save()
            return redirect('musicians:index')
    else:
        form = MusicianForm(instance=musician)

    context = {
        'form': form
    }
    return render(request, 'musicians/create.html', context)

def delete(request, musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    musician.delete()
    return redirect('musicians:index')


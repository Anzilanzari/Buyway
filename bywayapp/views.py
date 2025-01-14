from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Category,Courses

def home(request):
    categ = Category.objects.all()
    course = Courses.objects.all()
    for category in categ:
        category.course_count = Courses.objects.filter(course=category).count()
    return render(request, "home.html", {'cat': categ, 'crs': course})


def pageRoute(request, pk):
    course = Courses.objects.get(id=pk)
    courses = Courses.objects.all()
    return render(request, "singlepage.html",{'crs':course,'courses':courses})

def listCourses(request):
    course = Courses.objects.all()
    return render(request,"coursespage.html", {'crs':course})


def ViewCategory(request, pk):
    cat = Category.objects.get(id=pk)
    courses = Courses.objects.filter(course=cat)
    return render(request, "categories.html", {'crs': courses, 'cat':cat})



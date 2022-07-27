from django.shortcuts import render, redirect, get_object_or_404
from . models import Course, Category, Tags

# Create your views here.


def courses_list(request, category_slug=None, tags_slug=None):
    category_page = None
    tags_page = None
    category = Category.objects.all()
    tags = Tags.objects.all()

    if category_slug != None:

        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(category=category_page)
    elif tags_slug != None:
        tags_page = get_object_or_404(Tags, slug=tags_slug)
        courses = Course.objects.filter(tags=tags_page)
    else:
        courses = Course.objects.all().order_by('-date')
    context = {
        'courses': courses,
        'category': category,
        'tags': tags
    }
    return render(request, "courses.html", context)


def course_detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    category = Category.objects.all()
    tags = Tags.objects.all()

    context = {
        'course': course,
        'category': category,
        'tags': tags
    }
    return render(request, "course.html", context)

def search(request):
    pass

# def category_list(request,category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug)
    tags = Tags.objects.all()
    category = Category.objects.all()
    context = {
        'courses': courses,
        'category': category,
        'tags': tags

    }
    return render(request, "courses.html", context)

# def tags_list(request,tags_slug):
    courses = Course.objects.all().filter(tags__slug=tags_slug)
    category = Category.objects.all()
    tags = Tags.objects.all()
    context = {
        'courses': courses,
        'category': category,
        'tags': tags
    }
    return render(request, "courses.html", context)

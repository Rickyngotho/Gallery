from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Pic


# Create your views here.
def welcome(request):
    return HttpResponse(request, 'Welcome.html')

def photos_of_day(request):
    date = dt.date.today()
    news = Pic.todays_photos()
    return render(request, 'all-photos/todays-photos.html', {"date": date,"photos":photos})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_photos(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-photos/past-photos.html',{"date": date,"photos":photos})

def search_results(request):

    if 'photo' in request.GET and request.GET["pic"]:
        search_term = request.GET.get("pic")
        searched_pics = Photo.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_pics})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def Pic(request,pic_id):
    try:
        Pic = Pic.objects.get(id = pic_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photo/pic.html", {"pic":pic})
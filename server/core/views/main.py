from django.http.response import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    csdays = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"]
    currdate = datetime.datetime.now()
    html_body = f"today is <strong>{str(currdate.strftime("%A")).lower()}/{csdays[currdate.weekday()]} {str(currdate.date())}</strong>"
    html_body = f"{html_body}\n<br>\ncurrent time: <strong>{datetime.datetime.now().time().strftime("%H:%M")}</strong>"
    return render(request, 'rjdesign.html',{"web_name":"robertjiranek.eu","page_name":"home","page_body":html_body  })
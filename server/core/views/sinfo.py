from django.http.response import HttpResponse
from django.shortcuts import render

def sinfo(request):
    pbody = f"""
    <h2>Robert Jiranek</h2>
    email: <b><a href="mailto:robert.jiranek@gmail.com">robert.jiranek@gmail.com</a></b><br>
    mobile: <b>+420 606790348</b>
             """
    return render(request, 'rjdesign.html',{"web_name":"robertjiranek.eu","page_name":"sysinfo","page_body":pbody})
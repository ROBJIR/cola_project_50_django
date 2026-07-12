from django.http.response import HttpResponse
from django.shortcuts import render
import datetime

def calculator(request, operator:str = "", num1: int = 0,num2: int = 0):
    if (num1 >= 0 and num2 >= 0):
        match operator.lower():
            case "add":
                html_body = f"{num1} + {num2} = {num1 + num2}"
            case "diff":
                html_body = f"{num1} - {num2} = {num1 - num2}"
            case "multi":
                html_body = f"{num1} * {num2} = {num1 * num2}"
            case "div":
                html_body = f"{num1} / {num2} = {num1 / num2}"
            case _:
                html_body = f"warning: /calculator/{operator} ... value of operator is not supported [add,diff,multi,div]"
    else:
        html_body = f"warning: /calculator/{operator}/value_1/value_2/ ... values must be positive integers or 0."


    return render(request, 'rjdesign.html',{"web_name":"robertjiranek.eu","page_name":"calculator","page_body":html_body })
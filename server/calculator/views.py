from django.shortcuts import render

# Create your views here.
def calculator(request, operator:str = "add", num1: int = -1,num2: int = -1):
    html_body=f"<h2>operator: {operator}</h2>"
    if (num1 >= 0 and num2 >= 0):
        match operator.lower():
            case "add":
                html_body = f"{html_body}\n{num1} + {num2} = {num1 + num2}"
            case "diff":
                html_body = f"{html_body}\n{num1} - {num2} = {num1 - num2}"
            case "multi":
                html_body = f"{html_body}\n{num1} * {num2} = {num1 * num2}"
            case "div":
                if num2 == 0:
                    html_body = f"{html_body}\nSorry, but we don't divide by zero."
                else:
                    html_body = f"{html_body}\n{num1} / {num2} = {num1 / num2}"
            case _:
                if operator == "":
                    operator = "???"
                html_body = f"{html_body}\nwarning: /calculator/{operator}/[value_1]/[value_2]/ ... value of operator is not supported [add,diff,multi,div]"
    else:
        html_body = f"{html_body}\nwarning: /calculator/{operator}/[value_1]/[value_2]/ ... values must be positive integers or 0."

    return render(request, 'rjdesign.html',{"web_name":"robertjiranek.eu","page_name":"calculator","page_body":html_body })
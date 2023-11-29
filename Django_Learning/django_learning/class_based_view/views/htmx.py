from django.shortcuts import render
import json
from django.http import JsonResponse


def htmx(request):
    return render(request, 'htmx/htmx.html')

def htmx_form(request):

    if request.method == 'POST':    
        print(request.POST['id'], '----> POST')
        print(request.POST['mail'], '----> POST')
    elif request.method == 'GET':
        print(request.GET.get('param1'), '----> GET')

  
        
    my_list = ["apple", "banana", "orange"]
    print(my_list)
    return JsonResponse(my_list, safe=False)
    # return render(request, 'htmx/partial/form.html')
 

# hx-swap = {innerHTML - Is used to replace the content inside target div
#             outerHTML - Is used to replace the content Outside target div and that div was removed 
#             beforebegin - Is used to append the content before that target div 
#             afterend - Is used to append the content after that target div
#             afterbegin - Is uset to append the content the target div first element
#             beforeend - Is used to append the content the target div last element 
#             delete - Is used to delete that target div   
# swap:1s & settle:1s - It is use to apply that content after 3 sec}
# hx-trigger = {click delay:5s - It used to click after 5s}
 
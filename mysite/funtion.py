# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello world")
    return render(request, "home.html")

def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)

    word_dict = {} #创建一个叫word_dict的空字典

    for word in user_text: #判断字在不在文本里面
        if word not in word_dict: #如果不在word_dict里面 就创建一个word
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    wordict = word_dict.items() #让word_dict可迭代

    sorted_dict = sorted(wordict, key=lambda w:w[1], reverse=True) #'灭': 37 （ 灭是0 ， 37是1）这里是用37来排序

    return render(request, "count.html", {'Totalcount': total_count, 'text': user_text, 'worddict': word_dict, 'sort': sorted_dict})

def about(request):
    return render(request, "about.html")
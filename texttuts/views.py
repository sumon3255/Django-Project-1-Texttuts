#by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'newindex.html')


def analyze(request):
    #get TExt
    djtext = request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newline= request.POST.get('newline','off')
    spacerem= request.POST.get('spacerem','off')
    
    # analyze = djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        params={'purpose':'Remove Punctuations','analyzed_text':analyze}
        return  render(request,"analyze.html",params)
    elif fullcaps == "on":
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()
        params={'purpose':'Change To Upercase','analyzed_text':analyze}
        return  render(request,"analyze.html",params)
    elif newline == "on":
        analyze = ""
        for char in djtext:
                if char != "\n" and char!="\r":
                    analyze = analyze + char
        params={'purpose':'Removed Newlines','analyzed_text':analyze}
        return  render(request,"analyze.html",params)
    elif(spacerem=="on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                   if not(djtext[index] == " " and djtext[index+1]==" "):
                           analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            # Analyze the text
            return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error!! Please choose any of functions")
    


# def removepunc(request):
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove tag")

# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'> Back </a>")

# def charcount(request):
#     return HttpResponse("charcount ")
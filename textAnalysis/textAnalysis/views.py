from django.http import HttpResponse
from django.shortcuts import render


# render home page index.html
def index(request):
    return render(request, "index.html")


# render analyze.html file
def analyze(request):
    djtext = request.POST.get("ta", "default")
    removepunc = request.POST.get("ch", 'off')
    captalize = request.POST.get("ch1", "off")
    rmnwline = request.POST.get("ch2", "off")
    spaceremove = request.POST.get("ch3", "off")
    txtcount = request.POST.get("ch4", "off")
    # this will remove punctuation from text
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        analyzed_text = ""
        for a in djtext:
            if a not in punctuations:
                analyzed_text = analyzed_text + a
        params = {'analyzed_text': analyzed_text}
        djtext = analyzed_text

    # this will capitalize the text
    if captalize == "on":
        analyzed_text = ""
        for a in djtext:
            analyzed_text = analyzed_text + a.upper()
        params = {'analyzed_text': analyzed_text}
        djtext = analyzed_text

    # this will remove new line from the text
    if rmnwline == "on":
        analyzed_text = ""
        for a in djtext:
            if a != "\n" and a != "\r":
                analyzed_text = analyzed_text + a
        params = {'analyzed_text': analyzed_text}
        djtext = analyzed_text

    # this will remove extra spaces from the text
    if spaceremove == "on":
        analyzed_text = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed_text = analyzed_text + char
        params = {'analyzed_text': analyzed_text}
        djtext = analyzed_text

    # this will count the number of words and chars in the text
    if txtcount == "on":
        ccount = 0
        wcount = 1
        for a in djtext:
            ccount += 1
        for a in djtext:
            if a == " ":
                wcount += 1
        analyzed_text = djtext
        params = {"cchars": "number of characters", "cwords": "number of words", 'chars': ccount, 'words': wcount,
                  'analyzed_text': analyzed_text}

    # if no switch is on
    if removepunc != "on" and rmnwline != "on" and txtcount != "on" and spaceremove != "on" and captalize != "on":
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)

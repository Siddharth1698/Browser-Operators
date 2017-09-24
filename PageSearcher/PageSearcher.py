import urllib.request
import webbrowser


def UserEnter():
    x = input("What is your Search title ")
    y = int(input("Enter page number"))
    PageSearcher(x,y)


def PageSearcher(a,b):
    SearchName = a
    PageNumber = ((b-1)*10)
    webbrowser.open("https://www.google.co.in/search?q=" + SearchName +"&rlz=1C1CHBF_enIN760IN760&ei=aeTHWcvoO8znvgTl17PQBA&start=" + str(PageNumber) + "&sa=N&biw=1366&bih=662")




UserEnter()


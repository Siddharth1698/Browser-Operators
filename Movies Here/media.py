import webbrowser
class Movie:
   def __init__(self,mtitle,mstory,mimage,mtrailer):
       self.title = mtitle
       self.story = mstory
       self.image = mimage
       self.trailer = mtrailer


   def showtrailer(self):
       webbrowser.open(self.trailer)










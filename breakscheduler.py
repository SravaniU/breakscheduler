import time
import webbrowser
#redting no of hours to schedule
n=int(input('enter for no of hours the break has to be scheduled'))
#reding no of times the break has to be scheduled
m=int(input('enter no of times you want to take the break'))

while(m>0):
    time.sleep(60*60*n)
    webbrowser.open("https://www.youtube.com")
    m=m-1

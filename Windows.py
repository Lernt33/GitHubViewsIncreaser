#Lernt33
import webbrowser, time
import os
print("@Lernt33's first script")

a = input("GitHub nickname: ")
url = "github.com/"+ a +"/"

while True:
 try:
  views = int(input("Views quantity: "))
  break
 except:
  print("\nThat's not a number!\n")

for i in range(views):
 webbrowser.open_new(url)
 time.sleep(0.5)

time.sleep(3)
os.system("taskkill /im msedge.exe /f")
webbrowser.open_new("https://"+url)

import time
import win10toast
import sys
import playsound

x = input('Enter(hours:minutes:seconds)')
hours = int(x[:2])
minutes = int(x[3:5])
sec = int(x[6:8])
sec = (hours * 3600) + (minutes * 60) + sec
for i in range(sec, 0, -1):
    i -= 1
    sys.stdout.write("\r{0}".format(i))
    sys.stdout.flush()
    time.sleep(1)
toaster = win10toast.ToastNotifier()
toaster.show_toast('Python', 'The deed is done', duration=5)
playsound.playsound('rec.mp3')

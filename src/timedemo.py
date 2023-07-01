#from datetime import date
#import time

#print (time.strftime("%H:%M:%S"))
#today = date.today()
#print("Today's date:", today)
import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("log.txt")))
print("Created: %s" % time.ctime(os.path.getctime("log.txt")))

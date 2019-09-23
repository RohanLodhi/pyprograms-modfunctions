import time

epoch=time.time()
print('secs :',epoch)

timetup=time.localtime(epoch) #IST
print('\ntime tuple :',timetup)

usabletime=time.asctime(timetup)
print('\nusable time :',usabletime)

gmtime=time.gmtime(epoch)  #GMT
print('\ngm time :',gmtime)

usablegmtime=time.asctime(gmtime)
print('\nusable gm time :',usablegmtime)

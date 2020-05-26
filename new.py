import os
address_file = open('./addr_file','r')
less_ping = 500
best_server=0
for line in address_file :
    ip=line.strip()
    ping="ping -c2 "+ ip +" | tail -1 | awk '{print $4}' | cut -d '/' -f 2"
    time = os.popen(ping).read()
    time = time.strip()
    if( time == ""):
        continue
    if('.' in time):
        time = int(time[:(time.index('.'))])
    else:
        time = int(time)
    if time < less_ping :
        less_ping = time
        best_server = ip
print(best_server)
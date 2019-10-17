import datetime
l = ['Sun 10 May 2015 13:54:36 -0700',
     'Sun 10 May 2015 13:54:36 -0000']

def time_delta(t1, t2):
    s = '%a %d %b %Y %H:%M:%S %z'
    return str(int(abs((datetime.datetime.strptime(t1, s) - datetime.datetime.strptime(t2, s)).total_seconds())))

print(time_delta(l[0], l[1]))

# create function getSeconds which has hours, minutes and seconds which return total seconds 

def getsecond(hours,minutes,seconds):
    total_second=hours*3600+minutes*60+seconds
    return total_second
print(getsecond(1,60,60))
    
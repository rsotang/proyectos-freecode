def add_time(start, duration,day_of_week=''):
    #we build the clock
    hours = ['12','1','2','3','4','5','6','7','8','9','10','11']

    minutes = ['00','01','02','03','04','05','06','07','08','09']

    meridian = ['AM','PM']

    week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    counter = 10
    while counter <60:
        minutes.append(str(counter))
        counter = counter + 1
    
    
    #parsing of the input to extract useful information
    start_items = start.split()
    start_time = start_items[0].split(':')
    meridian_init = start_items[1]

    hours_init = start_time[0]
    minutes_init = start_time[1]

    plus_time = duration.split(':')
    hours_add = plus_time[0]
    minutes_add = plus_time[1]
    
       
    
    
    #new hour processing 
    minutes_new = int(minutes_init) + int(minutes_add) 
    hours_new = int(hours_init) + int(hours_add)

    meridian_cycles = hours_new // 12
    day_count = int(hours_add)//24
    
    print(meridian_cycles)   
   

    if minutes_new > 59:
        minutes_new = minutes_new - 60
        hours_new = hours_new + 1 
    
    hours_new = hours_new%12
   
    if hours[hours_new] == '12': meridian_cycles =meridian_cycles + 1
    if meridian_init == 'PM': 
        meridian_cycles = meridian_cycles + 1 
    
    print(meridian_cycles)
    meridian_new = meridian_cycles % 2
    print(meridian_new)
    #print(hours_new)
    
    if meridian_init == 'PM' and meridian[meridian_new] == 'AM': 
        day_count = day_count + 1 
    
    
    passed_days_str= ' (' + str(day_count) + ' days later)'
    if day_count ==1 :
        passed_days_str = ' (next day)'
    elif day_count ==0:
        passed_days_str = ''   

    new_time = hours[hours_new] +':'+ minutes[minutes_new]+' '+ meridian[meridian_new]+ passed_days_str

    if day_of_week!= '':
        day_of_week=week.index(day_of_week.casefold())
        day_of_week = (day_count + day_of_week)%7    
        new_time = hours[hours_new] +':'+ minutes[minutes_new]+' '+ meridian[meridian_new]+ ', ' + week[day_of_week].capitalize()+ ' ' + passed_days_str

    return new_time


actual = add_time("11:40 AM", '0:25')
expected = "12:05 PM"

print(actual)
print(expected)

if actual == expected: print('bien')
else: print('mal')
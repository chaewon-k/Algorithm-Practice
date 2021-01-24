def preprocessDate(dates):
    dic = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May': '05', 'Jun':'06',
           'Jul':'07','Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    result = []
    for i in dates:
        temp = i.split(' ')
        if len(temp[0][:-2]) < 2:   day = '0'+temp[0][:-2]
        else:   day = temp[0][:-2]
        result.append(temp[2]+'-'+dic[temp[1]]+'-'+day)
    return result

print(preprocessDate(['20th Oct 2052','6th Jun 1933','26th May 1960','20th Sep 1958',
'16th Mar 2068','25th May 1912','16th Dec 2018','26th Dec 2061','4th Nov 2030',
'28th Jul 1963']))
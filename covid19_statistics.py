regions =['seoul','gyeongi','busan','gyeongnam','incheon','gyeongbuk','daegu','chungnam','jeonnam','jeonbuk','chungbuk','ganwon','daegjeon','gwangju','ulsan','jeju','sejong']
n_people = [9550227,13530519,3359527,3322373,2938429,2630254,2393626,2118183,1838353,1792476,1597179,1536270,1454679,1441970,1124459,675883,365309]
n_covid = [644,529,38,29,148,28,41,62,23,27,27,33,16,40,20,5,4]

def normalize_data(n_case,n_people,scale):
    norm_case=[]
    for idx,n in enumerate(n_case):
        norm_case.append(n/n_people[idx]*scale)
    return norm_case

sum_people = sum(n_people)
sum_covid = sum(n_covid)
norm_covid = normalize_data(n_covid,n_people,1000000)
#print(sum_covid)

print('### Korean Population by Region')
print('* Total population:', sum_people)
print()
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')

for idx,pop in enumerate(n_people):
    ratio = n_people[idx]/sum_people * 100
    print('| %s | %d | %.1f |' % (regions[idx],pop,ratio) )
print(' ')

print('### Korean Covid-19 New Cases by Region')
print('* Total new cases:', sum_covid)
print()
print('| Region | Population | Ratio (%) | New case |')
print('| ------ | ---------- | --------- | -------- |')

for idx,pop in enumerate(n_covid):
    ratio = n_covid[idx]/sum_covid * 100
    print('| %s | %d | %.1f | %1.f |' % (regions[idx],pop,ratio,norm_covid[idx]))
print(' ')

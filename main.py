'''
1. Выполните задание уровня light
2. Замерьте время генерации отчета (время выполнения пункта 3).
3. В каждый файл из задания Light добавьте параметр: время, затраченное на генерацию отчета.
'''
import datetime, time
from datetime import timedelta
import csv
import json

def getContext( data ):
    rez=[]
    dic = {
        'model': '',
        'volume': '',
        'type': '',
        'power': '',
        'transmission': '',
        'ntransmission': '',
        'drive': '',
        'body': '',
        'country': ''
    }
    i = 0
    with open( data, 'r', encoding='utf8' )  as  f:
        s = f.read()
        lst = s.split('\n')


    for v in dic.keys():
        d = {'character':v, 'val':lst[i] }
        rez.append( d )
        dic[v] = lst[i]
        i += 1

    return rez, dic

# чтение данных
lst, dic = getContext(  'dataauto.txt')   # lst для CSV, dic для JSON

#print(lst)
#print(dic)
#*********************************************************************** CSV

tim10 = time.perf_counter_ns()
namField = ['character', 'val']

with open( 'auto.csv','w', newline='', encoding='utf8' ) as f:
    w = csv.DictWriter( f, delimiter=',', fieldnames=namField )
    w.writeheader()

    w.writerows( lst )
    # или
    # for i in range(len(lst)):
    #     w.writerow( lst[i] )
    #     print( lst[i])

# время окончания формирования отчета и дозапись
tim11 = time.perf_counter_ns()
t = tim11-tim10
#print( t )

with open( 'auto.csv','a', newline='', encoding='utf8' ) as f:
    f.write( 'time,'+str(t) )

#******************************************************* JSON
tim20 = time.perf_counter_ns()  # начало

with open(  'auto.json', 'w', encoding='utf8' )  as f:
    json.dump( dic, f , ensure_ascii=False)   # ensure_ascii=False - для запрета экранирования символов не ASCII

tim21 = time.perf_counter_ns()   # окончание

# дозапись времени
with open(  'auto.json', 'r', encoding='utf8' )  as f:
    data = json.load(f)
data['time']=tim21-tim20
with open(  'auto.json', 'w', encoding='utf8' )  as f:
    json.dump( data, f , ensure_ascii=False)

print(  'csv:',tim11-tim10,'JSON:',tim21-tim20, 'наносекунд')
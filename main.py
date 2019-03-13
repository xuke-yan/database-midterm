import sqlite3
import timeit

def indexNo():
    conn = sqlite3.connect('midterm')
    curs = conn.cursor()
    curs.execute('select distinct B,H \
                from R1 inner join R21 inner join R22 inner join R3\
                where R21.G= "low" AND (A="med" OR A="high")')
    conn.commit()

def indexA():
    conn = sqlite3.connect('midterm')
    curs = conn.cursor()
    curs.execute('select distinct B,H\
                from R1 inner join R21 inner join R22 inner join R3\
                where R21.G= "low" AND (A="med" OR A="high")')
    conn.commit()
    
def indexG():
    conn = sqlite3.connect('midterm')
    curs = conn.cursor()
    conn.commit()
    curs.execute('select distinct B,H\
                from R1 inner join R21 inner join R22 inner join R3\
                where R21.G= "low" AND (A="med" OR A="high")')
    conn.commit()

def indexAandG():
    conn = sqlite3.connect('midterm')
    curs = conn.cursor()
    curs.execute('select distinct B,H\
                from R1 inner join R21 inner join R22 inner join R3\
                where R21.G= "low" AND (A="med" OR A="high")')
    conn.commit()

def indexAG():
    conn = sqlite3.connect('midterm')
    curs = conn.cursor()
    curs.execute('create index tag_AG on data (A, G)')
    conn.commit()
    curs.execute('select distinct B,H\
                from R1 inner join R21 inner join R22 inner join R3\
                where R21.G= "low" AND (A="med" OR A="high")')
    conn.commit()
    

if __name__ == '__main__':

    print('No index condition:')
    print(timeit.timeit(stmt='indexNo()', number =1, setup='from __main__ import indexNo'))
    print('Index on A condition:')
    print(timeit.timeit(stmt='indexA()', number =1, setup='from __main__ import indexA'))
    print('Index on G condition:')
    print(timeit.timeit(stmt='indexG()', number =1, setup='from __main__ import indexG'))
    print('Seperate index on A and G condition:')
    print(timeit.timeit(stmt='indexAandG()', number =1, setup='from __main__ import indexAandG'))
    print('Composite index on both A and G condition:')
    print(timeit.timeit(stmt='indexAG()', number =1, setup='from __main__ import indexAG'))
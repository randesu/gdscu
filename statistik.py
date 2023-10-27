person1 = {
    'no' : 1,
    'nama' : 'nanda',
    'tabungan' : 50000000,
    'aset' :"rumah,mobil,motor",
    'totalkekayaan' : 5000000000,
    'kelas' : 'atas'
}

person2 = {
    'no' : 2,
    'nama' : 'josua',
    'tabungan' : 100000000,
    'aset' :"rumah,mobil,motor",
    'totalkekayaan' : 1000000000,
    'kelas' : 'atas'
}

person3 = {
    'no' : 3,
    'nama' : 'ahmmad',
    'tabungan' : 2000000000,
    'aset' :"rumah,motor",
    'totalkekayaan' : 5000000000,
    'kelas' : 'atas'
}

person4 = {
    'no' : 4,
    'nama' : 'falah',
    'tabungan' : 10000000,
    'aset' :"rumah,motor",
    'totalkekayaan' : 300000000,
    'kelas' : 'bawah'
}

person5 = {
    'no' : 5,
    'nama' : 'adit',
    'tabungan' : 150000000,
    'aset' :"rumah,mobil,motor",
    'totalkekayaan' : 4500000000,
    'kelas' : 'atas'
}
person6 = {
    'no' : 6,
    'nama' : 'soqi',
    'tabungan' : 20000000,
    'aset' :"rumah,motor",
    'totalkekayaan' : 900000000,
    'kelas' : 'bawah'
}

person7 = {
    'no' : 7,
    'nama' : 'leo',
    'tabungan' : 50000000,
    'aset' :"rumah,mobil,motor",
    'totalkekayaan' : 2000000000,
    'kelas' : 'atas'
}

person8 = {
    'no' : 8,
    'nama' : 'firly',
    'tabungan' : 75000000,
    'aset' :"rumah,mobil,motor",
    'totalkekayaan' : 3000000000,
    'kelas' : 'atas'
}

person9 = {
    'no' : 9,
    'nama' : 'okta',
    'tabungan' : 30000000,
    'aset' :"rumah,mobil,motor",
    'totalkekayaan' : 500000000,
    'kelas' : 'bawah'
}

person10 = {
    'no' : 10,
    'nama' : 'nandi',
    'tabungan' : 5000000,
    'aset' :"rumah,motor",
    'totalkekayaan' : 600000000,
    'kelas' : 'bawah'
}

gdscu ={
    1 : person1,
    2 : person2,
    3 : person3,
    4 : person4,
    5 : person5,
    6 : person6,
    7 : person7,
    8 : person8,
    9 : person9,
    10 : person10
}


def minvalue(data,target):
    minlist = []
    templist = []
    for i in range (1, len(gdscu)+1):
        a = data[i][target]
        templist.append(a)

        # print(a)
        # print(i)
        # print(templist)

    swapped = False
    minlist = templist
    # print(minlist)
    for j in range(0,len(minlist)-1):
        for k in range(0,len(minlist)-1):
            # print(minlist[k])
            if minlist[k] > minlist[k+1]:
                swapped = True
                minlist[k],minlist[k+1] = minlist[k+1], minlist[k]
                # print(minlist)
            # if swapped == False:
            #     break
    minimalvalue = minlist[0]
    print(minlist)
    print(minimalvalue)
    

# mintabungan(gdscu,'tabungan')

def maxvalue(data,target):
    maxlist = []
    templist = []
    for i in range (1, len(data)+1):
        a = data[i][target]
        templist.append(a)

        # print(a)
        # print(i)
        # print(templist)

    swapped = False
    maxlist = templist
    # print(maxlist)
    for j in range(0,len(maxlist)-1):
        for k in range(0,len(maxlist)-1):
            # print(minlist[k])
            if maxlist[k] < maxlist[k+1]:
                swapped = True
                maxlist[k],maxlist[k+1] = maxlist[k+1], maxlist[k]
                # print(maxlist)
            # if swapped == False:
            #     break
    maximalvalue = maxlist[0]
    print(maxlist)
    print(maximalvalue)

# minvalue(gdscu,'totalkekayaan')
# maxvalue(gdscu,'tabungan')

def modevalue(data, target):
    tempdata1 = {}
    tempdata2 = {'value' : 0,
                'count': 0}
    templist = []
    anotherlist = []
    counter = 0
    for i in range (1,len(gdscu)+1):
        a = gdscu[i][target]
        # print(a)
        templist.append(a)
    print(templist)
    print('-----------------------')
    for j in templist:
        number = j
        anotherlist.append(number)
        for k in templist:
            if k in anotherlist:
                counter += 1
                # print(counter)
                data = {'value':number,'count':counter}
                tempdata1.update(data)
                # print(tempdata1)
            if tempdata2['count'] < tempdata1['count']:
                tempdata2.update(data)
                # print(tempdata2)
        anotherlist=[]
        counter = 0
        tempdata1 = {'value':0,
                    'count' : 0}
    
    print(tempdata2)

        
# modevalue(gdscu,'totalkekayaan')


def meanvalue(data,target):
    values = []
    for i in range(1,len(data)+1):
        check = data[i][target]
        values.append(check)
    # values.pop(0)
    print(values)
    a = len(values)
    print(a)
    if a % 2 == 0:
        firstmean = int(a/2)
        secondmean = firstmean+1
        # print(firstmean)
        firstvalue = values[firstmean-1]
        secondvalue = values[secondmean-1]
        # print(firstvalue)
        # print(secondvalue)
        result = (firstvalue+secondvalue)/2
        print(result)
    elif a%2 == 1:
        locate = a/2
        locate = locate+0.5
        print(values[int(locate-1)])

meanvalue(gdscu,'tabungan')





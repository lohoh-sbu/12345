def s(q):
    onetwofreefour =q//10000

    twofreefourone =(q%10000) //1000

    freefouronetwo =(q%1000) //100

    fouronetwotree =(q%100) //10

    fivefourtreetwoone =q%10

    reversedlohoh = onetwofreefour*1+twofreefourone*10+freefouronetwo*100+fouronetwotree*1000+fivefourtreetwoone*10000
    return reversedlohoh
q =int(input('введіть 5-х значне'))
reversedlohoh =s(q)
print(reversedlohoh)
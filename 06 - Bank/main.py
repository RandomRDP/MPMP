

def test_ans(D1_deposit,D2_deposit):
    def newday(d,y,t,te):
        d += 1
        te = t
        t += y
        y = te
        #print("day: {} balance: {}".format(d,t))
        return d,y,t,te

    days = 2
    yesturday_balance = D1_deposit
    today_balance = D2_deposit + D1_deposit
    temp_balance = 0


    while today_balance < 999999:
        days,yesturday_balance,today_balance,temp_balance = newday(days,yesturday_balance,today_balance,temp_balance)


    if today_balance == 1000000:
        print("days:{}, balance:{}, D1:{}, D2:{}".format(days,today_balance,D1_deposit,D2_deposit))


for i in range(1,10000):
    for j in range(0,10000):
        test_ans(i,j)

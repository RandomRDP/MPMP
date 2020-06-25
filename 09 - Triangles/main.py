GOAL = 14

class triangle:

    def __init__(self,list):
        self.Nums = [0,0,0]
        self.Next_Nums = [0,0,0]
        self.Nums_total = 0
        self.Next_Nums_total = 0
        for i in range(0,3):
            self.Nums[i] = list[i]
            self.Nums_total += self.Nums[i]

    def calculate(self):
        self.Next_Nums[0] = abs(self.Nums[0] - self.Nums[2])
        self.Next_Nums[1] = abs(self.Nums[0] - self.Nums[1])
        self.Next_Nums[2] = abs(self.Nums[1] - self.Nums[2])
        self.Next_Nums_total = self.Next_Nums[0]+self.Next_Nums[1]+self.Next_Nums[2]

    def set_nums(self,list):
        self.Nums_total = 0
        for i in range(0,3):
            self.Nums[i] = list[i]
            self.Nums_total += self.Nums[i]

def test_triangle(list):
    global GOAL
    T1 = triangle(list)
    #T2 = triangle(list)
    p_total = -1
    pp_total = -2
    ppp_total = -3
    while True:
        T1.calculate()
        if T1.Next_Nums_total < GOAL:
            # print ("Nope start:{} end:{}".format(list,T1.Next_Nums))
            break
        if p_total == pp_total == ppp_total == T1.Next_Nums_total :
            if p_total == GOAL:
                print ("Soultion {} {} {}".format(T1.Next_Nums_total, list, T1.Next_Nums))
            break
        ppp_total = pp_total
        pp_total = p_total
        p_total = T1.Next_Nums_total
        T1.set_nums(T1.Next_Nums)
#        print("1p{} 2p{} 3p{} l{}".format(p_total,pp_total,ppp_total,T1.Next_Nums))

for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            if i+j+k != GOAL:
                test_triangle([i,j,k])


#test_triangle([12,5,7])

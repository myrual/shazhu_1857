# coding=utf-8
"""
if  start time < infotime < endtime
    bonus
    freecounter_rate
    cheapercounter_rate
    cheaperprice
    laterprice = earlierprice 
    前复权：复权后价格＝[(earlierprice-bonus)＋cheaperprice*cheapercounter]÷(1＋cheaperaccount_rate+freecounter_rate) 
            fq_1 prince =  (earlierprice-bonus)
            fq_2 price  =  (fq_1 price)/(1+free_rate)
            fq_3 = fq_2
    return fq_3
else
"""    

STDTFQinfo = [[20110617, 0.3, 0, 0.6, 0, 0]]

def SingleFuqian_Forward(FQinfo):
    """FQinfo is : [time(trade time), free(how many), gift(How many), bonus(how much), cheaper_price(how much), cheaper_count(how many)]
    """
    print FQinfo
    earlierprice = 27.54
    bonus = FQinfo[3]
    free = FQinfo[1]
    gift = FQinfo[2]
    cheaper_price = FQinfo[4]
    cheaper_count = FQinfo[5]
    fq_1 = (earlierprice - bonus)
    fq_2 = (fq_1)/(1 + free + gift) 
    fq_3 = ((fq_2) + cheaper_price*cheaper_count)/(1+cheaper_count)
    return fq_3/earlierprice 
def periodFuquan_factor_Forward(FQPeriodTable):
    result = 1
    if type(FQPeriodTable[0]) == type([]):
        for i in FQPeriodTable:
            result = result * SingleFuqian_Forward(i)
    else:
        result = result * SingleFuqian_Forward(FQPeriodTable)
    return result
print periodFuquan_factor_Forward(STDTFQinfo)

def change(cost, money):
    #money is the money that is returned
    coins={'penny':0.01, 'nickel':0.05, 'dime':0.1,'quarter':0.25}
    num_quarters=0
    num_dimes=0
    num_nickels=0
    num_pennies=0
    change=money-cost
    if int(change) >= 1.0:
        num_quarters+=int(change/coins['quarter'])
        change-=num_quarters*0.25
    if round(change, 1) >=0.10:
        num_dimes+=round(change,1)/coins['dime']
        change-=num_dimes*0.1
    if round(change,2) <= 0.1 and round(change,2) >=0.05:
        num_nickels+=round(change, 2)/coins['nickel']
        change-=num_nickels*0.05
    if round(change,2) <=0.05 and round(change,2) >=0.01:
        num_pennies+=round(change,2)/coins['penny']
        change-=num_pennies*0.01
    print('quarters: ' + str(num_quarters))
    print('dimes: ' + str(num_dimes))
    print('nickels: '+ str(num_nickels))
    print('pennies: '+ str(num_pennies))
    
        

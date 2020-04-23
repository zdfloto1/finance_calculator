def future_value(principal,int_rate,years,monthly_contrib=0):
    
    monthly_rate = int_rate/12
    
    months = years * 12
    
    for i in range(months):
        principal = principal + monthly_contrib
        principal = principal * (1 + monthly_rate)
        
    return principal

def retirement_calculator(current_age,retirement_age,monthly_contribution,interest_rate):
    
    difference = retirement_age - current_age
    
    retirement_amount = future_value(0,interest_rate,difference,monthly_contribution)
    
    return retirement_amount
    
    
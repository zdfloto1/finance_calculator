market_returns = [-9.02, 28.88, -6.24, 19.42, 9.54, -0.73, 11.39, 29.6, 13.41, 0.0, 12.78, 23.45, -38.49, 3.53, 13.62, 3.0, 8.99, 26.38, -23.37, -13.04, -10.14, 19.53, 26.67, 31.01, 20.26, 34.11, -1.54, 7.06, 4.46, 26.31, -6.56, 27.25, 12.4, 2.03, 14.62, 26.33, 1.4, 17.27, 14.76, -9.73, 25.77, 12.31, 1.06, -11.5, 19.15, 31.55, -29.72, -17.37, 15.63, 10.79, 0.1, -11.36, 7.66, 20.09, -13.09, 9.06, 12.97, 18.89, -11.81, 23.13, -2.97, 8.48, 38.06, -14.31, 2.62, 26.4, 45.02, -6.62, 11.78, 16.46, 21.78, 10.26, -0.65, 0.0, -11.87, 30.72, 13.8, 19.45, 12.43, -17.86, -15.29, -5.45, 25.21, -38.59, 27.92, 41.37, -5.94, 46.59, -15.15, -47.07, -28.48, -11.91, 37.88]

def future_value(principal,int_rates,years,monthly_contrib=0):
    
    for y in range(years):
        print('rate: ' + str(int_rates[y]))
        monthly_rate = int_rates[y]/12
        for i in range(12):
            principal = principal + monthly_contrib
            principal = principal * (1 + monthly_rate)
        
    return principal

def retirement_calculator(current_age,retirement_age,monthly_contribution):
    
    difference = retirement_age - current_age
    
    interest_rates = getting_returns(difference)
    
    retirement_amount = future_value(0,interest_rates,difference,monthly_contribution)
    
    return retirement_amount

def getting_returns(years):
    std,avg = get_stats()
    import numpy
    returns = []
    for i in range(years):
        returns.append(numpy.random.normal(avg,std)/100)
    return returns

def get_stats():
    import statistics
    standard_deviation = statistics.stdev(market_returns)
    average = statistics.mean(market_returns)
    return standard_deviation,average
    
    
def calculate_probability (favorable_outcomes, total_outcomes): 
if total_outcomes == 0: 
return 0   
return favorable_outcomes / total_outcomes 

total_outcomes = 6 

favorable_outcomes = 1 
       
probability = calculate_probability (favorable_outcomes, total_outcomes) 
print (f"The probability of rolling a 3 is: {probability:.2f}") 


b.   Applications of probability distribution to real life applications. 
from scipy.stats import poisson 
avg_arrival_rate = 5  
real_time_calls = 8 
call_prob = poisson.pmf(real_time_calls, avg_arrival_rate) 
print(f"Probability of receiving {real_time_calls} calls in a minute: {call_prob:.4f}") 
if real_time_calls > 6: 
print("High traffic! Consider adding more staff.") 
else: 
print("Traffic is normal.")
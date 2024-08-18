def compute_pay(hours_worked, hourly_rate):
    
    regular_hours = 40
    overtime_rate = 1.5
    
    if hours_worked > regular_hours:
        
        regular_pay = regular_hours * hourly_rate
       
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * hourly_rate * overtime_rate
      
        total_pay = regular_pay + overtime_pay
    else:
        
        total_pay = hours_worked * hourly_rate
    
    return total_pay

pay = compute_pay(45, 10)
print(pay)

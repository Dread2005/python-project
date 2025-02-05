#day 10 functions with input(Leap year calculator part 2)

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


  
# TODO: Add more code here 👇
def days_in_month(The_year, The_month):
  month_days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year)==True:
    return 29
  else:
    return month_days[month]
  
  
  
    

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)


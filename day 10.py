
def is_leap(year):
  year = True
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return year == True
      else:
        return year == False
    else:
      return year == True
  else:
    return year == False


  
# TODO: Add more code here 👇
def days_in_month(days, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  The_year = year
  The_month = month
  is_leap(year)
  if is_leap(year) == True:
    month_days.index[1] = 29
  
  
    

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)
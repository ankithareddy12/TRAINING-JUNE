s=7262
h=s//3600
m=(s%3600)//60
s=s%60
print(h,m,s)



l=[4,3,7]
x=16
l=sorted(l)
print(l)
for i in l:
    print(x%i)
    
    
    



def convert_days(total_days):
    years = total_days // 360
    remainder_after_years = total_days% 360
    months = remainder_after_years // 30
    remainder_after_months = remainder_after_years % 30
    weeks = remainder_after_months // 6
    days = remainder_after_months % 6
    return f"{years}y/{months}m/{weeks}w/{days}d"
total_days = 65476
result = convert_days(total_days)
print(result)












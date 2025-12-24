print("---Age in Days,Mouths,Hours,Minutes,Seconds calculator---")
age_in_years  = float(input('enter your age in years:'))
Day =age_in_years * 365.25
print("you have lived for",Day ,"Days")

Month =age_in_years*12
print("you have lived for",Month ,'Months')

Hour =Day* 24
print('you have lived for',Hour ,'Hours')

Minute =Hour* 60
print('you have lived for',Minute ,'Minutes')

Second =Minute* 60
print('you have lived for',Second ,'Seconds')
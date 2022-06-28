# https://www.joshuakennon.com/the-average-person-lives-27375-days-make-each-of-them-count/
# The Average Person Lives 27,375 Days. Make Each of Them Count.

AVERAGE_DAYS = 27375

year = input("What year were you born in? ")
month = input("Month? ")
day = input("Day? ")

days_lived = (2022-int(year))*365 + (int(month) * 30) + int(day)
print("Days lived: ", days_lived)
print("Days left to live : ", AVERAGE_DAYS - days_lived)

#TODO add leap years
#TODO days per month

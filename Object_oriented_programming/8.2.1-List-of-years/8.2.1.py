"""Please write a function named list_years(dates: list) which takes a list of date 
type objects as its argument. The function should return a new list, which contains 
the years in the original list in chronological order, from earliest to latest."""

from datetime import date

def list_years(dates: list):
    year1 = date1.year
    year2 = date2.year
    year3 = date3.year

    new_list = sorted([year1, year2, year3])
    
    return new_list

date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)
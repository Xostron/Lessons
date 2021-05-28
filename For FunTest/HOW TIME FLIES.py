"""
Example 1:

Input:
01.01.2000
01.01.2016

Output:
16 years, total 5844 days

Example 2:

Input:
15.12.2014
14.02.2016

Output:
1 year, 1 month, total 426 days

Example 3:

Input:
01.01.2016
18.08.2016

Output:
7 months, total 230 days



"""
from datetime import *
import sys
from dateutil.relativedelta import relativedelta

data1 = [int(i) for i in input().split('.')]
data2 = [int(i) for i in input().split('.')]



begin = datetime(data1[2], data1[1], data1[0],)

end = datetime(data2[2], data2[1], data2[0],)

difference = relativedelta(end, begin)


print((f"{difference.years} years, " if difference.years>1 else f"{difference.years} year, " if difference.years==1 else '') +
      (f"{difference.months} months, " if difference.months>1 else f"{difference.months} month, " if difference.months==1 else '') +
      (f"total {(end-begin).days} days" ))


"""
example:

print(((f"{difference.years} year"+ 's'*(difference.years>1)+', ')*(difference.years>=1)) +
      (f"") +
      (f"total {(end-begin).days} days"))
"""
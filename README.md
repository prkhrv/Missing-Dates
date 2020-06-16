# Missing Dates Problem

![Python application](https://github.com/prkhrv/Missing-Dates/workflows/Python%20application/badge.svg)

Missing Dates Problem is basically to fill the missing data in the database and replace it with Average Data.

## Problem Statement
"Given a dictionary D where key is of form  YYYY-MM-DD and its corresponding value is an integer, returns a new Dictionary D with missing dates values which are average of prev and next  date values"

## Test Cases
### Case 1
```
Input 1 : {'2019-01-01':100,'2019-01-04':115}
Desired Output : {'2019-01-01':100,'2019-01-02':105,'2019-01-03':110,'2019-01-04':115}
```
### Case 2

```
Input 2 : {'2019-01-10':10,'2019-01-11':20,'2019-01-13':10}
Desired Output : {'2019-01-10':10,'2019-01-11':20,'2019-01-12':15,'2019-01-13':10}
```

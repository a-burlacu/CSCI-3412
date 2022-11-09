"""
Name: Alina Burlacu
ID: 109129252
Date: 09/27/2022
Assignment: HW2 - Part 1 - Algorithm efficiency comparison
Description: For each function f(n) and time ,t, in the following table, determine the largest size, n, of a problem that
             can be solved in time, t, assuming that the algorithm to solve the problem takes f(n) microseconds.
             It will display the output in a table in HTML.
"""
import decimal
import math
import webbrowser
import numpy as np
import pandas as pd
from scipy.special import lambertw

# time interval in microseconds
tsec = pow(10, 6)
tmin = 60 * tsec
thour = 3600 * tsec
tday = 86400 * tsec
tmonth = 30 * tday
tyear = 365 * tday
tcentury = 100 * tyear

tlist = [tsec,tmin,thour,tday,tmonth,tyear,tcentury]


# function to determine if output is integer or scientific notation
def int_or_sci(x):
    if x >= math.pow(10,6):
        x = '%.1E' % decimal.Decimal(x)
    else:
        x = int(x)
    return x



############################### log (n) ######################################
fn1 = ["lg(n)"]
for t in tlist:
    x = int_or_sci(t)
    fn1.append("2^%s" %x)

############################### sqrt(n) #####################################
f = lambda n : n**2
fn2 = ["sqrt(n)"]
for t in tlist:
    fn = f(t)
    x = int_or_sci(fn)
    fn2.append("%s" % x)

################################# n #########################################
fn3 = ["n"]
for t in tlist:
    x = int_or_sci(t)
    fn3.append("%s" %x)

################################ n log (n) ##################################
f = lambda n : n * math.log(2)
fn4 = ["n lg n"]

for t in tlist:
    fn = f(t)
    fnw = math.exp(lambertw(fn))
    x = int_or_sci(fnw)
    fn4.append("%s" % x)

############################### n^2 #####################################
f = lambda n : n**(1/2)
fn5 = ["n^2"]
for t in tlist:
    fn = f(t)
    x = int_or_sci(fn)
    fn5.append("%s" %x)

############################### n^3 #####################################
f = lambda n : n**(1/3)
fn6 = ["n^3"]
for t in tlist:
    fn = f(t)
    x = int_or_sci(fn)
    fn6.append("%s" %x)

################################# 2^n ###################################
f = lambda n : math.log(n,2)
fn7 = ["2^n"]
for t in tlist:
    fn = f(t)
    x = int_or_sci(fn)
    fn7.append("%s" %x)

############################## n! ########################################
def factorial_cap(num):
    n = 1
    i = 1
    while n < num:
        i += 1
        n *= i
    return i

fn8 = ["n!"]
for t in tlist:
    fn8.append(factorial_cap(t))

############################# HTML Output ############################################
def html():

    # 'base' is the main chunk of the html file, must be first to print to file
    base = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Running Time Table</title>
     <style>
      body {
          margin: 15px;
          font-family: Verdana;
          font-size: 14px;
          font-weight: 500;
        }
        table, th, td {
            border: 2px solid black;
             border-collapse: collapse;
             font-size: 16px;}
    </style>
    </head>
    <body>
    <h1> Comparison of Running Times: </h1>
     <table style="width:70%">
        <tr style="height:40px">
            <th>  </th>
            <th>1 second</th>
            <th>1 minute</th>
            <th>1 hour</th>
            <th>1 day</th>
            <th>1 month</th>
            <th>1 year</th>
            <th>1 century</th>
        </tr>
        <tr style="height:40px">
    """

    # 'cell' is what will hold each value from the array as it is iterated over
    cell = """
            <td style="text-align:center">{}</td>
            """

    # adds in the html code to end a row and start on a new one (sort of acting like the '\n')
    new_row = """
        </tr>
        <tr style="height:40px">
            """

    # the end of the html code, closes the table
    end = """
        </tr>
    </table>
    </body>
    </html>
    """

    #   create a new empty string for each row of the table

    row0, row1, row2, row3, row4, row5, row6, row7 = '', '', '', '', '', '', '', ''

    # a for loop will iterate over the row's index and return a new 'cell' for each item

    for i in range(len(fn1)):
        row0 = row0 + cell.format(fn1[i])

    for i in range(len(fn2)):
        row1 = row1 + cell.format(fn2[i])

    for i in range(len(fn3)):
        row2 = row2 + cell.format(fn3[i])

    for i in range(len(fn4)):
        row3 = row3 + cell.format(fn4[i])

    for i in range(len(fn5)):
        row4 = row4 + cell.format(fn5[i])

    for i in range(len(fn6)):
        row5 = row5 + cell.format(fn6[i])

    for i in range(len(fn7)):
        row6 = row6 + cell.format(fn7[i])

    for i in range(len(fn8)):
        row7 = row7 + cell.format(fn8[i])

    # this creates the html file, it can be opened by itself,
    #      but the driver function will open a browser window

    # add the 'base' first then alternate between a 'row#' and a 'new_row' then add 'end' last
    with open("table.html", 'w') as f:
        f.write(base +
                row0 +
                new_row +
                row1 +
                new_row +
                row2 +
                new_row +
                row3 +
                new_row +
                row4 +
                new_row +
                row5 +
                new_row +
                row6 +
                new_row +
                row7 +
                end)


# driver function & display table in browser
html()
webbrowser.open_new_tab('table.html')

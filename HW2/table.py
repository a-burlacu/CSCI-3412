import numpy as np
import webbrowser

itemArray = np.array([["lg n", "b", "c", "123", "b", "c", "123", "aaa"],
                      ["sqrt(n)", "b", "c", "123", "b", "c", "123", "aaa"],
                      ["n", "e", "f", "456", "b", "c", "123", "aaa"],
                      ["n lg n", "h", "i", "789", "b", "c", "123", "aaa"],
                      ["n^2", "k", "l", "100", "b", "c", "123", "aaa"],
                      ["n^3", "k", "l", "100", "b", "c", "123", "aaa"],
                      ["2^n", "k", "l", "100", "b", "c", "123", "aaa"],
                      ["n!", "k", "l", "100", "b", "c", "123", "aaa"]])
def main():
    # create a 2D array of items using numpy (this can be any size array, each row is enclosed in [] )



    # this is where we create the HTML table

    # 'base' is the main chunk of the html file, must be first to print to file
    base = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Running Time Table</title>
     <style>
      body {
          margin: 15px;
          font-family: Helvetica, sans-serif;
          font-size: 14px;
        }
        table, th, td { 
            border: 1px solid black;
             border-collapse: collapse;
             font-size: 16px;}
    </style>
    </head>
    <body>
    <h1> Comparison of Running Times: </h1>
     <table style="width:80%">
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

    for i in range(len(itemArray)):
        row0 = row0 + cell.format(itemArray[0][i])

    #           sample output for 'row0':
    #
    # <td style ="text-align:center"> a </td>
    #
    # <td style ="text-align:center"> b </td>
    #
    # <td style ="text-align:center"> c </td>
    #
    # <td style ="text-align:center"> 123 </td>

    for i in range(len(itemArray)):
        row1 = row1 + cell.format(itemArray[1][i])

    for i in range(len(itemArray)):
        row2 = row2 + cell.format(itemArray[2][i])

    for i in range(len(itemArray)):
        row3 = row3 + cell.format(itemArray[3][i])

    for i in range(len(itemArray)):
        row4 = row4 + cell.format(itemArray[4][i])

    for i in range(len(itemArray)):
        row5 = row5 + cell.format(itemArray[5][i])

    for i in range(len(itemArray)):
        row6 = row6 + cell.format(itemArray[6][i])

    for i in range(len(itemArray)):
        row7 = row7 + cell.format(itemArray[7][i])

    # this creates the html file
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


# driver function & display table
main()
webbrowser.open_new_tab('table.html')






######### some extra for loops just in case ###########


# this prints every item in array in order (i.e. itemArray[0][0] itemArray[0][1]...etc.)
#
# for i in range(len(itemArray)):
#     for j in range(len(itemArray[i])):
#         print(itemArray[i][j])

# # this prints every item in first row in order
#
# for i in range(len(itemArray) + 1):
#     print(itemArray[0][i])
#
# # this prints every item in second row in order
#
# for i in range(len(itemArray) + 1):
#     print(itemArray[1][i])

#######################################################

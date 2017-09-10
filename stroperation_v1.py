#! usr/bin/env python3


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0]*len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if colWidths[i] < len(table[i][j]):
                colWidths[i] = len(table[i][j])

    print(colWidths)

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidths[j]) + ' ', end='')
        print('')

printTable(tableData)


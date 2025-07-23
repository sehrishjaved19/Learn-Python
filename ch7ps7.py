'''Write a program to print the following pattern
####################
#                  #
#                  #
#                  #
#                  #
#                  #
#                  #
#                  #
#                  #
####################
'''

rows = 10
cols = 20



for i in range(rows):
    if i==0 or i ==rows-1:
        print('#'*cols) #top or bottom row:all#
    else:
        print('#'+(' '*(cols-2))+'#')# middle rows: # + space + #
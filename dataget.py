'''
@Authors: 1daIas and 

Created : 2021-02-04

This file is responsible for the collection and assortment
of game data from the League of Legends API.
'''

import pandas
import os

'''
This method will be changed once the main program is implemented
'''

def find_summoner():
    if(not os.path.isfile('users.txt')):
      f = open('users.txt')
      f.close()
  
    use_name = input('Would you like to check a saved user? (y/n)\n (Any other input will quit)')

    if(use_name == 'y'):
        f = open('users.txt', 'r')

        print('Enter the number next to the name you want to use')
        
        name_ind = 1
        
        for name in f:
            print('(%d) %s' % (name_ind, name))
            name_ind += 1
        
        select = input()
        while(int(select) > name_ind - 1):
            select = input('Please enter the number associated with the user to check\n')

        f.seek(0)        
        names = f.readlines()
        summoner_name = names[int(select)-1]
        summoner_name = summoner_name.rstrip()
        f.close
    if(use_name == 'n'):
        new_inp = input('Would you like to quit(q) or enter a new summoner name(n)?')
        while new_inp != 'q' or new_inp != 'n':
            new_inp = input("Invalid input. Please enter 'q' to quit or 'n' to enter a new name: ")

        if(new_inp == 'q'):
                quit()
        elif(new_inp == 'n'):
            summoner_name = input('Enter your summoner name:\n')
    else:
        quit()
return summoner_name



if __name__ == "__main__":

    '''
    Placeholder definitions and variables for now.
    Will later get summoner name and other information
    related to a query from a the main program
    '''

    summoner_name = find_summoner()

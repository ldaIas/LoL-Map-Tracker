'''
@Authors: 1daIas and MatthewL-1

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

def save_summoner(summoner_name):
    with open('users.txt') as users:
        names = users.readlines()
        for name in names:
            if name.rstrip() == summoner_name:
                return
        save_name = input('Would you like to store this user? (y/n)\n')
        if save_name == 'y':
            f = open('users.txt', 'a')
            f.write(summoner_name + '\n')
            f.close()

def validate_request(request):
    try:
        code = request['status']['status_code']
        if(code == 403):
            print('Error while trying to complete request:')
            print(code, ':', request['status']['message'])
            print('Most likely cause: Bad API key')
            return 403
        if(code == 404):
            print('Error while trying to complete request:')
            print(code, ':', request['status']['message'])
            print('Most likely cause: Bad summoner name')
            return 404
        if(code == 429):
            print('Error while trying to complete request:')
            print(code, ':', request['status']['message'])
            print('Most likely cause: Rate limit exceeded')
            return 429
    except:
        return 0

def wait_for_api(wait_time):
    inp = ' '
    while (inp != 'w' or inp != 'q'):
        inp = input('Would you like to wait(w)), or end the program now?(q)')        
    if(inp == 'w'):
          print('Waiting for API limit to reset...')
          time_to_wait = wait_time
          while time_to_wait > 0:
                print('Time: %d seconds' % (time_to_wait))
                time.sleep(1)
                time_to_wait -= 1
    if(inp == 'q'):
        quit()

def validate_name(region_url, name_get, summoner_name, api_key):
        validName = False
    while validName != True:

        request_string = region_url + name_get + summoner_name + api_key
        request = requests.get(request_string)
        request_json = json.loads(request.text)
    
        valid_code = validate_request(request_json)
    
        if(valid_code == 403):
            api_inp =  input("Enter the api key:\n")
            api_key = api_url + api_inp
        if(valid_code == 404):
            print("Name input: '%s'" % (summoner_name))
            summoner_name = find_summoner()
        if(valid_code == 429):
            wait_for_api(2 * 60)
        if(valid_code == 0):
            return True    



if __name__ == "__main__":

    '''
    Placeholder definitions and variables for now.
    Will later get summoner name and other information
    related to a query from a the main program
    '''
    region_url = 'https://na1.api.riotgames.com/'
    name_get = "lol/summoner/v4/summoners/by-name/"
    api_url = "?api_key="
    api_inp =  input("Enter the api key:\n")
    api_key = api_url + api_inp


    summoner_name = find_summoner()

    validate_name(region_url, name_get, summoner_name, api_key)

import requests
import urllib.parse
import os


def make_dashes(length=60, style='=') -> int:
    print(style * length)


def mapquest(orig, dest):
    """"
    :param orig: starting point
    :param dest: destination
    
    Ensures that the start and end locations are received before making a request to the
    API server. This helps to get rid of empty and bogus requests. Saves the amount of
    tokens as well, since only valid requests are sent to the API.
    """
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    api_key = os.getenv('MAPQUEST_API_KEY')
    
    # Error code 611 (info dict) => the start and/or destination parameters were not received. This checks the parameters before sending it to the API server.
    if '' not in (orig, dest):
        # ensures that the available tokens are not wasted with empty requests
        url = main_api + urllib.parse.urlencode(
            {'key': api_key, 'from': orig, 'to': dest,}
        )
        
        get_directions = requests.get(url).json()
        # get the status code in the response (API specific)     
        status_code = get_directions['info']['statuscode']
        
    else:
        make_dashes(style='#')
        print(f'Error code 611: At least two locations must be provided.')
        make_dashes(style='#')
        quit()
    
    if status_code == 0:  # successful API request-response
        count = 1
        make_dashes()
        print(f"Direction from {orig} to {dest}")
        # this key was not using when the unit was set to km. it returned None
        print(f"Trip Duration: {get_directions['route']['formattedTime']}")
        print(f"Distance: {get_directions['route']['distance'] * 1.61:.2f} km")
        # I don't seem to have this key in the response
        print(f"Fuel Used (Gal): {get_directions.get('route').get('fuelUsed', '')}")
        make_dashes()
        # get direction narratives
        directions = get_directions['route']['legs'][0]['maneuvers']   
        for direction in directions:
            print(f"{count}. {direction['narrative']} ({direction['distance'] * 1.61:.2f} km)")
            count += 1
            
    elif status_code == 402:
        make_dashes(style='-+-', length=25)
        print(f'Error code {status_code}: Unable to route with the given locations')
        make_dashes(style='-+-', length=25)
        
    print()
    

if __name__ == '__main__':
    searching = True
    
    while searching:
        try:    
            orig = input("Starting Point: ")
            if orig != 'quit':
                dest = input("Destination: ")
                if dest == 'quit':
                    quit(0)
            else:
                searching = False
                quit(0)
        except KeyboardInterrupt:
            quit(1)
        except EOFError:
            quit(1)
        
        mapquest(orig, dest)

import random
destinations = ['Milwaukee',  'Chicago', 'Madison', 'Cincinnati']
restaurants =  ['Milwaukee Burger Company', "Giordano's", 'Cento', 'Sotto']
transportation = ['rental car', 'train', 'plane', 'boat']
entertainments = ['tour the Milwaukee Art Museum', 'visit Millennium Park', 'go to Henry Vilas Zoo', 'explore the Newport Aquarium' ]

def pick_random_destination(destinations):  
    random_destination = random.choice(destinations)
    print("We chose", random_destination, "for your destination! Is this good? Enter: y/n:")
    destination_input = input('')
    while destination_input == 'n':
        random_destination = random.choice(destinations)
        print("How about", random_destination, "is this better? Enter: y/n:")
        destination_input = input ('')
        if destination_input == 'y':
            print("Great, lets pick out the next part of your trip!")
            
    return random_destination

def pick_random_transport(transport):
    transport = random.choice(transportation)
    print("We found a", transport, "is this good? Enter: y/n")
    transport_input = input('')
    while transport_input == 'n':
        transport = random.choice(transportation)
        print("We also have a", transport, "is this better? Enter: y/n")
        transport_input = input('')
        if transport_input == 'y':
          print("Great, lets pick out the next part of your trip!")   
    
    return transport

def pick_random_entertainment(entertainment):
    entertainment = random.choice(entertainments)
    print("We chose", entertainment, "for your entertainment tonight! Is this good? Enter: y/n")
    entertainment_input = input('')
    while entertainment_input == 'n':
        entertainment = random.choice(entertainments)
        print("Dont like that option? No problem how about",entertainment, "is this better? Enter: y/n" )
        entertainment_input = input('')
        if entertainment_input == 'y':
            print("Great, lets pick out the next part of your trip!")

    return entertainment

def pick_random_restaurant(restaurant):
    restaurant = random.choice(restaurants)
    print("We chose", restaurant, "for your restaurant is this good? Enter: y/n")
    restaurant_input = input('')
    while restaurant_input == 'n':
        restaurant = random.choice(restaurants)
        print("Oh im sorry you dont like that option, how about",restaurant, "is this better? Enter: y/n" )
        restaurant_input = input('')
        if restaurant_input == 'y':
            print("Great, lets move on!")

    return restaurant 
    
def confirm_day_trip():
    chosen_destination = pick_random_destination(destinations)
    chosen_transport = pick_random_transport(transportation)
    chosen_entertainment = pick_random_entertainment(entertainments)
    chosen_restaurant = pick_random_restaurant(restaurants)
    print("Great! We are done generating your day trip. Now lets confirm these are the options you want.")
    print("Your completed trip is:")
    print("Destination:", chosen_destination)  
    print("Transport:", chosen_transport)
    print("Entertainment:", chosen_entertainment)
    print("Restaurant:", chosen_restaurant)
    print("Would you like to sign off on this trip? Enter y/n:")
    day_trip_input = input('')
    if day_trip_input == ('y'):
        print("Prepare to experience your dream travel trip! You will arrive in", chosen_destination, "by", chosen_transport, "where you will", chosen_entertainment, "and end your evening by dining at a local favorite", chosen_restaurant, "we hope you choose us as your travel agency again!")
    else:
        print("We're sorry you didnt like those options. Would you like to plan a new trip?")


confirm_day_trip()





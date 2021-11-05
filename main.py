#Create 4 lists
import random

destinations = ["Texas", "Wisconsin", "New York", "Florida", "Tahiti", "Chicago", "Milwaukee"]

restaurants = ["Chilis", "Applebees", "Olive Garden", "Panera"]

transportations = ["Car", "Airplane", "Train", "Taxi"]

entertainments = ["Circus", "Movie", "Play", "Comedy Show"]


#Create random generator function to return values

def place_to_go (some_list):
    list_index = random.randint(0, len(some_list) - 1 ) 
    return some_list[list_index]



chosen_dest = place_to_go(destinations)
chosen_rest = place_to_go(restaurants)
chosen_trans = place_to_go(transportations)
chosen_entertain = place_to_go(entertainments)

#Print generator function
def trip_to_take(place, eatery, ride, show):
    print(f"'\nHere is your trip!\n Destination: {place}\n Restaurants: {eatery}\n Transportaion: {ride}\n Entertainment: {show}\n")



#While loop,processes while condition is true trip is printed. If not true allows user to change which option the would like and re-picks
not_satisfied = True

while not_satisfied == True:
    trip_to_take(chosen_dest, chosen_rest, chosen_trans, chosen_entertain)
    response = input("Is this the trip you want?: ")
    if response == "yes":
        print("This is your trip!")
        not_satisfied = False
    else:
        print("lets try again")
        option = input("\nChose \n1=Destination \n2=Restaurant \n3=Transportation \n4=Entertainment\n Enter number here:")
        if option == '1':
            chosen_dest = place_to_go(destinations)
        elif option == '2':
            chosen_rest = place_to_go(restaurants)
        elif option == '3':
            chosen_trans = place_to_go(transportations)
        elif option == '4':
            chosen_entertain = place_to_go(entertainments)
        else:
            print("Invalid Entry, Try Again..")

# Call function to run
trip_to_take(chosen_dest, chosen_rest, chosen_trans, chosen_entertain)


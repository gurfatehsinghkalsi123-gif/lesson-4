# Taking total amount as input from user
Amount = int(input("enter amount to withdraw;"))

# Calculating the number of 2000 denomination notes)
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10


print( "notes of 100 rupees" , note_1)
print( "notes of 50 rupees" , note_2)
print( "notes of 10 rupees" , note_3)

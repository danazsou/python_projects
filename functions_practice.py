#create greeting function
def hello(): 
    print("Hello World")

def pack (a,b,c):
    return[a,b,c]

def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My Lunchbox is empty")
  
    for food_index in range(len(my_lunch)):
        if food_index == 0:
            print(f"First I ate {my_lunch[food_index]}")
        elif food_index < (len(my_lunch)  - 1) : 
            print(f"Then I ate  {my_lunch[food_index]}")
        else: 
            print ("my lunchbox is empty)")

hello()
print(pack(1,5,10))
print(pack("a", "b", "c"))

eat_lunch([])
eat_lunch(["Salad"])
eat_lunch(["Salad", "Soup", "Sushi", "Cupcake"])
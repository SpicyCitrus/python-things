import time

print("Made with 💖")
print("Lister. By CozyTorch")

time.sleep(3)


test_mapping = {
    1: "Test 1: Description for Option 1",
    2: "Test 2: Description for Option 2",
    3: "Test 3: Description for Option 3",
    4: "Test 4: Description for Option 4",
    5: "Test 5: Description for Option 5",
    6: "Test 6: Description for Option 6",
    7: "Test 7: Description for Option 7",
}

while True:
    try:
        user_input = int(input("Enter a number (1-7) to display a test description, or 0 to exit: "))
        
        if user_input == 0:
            print("Exiting program.")
            break

        if user_input in test_mapping:
            print(test_mapping[user_input])  
        else:
            print("Invalid input. Please enter a number between 1 and 7.")
    
    except ValueError:
        print("Please enter a valid number.")
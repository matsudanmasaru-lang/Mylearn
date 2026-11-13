todos = []

while True:
    print("\n1. Add task")
    print("2. See tasks")
    print("3. Edit tasks")
    print("4. Exit")
    
    choice = input("Choose 1, 2, 3 or 4: ")
    
    if choice == "1":
        task = input("What task? ")
        todos.append(task)
        print("Added!")
    elif choice == "2":
        print("\nYour tasks:")
        for t in todos:
            print("-", t)
    elif choice == "3":
          task = input("edit tasks")
          todos.append(task)
          print("edited!")
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Pick 1, 2 or 3")

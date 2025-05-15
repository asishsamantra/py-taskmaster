def show_menu(): 
    print("\nTask Manager CLI")
    print("1: Add Task")
    print("2: List Tasks")
    print("3: Complete Task")
    print("4: Delete Task")
    print("5: Exit")

def main(): 
    show_menu()

    while True: 
        choice = input("Enter Choice: ")

        if choice == "1": 
            task = input("Enter task: ")
            print(f"Task is {task}.")
        elif choice == "2": 
            print("You have many tasks pending")
        elif choice == "3": 
            index = int(input("Enter task number to complete: "))
            print(f"Completed task - {index}")
        elif choice == "4": 
            index = int(input("Enter task number to delete: "))
            print(f"Deleted task - {index}")
        elif choice == "5": 
            print("Goodbye")
            break
        else: 
            print("Invalid choice, please try again.")

if __name__ == "__main__": 
    main()
Todos=[]

while True:
    user_input=input("please enter the Add,Edit,Delete,Show:")
    user_input=user_input.strip()
    match user_input:
        case 'Add':
            Todo=input("Please enter the list:")
            Todos.append(Todo)
            print(Todos)
        case 'Show':
            print("Listing the data \n")
            for index,value in enumerate(Todos):
                row = f"{index}----{value}"
                print(row)
        case 'Edit':
            Edit_value=int(input("please enter the number"))
            change_number=Edit_value-1
            Todos[change_number]=input("Enter the word to Edit")
        case 'Delete':
            input2=int(input("please enter the number of the "))
            Todos.pop(input2)
        case '_':
            break;

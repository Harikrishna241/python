while True:
    user_input=input("please enter the Add,Edit,Delete,Show:")
    user_input=user_input.strip()
    match user_input:
        case 'Add':
            Todo=input("Please enter the list:")+ "\n"
            with open('file.txt','r') as f:
                Todos=f.readlines()
            Todos.append(Todo)
            with open('file.txt','w') as f:
                f.writelines(Todos)
            print(Todos)
        case 'Show':
            with open('file.txt','r') as f:
                Todos=f.readlines()
            for index,value in enumerate(Todos):
                row = f"{index+1}.{value.strip('\n')}"
                print(row)
        case 'Edit':
            with open('file.txt','r') as f:
                Todos=f.readlines()
            Edit_value=int(input("please enter the number"))
            change_number=Edit_value-1
            Todos[change_number]=input("Enter the word to Edit ")+ "\n"
            with open('file.txt','w') as f:
               f.writelines(Todos)
        case 'Delete':
            with open('file.txt','r') as f:
                Todos=f.readlines()
            input2=int(input("please enter the number of the \n "))-1
            Todos.pop(input2)
            with open('file.txt','w') as f:
               f.writelines(Todos)
        case '_':
            break;

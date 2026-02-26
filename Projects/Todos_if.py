while True:
    user_input=input("please enter the Add,Edit,Delete,Show:")
    user_input=user_input.strip()
   
    if 'Add' in user_input:
        with open('file.txt','r') as f:
            Todos=f.readlines()
        Todo = user_input[4:]
        Todos.append(Todo)
        with open('file.txt','w') as f:
            f.writelines(Todos)
        print(Todos)
    elif 'Show' in user_input:
        with open('file.txt','r') as f:
            Todos=f.readlines()
        for index,value in enumerate(Todos):
            row = f"{index+1}.{value.strip('\n')}"
            print(row)
    elif 'Edit' in user_input:
        with open('file.txt','r') as f:
            Todos=f.readlines()
        Edit_value=int(user_input[5:])
        change_number=Edit_value-1
        Todos[change_number]=user_input[6:]+ "\n"
        with open('file.txt','w') as f:
            f.writelines(Todos)
    elif 'Delete' in user_input:
        with open('file.txt','r') as f:
            Todos=f.readlines()
        input2=int(input("please enter the number of the \n "))-1
        Todos.pop(input2)
        with open('file.txt','w') as f:
            f.writelines(Todos)
    else:
        break
print("bye")

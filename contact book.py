contacts=[]
while True:
    print("1.Add contact")
    print("2.view all contact details")
    print("3.search contact")
    print("4.update contact")
    print("5.delete contact")
    print("6.Exit")

    choice=input("enter your choice:")
    if(choice=="1"):
        contact_id=input("enter your id:")
        contact_name=input("enter your name:")
        contact_number=input("enter your number:")
        contact_email=input("enter your email:")
        contact={
            "id":contact_id,
            "name":contact_name,
            "number":contact_number,
            "email":contact_email
        }
        contacts.append(contact)
        print("contacts add successfully!")
    elif(choice=="2"):
        print("------contacts details------")
        for contact in contacts:
            print(f"id:{contact["id"]}")
            print(f"name:{contact["name"]}")
            print(f"number:{contact["number"]}")
            print(f"email:{contact["email"]}")
            print("-------------------------")
    elif(choice=="3"):
        search_id=input("enter your id:")
        found=False
        for contact in contacts:
            if(contact["id"]==search_id):
                print("contact found successfuly!")
                print(f"id:{contact["id"]}")
                print(f"name:{contact["name"]}")
                print(f"number:{contact["number"]}")
                print(f"email:{contact["email"]}")
                print("-------------------------")
                found=True
                break
            else:
                print("no contact found yet!")
    elif(choice=="4"):
        update_id=input("enter yor new id:")
        found=False
        for contact in contacts:
            if(contact["id"]==update_id):
                print("contact update successfully!")
                contact["name"]=input("enter your name:")
                contact["number"]=input("enter your number:")
                contact["email"]=input("enter your email:")
                print("-----------------------------")
                found=True
                break
            else:
                print("no contact updated yet!")
    elif(choice=="5"):
        delete_id=input("enter id:")
        found=False
        for contact in contacts:
            if(contact["id"]==delete_id):
                contacts.remove(contact)
                print("contact delete successfully!")
                found=True
                break
            else:
                print("no contact delete yet!")
    elif(choice=="6"):
        print("thanku soo much for using contact book!")
        break
    else:
        print("invalid choice! please try again!")
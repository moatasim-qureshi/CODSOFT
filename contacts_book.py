class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contacts(self, contact):
        self.contacts.append(contact)

    def search_contact(self,info):
        for item in self.contacts:
            if item[0] == info:
                print("\n    -----CONTACT FOUND------\n")
                return f'NAME:            {item[0]}\nCONTACT NUMBER:  {item[1]}\nEMAIL ADDRESS:   {item[2]}\nADDRESS:         {item[3]}\n----------------------'
            
            if item[1] == info:
                print("\n    -----CONTACT FOUND------\n")
                return f'NAME:            {item[0]}\nCONTACT NUMBER:  {item[1]}\nEMAIL ADDRESS:   {item[2]}\nADDRESS:         {item[3]}\n----------------------'
        
        return f'\n    -----CONTACT NOT FOUND------\n'
    
    def delete_contact(self,name):
        for i in self.contacts:
            if i[0] == name:
                return self.contacts.remove(i)
        return f'\n    -----NO SUCH CONTACT EXIST------\n'
        
            
    def view_contacts(self):
        print("\n      -------ALL CONTACTS-------\n")
        for item in self.contacts:
            print(f'NAME:            {item[0]}\nCONTACT NUMBER:  {item[1]}\nEMAIL ADDRESS:   {item[2]}\nADDRESS:         {item[3]}\n----------------------')

contacts = PhoneBook()
contacts.add_contacts(["tintint",567447353,"tintinty@yahoo.com","california"])
contacts.add_contacts(["aliyasur",88253749,"aliyasiry@yahoo.com","karachi"])
contacts.view_contacts()
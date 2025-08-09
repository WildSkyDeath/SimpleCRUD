class Node:
    def __init__(self, d, n=None, p=None):
        self.data=d
        self.next_node=n
        self.prev_node=p
    def __str__(self):
        return('('+str(self.data)+')')
    
class LinkedList:
    def __init__(self, r=None):
        self.root=r
        self.size=0
        
    def add(self, d):
        new_node=Node(d, self.root)
        self.root=new_node
        self.size +=1
        
    def find(self, d):
        this_node=self.root
        while this_node is not None:
            if this_node.data == d:
                print(f"Found: {this_node}")
                return this_node
            this_node = this_node.next_node
        return None
    
    def update(self, d, new_data):
        this_node=self.root
        while this_node is not None:
            if this_node.data == d:
                old_data=this_node.data
                this_node.data=new_data
                print(f"The Number is Updated {d}: '{old_data}' -> '{new_data}'")
                return
            this_node=this_node.next_node
        print("No match found. Nothing changed.")
    
    def remove(self, d):
        this_node=self.root
        prev_node=None
        
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root=this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node=this_node
                this_node=this_node.next_node
        return False
    
    def print_list(self):
        this_node=self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node=this_node.next_node
        
myList = LinkedList()
while True:
    print("Type 1 to Create")
    print("Type 2 to Read(find)")
    print("Type 3 to Update")
    print("Type 4 to Delete")
    print("Type 5 for outcome")
    print("Type 6 to end")
    a = str(int(input("Type a number you wish to do: ")))
    if a=="1":
        myList.add(int(input("What number do you wish to Create(add)?: ")))
        print("Number is added")
        print("\n")
        
    elif a=="2":
        print(myList.find((int(input("What number are you looking for?: ")))))
        print("\n")
        
    elif a=="3":
        old_val=int(input("What number do you wish to Update?: "))
        new_val=int(input("Enter the new number: "))
        myList.update(old_val, new_val)
        print("Number is Updated")
        print("\n")
        
    elif a=="4":
        myList.remove(int(input("What number do you wish to Delete(remove)?: ")))
        print("Number is removed")
        print("\n")
        
    elif a=="5":
        print(myList.print_list())
        print("\n")
        
    elif a=="6":
        print("\n")
        print("Thank you for using this program")
        break
    
    else:
        print("\n")
        print("Incorrect Input please try again")
        print("\n")

import csv

def get_inventory_info():
    """ Loads Information from CSV
    """
    with open('current_inventory.csv') as inventory_file:
        return list(csv.reader(inventory_file))
    
def get_del_inventory_info():
    """ Loads Information from Deleted CSV
    """
    with open('recently_deleted.csv') as inventory_file:
        return list(csv.reader(inventory_file))    

def modify_inventory_info(index,information):
    """ Modifies Inventory Information at the 
    Specified Index. Checks that Price Has a
    Maximum of 2 Decimals and Rounds Price
    Otherwise.
    """
    modified_inventory = get_inventory_info() #Gets Current Inventory Information
    information[-1] = round(float(information[-1]),2) #Rounds Price to 2 Decimals
    modified_inventory[index] = information + [round(float(information[-1]) * int(information[1]),2)] #Calculates Total Value
    with open('current_inventory.csv','w', newline='') as inventory_file:
        writer = csv.writer(inventory_file) 
        writer.writerows(modified_inventory) #Writes New Inventory Information

def add_inventory_info(information):
    added_inventory = get_inventory_info() #Gets Current Inventory Information
    information[-1] = round(float(information[-1]),2) #Rounds Price to 2 Decimals
    information += [round(float(information[-1]) * int(information[1]),2)] #Calculates Total Value
    added_inventory += [information] #Adds New Item to Current Inventory
    with open('current_inventory.csv','w', newline='') as inventory_file:
        writer = csv.writer(inventory_file)   
        writer.writerows(added_inventory) #Writes New Inventory Information

def delete_inventory_info(index,comment):
    all_inventory = get_inventory_info() #Gets Current Inventory Information
    toBeDeleted = all_inventory[index] + [comment]
    with open('recently_deleted.csv','a', newline='') as deleted_inventory_file:
        writer = csv.writer(deleted_inventory_file)
        writer.writerow(toBeDeleted)     
    del all_inventory[index] #Deletes Desired Inventory item
    with open('current_inventory.csv','w', newline='') as inventory_file:
        writer = csv.writer(inventory_file)        
        writer.writerows(all_inventory) #Writes New Inventory Information

def undelete_inventory_info(index):
    deleted_inventory = get_del_inventory_info() #Gets Current Inventory Information
    toBeUnDeleted = deleted_inventory[index] 
    with open('current_inventory.csv','a', newline='') as inventory_file:
        writer = csv.writer(inventory_file)
        writer.writerow(toBeUnDeleted[:-1])        
    del deleted_inventory[index] #Deletes Desired Inventory item
    with open('recently_deleted.csv','w', newline='') as deleted_inventory_file:
        writer = csv.writer(deleted_inventory_file)        
        writer.writerows(deleted_inventory) #Writes New Inventory Information

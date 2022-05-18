from flask import Flask, render_template, request, redirect, send_from_directory, flash
from CSV_Modifiers import *
import os
import logging
        
app = Flask(__name__,template_folder='templates')
app.secret_key = 'SuperSecretKeyNobodyWillGuessThis'
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

@app.route("/")
def index():
    """ Loads inventory home page. Includes
    methods to delete, edit and add to the inventory.
    """    
    inventory_list = get_inventory_info()
    deleted_list = get_del_inventory_info()
    header = inventory_list[0] #Item Labels
    inventory_list = inventory_list[1:] #Actual Items
    for inventory_index in range(len(inventory_list)):
        inventory_list[inventory_index].append("/edit/" + str(inventory_index+1)) #Adds Edit Button Link
        inventory_list[inventory_index].append("/delete/" + str(inventory_index+1)) #Adds Delete Button Link
    delheader = deleted_list[0] #Item Labels
    deleted_list = deleted_list[1:] #Actual Items
    for inventory_index in range(len(deleted_list)):
        deleted_list[inventory_index].append("/undelete/" + str(inventory_index+1)) #Adds Edit Button Link
    return render_template('index.html',inventoryInfo=inventory_list,header=header,deletedInfo=deleted_list,delheader=delheader) #Loads Page
        
    
@app.route("/edit/<index>",methods=["GET","POST"])
def edit_inventory_requests(index):
    """ Identifies whether a POST or GET request
    is sent. Either loads HTML page or
    modifies inventory CSV.
    """
    def get_edit_inventory(index):
        """ Loads HTML for edit page based on
        which item the user wants to edit
        """
        inventory_list = get_inventory_info() #Loads All Inventory
        header=inventory_list[0] #Identifies Item Labels
        edited_inventory = inventory_list[int(index)] #Identifies Item User Wishes to Edit
        return render_template('edit_inventory.html',header=header,inventoryInfo=edited_inventory) #Loads Page

    def post_edit_inventory(index):
        """ Edits Inventory Item in CSV
        based on information in POST request.
        """
        inventory_list = get_inventory_info() #Loads All Inventory
        edited_inventory = inventory_list[int(index)] #Identifies Item User Wishes to Edit
        result = request.form #Loads Request Information with Edited Item
        modify_inventory_info(int(index),list(result.values())) #Modifies Item
        return redirect('/') #Goes Back to Home
    
    if request.method == "GET": #Identifies request type as GET
        return get_edit_inventory(index)
    else: #Identifies request type as POST
        return post_edit_inventory(index)
    
@app.route("/add", methods=["POST"])
def add_inventory():
    """ Checks for Empty Fields. If None
    are Detected, Adds Item to Inventory.
    """
    result = dict(request.form) #Turns Response Into Dictionary
    if '' not in result.values(): #Looks for Empty Fields
        add_inventory_info(list(result.values())) #Adds Item to CSV
        return redirect('/') #Reloads Home Page
    else:
        flash('All Fields Must Have an Entry')
        return redirect('/') #Reloads Home Page with No Change to Inventory

@app.route("/delete/<index>")
def delete_inventory(index):
    """ Deletes Desired Item from CSV File
    """
    comment = request.args.get('comment')
    delete_inventory_info(int(index),comment) #Deletes Item from CSV
    return redirect('/')

@app.route("/undelete/<index>")
def undelete_inventory(index):
    """ Undeletes Desired Item from CSV File
    """
    undelete_inventory_info(int(index)) #Deletes Item from CSV
    return redirect('/')
    
if __name__ == '__main__':
    
    port = 5002
    print(port)
    url = "http://127.0.0.1:{0}".format(port)
    print(url)
    app.run(use_reloader=False, debug=True, port=port)
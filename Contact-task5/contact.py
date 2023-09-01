import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields!")

# Function to display the contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, contact_info in contacts.items():
        phone = contact_info["Phone"]
        contact_listbox.insert(tk.END, f"{name} - {phone}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get().strip()
    contact_listbox.delete(0, tk.END)
    
    for name, contact_info in contacts.items():
        if search_term.lower() in name.lower() or search_term in contact_info["Phone"]:
            phone = contact_info["Phone"]
            contact_listbox.insert(tk.END, f"{name} - {phone}")

# Function to update a contact
def update_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if not selected_contact:
        messagebox.showerror("Error", "Please select a contact from the list.")
        return

    selected_name = selected_contact.split(" - ")[0]
    new_phone = new_phone_entry.get()
    new_email = new_email_entry.get()
    new_address = new_address_entry.get()

    if new_phone or new_email or new_address:
        contacts[selected_name]["Phone"] = new_phone
        contacts[selected_name]["Email"] = new_email
        contacts[selected_name]["Address"] = new_address
        clear_update_entries()
        update_contact_list()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showerror("Error", "Please enter new contact details.")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if not selected_contact:
        messagebox.showerror("Error", "Please select a contact from the list.")
        return

    selected_name = selected_contact.split(" - ")[0]
    del contacts[selected_name]
    update_contact_list()
    clear_update_entries()
    messagebox.showinfo("Success", "Contact deleted successfully!")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to clear update entry fields
def clear_update_entries():
    new_phone_entry.delete(0, tk.END)
    new_email_entry.delete(0, tk.END)
    new_address_entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Contact Management App")

# Create and pack widgets
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

contact_listbox = tk.Listbox(root)
contact_listbox.pack()

update_label = tk.Label(root, text="Update Contact:")
update_label.pack()

new_phone_label = tk.Label(root, text="New Phone:")
new_phone_label.pack()
new_phone_entry = tk.Entry(root)
new_phone_entry.pack()

new_email_label = tk.Label(root, text="New Email:")
new_email_label.pack()
new_email_entry = tk.Entry(root)
new_email_entry.pack()

new_address_label = tk.Label(root, text="New Address:")
new_address_label.pack()
new_address_entry = tk.Entry(root)
new_address_entry.pack()

update_button = tk.Button(root, text="Update", command=update_contact)
update_button.pack()

delete_button = tk.Button(root, text="Delete", command=delete_contact)
delete_button.pack()

# Start the main application loop
root.mainloop()

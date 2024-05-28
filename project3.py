import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name.lower()] = Contact(name, phone, email)

    def get_contact(self, name):
        return self.contacts.get(name.lower(), None)

    def update_contact(self, name, phone, email):
        if name.lower() in self.contacts:
            self.contacts[name.lower()] = Contact(name, phone, email)
            return True
        return False

    def delete_contact(self, name):
        return self.contacts.pop(name.lower(), None)

    def get_all_contacts(self):
        return self.contacts.values()
    
class ContactBook2:
    def __init__(self, root):
        self.contact_book = ContactBook()
        self.root = root
        self.root.title(" My Contact Book")
        self.root.configure(bg="lightblue")

        self.name_label = tk.Label(root, text="Name:",fg="green")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone:",fg="green")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email:",fg="green")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact,fg="green")
        self.add_button.grid(row=3, column=0)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact,fg="green")
        self.update_button.grid(row=4, column=0)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact,fg="green")
        self.delete_button.grid(row=5, column=0)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact,fg="green")
        self.search_button.grid(row=6, column=0)

        self.view_button = tk.Button(root, text="View All Contacts", command=self.view_contacts,fg="green")
        self.view_button.grid(row=7, column=0, columnspan=2)

        self.contacts_listbox = tk.Listbox(root, width=50)
        self.contacts_listbox.grid(row=8, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone and email:
            self.contact_book.add_contact(name, phone, email)
            messagebox.showinfo("Successful", "Contact added successfully!")
            self.clearing_entries()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone and email:
            updated = self.contact_book.update_contact(name, phone, email)
            if updated:
                messagebox.showinfo("Successful", "Contact updated successfully!")
                self.clearing_entries()
            else:
                messagebox.showerror("Error", "Contact not found!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def delete_contact(self):
        name = self.name_entry.get()
        if name:
            deleted = self.contact_book.delete_contact(name)
            if deleted:
                messagebox.showinfo("Successful", "Contact deleted successfully!")
                self.clearing_entries()
            else:
                messagebox.showerror("Error", "Contact not found!")
        else:
            messagebox.showerror("Error", "Name field is required!")

    def search_contact(self):
        name = self.name_entry.get()
        if name:
            contact = self.contact_book.get_contact(name)
            if contact:
                self.phone_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.phone_entry.insert(0, contact.phone)
                self.email_entry.insert(0, contact.email)
            else:
                messagebox.showerror("Error", "Contact not found!")
        else:
            messagebox.showerror("Error", "Name field is required!")

    def view_contacts(self):
        for contact in self.contact_book.get_all_contacts():
            self.contacts_listbox.insert(tk.END, str(contact))

    def clearing_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook2(root)
    root.mainloop()

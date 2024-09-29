import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Contact Book')
        self.master.geometry('400x500')
        self.master.config(bg='#3498db')

        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.master, text='Contact Book', font=('Arial', 24, 'bold'), bg='#3498db', fg='white')
        self.title_label.pack(pady=20)

        self.add_button = tk.Button(self.master, text='Add Contact', command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.master, text='View Contacts', command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(self.master, text='Search Contact', command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.master, text='Update Contact', command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.master, text='Delete Contact', command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.exit_button = tk.Button(self.master, text='Exit', command=self.master.quit, bg='red', fg='white')
        self.exit_button.pack(pady=20)

        # Ending label
        self.ending_label = tk.Label(self.master, text='Made By Onkar', font=('Arial', 10), bg='#3498db', fg='white')
        self.ending_label.pack(side='bottom', pady=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter the contact name:")
        phone = simpledialog.askstring("Input", "Enter the contact phone number:")
        
        if name and phone:
            self.contacts[name] = phone
            messagebox.showinfo("Success", f'Contact {name} added!')
        else:
            messagebox.showwarning("Input Error", "Both fields must be filled.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contact List", "No contacts found.")
            return
        
        contact_list = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        name = simpledialog.askstring("Input", "Enter the contact name to search:")
        
        if name in self.contacts:
            phone = self.contacts[name]
            messagebox.showinfo("Contact Found", f"{name}: {phone}")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter the contact name to update:")
        
        if name in self.contacts:
            new_phone = simpledialog.askstring("Input", "Enter the new phone number:")
            if new_phone:
                self.contacts[name] = new_phone
                messagebox.showinfo("Success", f'Contact {name} updated!')
            else:
                messagebox.showwarning("Input Error", "Phone number must be filled.")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the contact name to delete:")
        
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f'Contact {name} deleted!')
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

if __name__ == '__main__':
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

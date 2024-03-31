import tkinter as tk
from tkinter import ttk

class StoreManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Management System")

        # Increase window size
        self.root.geometry("800x600")

        # Create notebook widget
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.product_tab = ttk.Frame(self.notebook)
        self.customer_tab = ttk.Frame(self.notebook)
        self.order_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.product_tab, text="Products")
        self.notebook.add(self.customer_tab, text="Customers")
        self.notebook.add(self.order_tab, text="Orders")

        # Add widgets to tabs
        self.create_product_widgets()
        self.create_customer_widgets()
        self.create_order_widgets()

    def create_product_widgets(self):
        product_label = ttk.Label(self.product_tab, text="Product Management", font=('Arial', 24, 'bold'), anchor='center')
        product_label.pack(pady=10)

        # Entry fields for product credentials
        product_fields = ["Product ID", "Name", "Price", "Quantity"]
        self.product_entries = {}
        for field in product_fields:
            label = ttk.Label(self.product_tab, text=field + ":", font=('Arial', 14))
            label.pack()
            entry = ttk.Entry(self.product_tab, font=('Arial', 14))
            entry.pack()
            self.product_entries[field] = entry

        # Button to save product information
        save_button = ttk.Button(self.product_tab, text="Save", command=self.save_product_info)
        save_button.pack(pady=10)

    def save_product_info(self):
        # Retrieve entered product information
        product_info = {}
        for field, entry in self.product_entries.items():
            product_info[field] = entry.get()

        # Print the entered product information (you can save it to a file or database instead)
        print("Entered Product Information:")
        for field, value in product_info.items():
            print(f"{field}: {value}")

    def create_customer_widgets(self):
        customer_label = ttk.Label(self.customer_tab, text="Customer Management", font=('Arial', 24, 'bold'), anchor='center')
        customer_label.pack(pady=10)

        # Placeholder for customer credentials
        customer_credentials = {
            "customer_id": "456",
            "name": "Customer Name",
            "email": "customer@example.com"
        }

        # Add customer management widgets here

    def create_order_widgets(self):
        order_label = ttk.Label(self.order_tab, text="Order Management", font=('Arial', 24, 'bold'), anchor='center')
        order_label.pack(pady=10)

        # Placeholder for order credentials
        order_credentials = {
            "order_id": "789",
            "customer_id": "456",
            "product_ids": ["123", "124"]
        }

        def create_customer_widgets(self):
            customer_label = ttk.Label(self.customer_tab, text="Customer Management", font=('Arial', 24, 'bold'),
                                       anchor='center')
            customer_label.pack(pady=10)

            # Entry fields for customer credentials
            customer_fields = ["Customer ID", "Name", "Email"]
            self.customer_entries = {}
            for field in customer_fields:
                label = ttk.Label(self.customer_tab, text=field + ":", font=('Arial', 14))
                label.pack()
                entry = ttk.Entry(self.customer_tab, font=('Arial', 14))
                entry.pack()
                self.customer_entries[field] = entry

            # Button to save customer information
            save_button = ttk.Button(self.customer_tab, text="Save", command=self.save_customer_info)
            save_button.pack(pady=10)

        def save_customer_info(self):
            # Retrieve entered customer information
            customer_info = {}
            for field, entry in self.customer_entries.items():
                customer_info[field] = entry.get()

            # Print the entered customer information (you can save it to a file or database instead)
            print("Entered Customer Information:")
            for field, value in customer_info.items():
                print(f"{field}: {value}")

        # Add order management widgets here

# Create main window
root = tk.Tk()
app = StoreManagementApp(root)
root.mainloop()

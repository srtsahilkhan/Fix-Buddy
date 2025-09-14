
import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import threading
import time

# Sample pending phones list (tu ise update kar sakta hai)
pending_phones = [
    {"name": "Phone A", "received": "2025-09-10", "status": "pending"},
    {"name": "Phone B", "received": "2025-09-12", "status": "pending"},
    {"name": "Phone C", "received": "2025-09-13", "status": "pending"}
]

# Function to randomly alert user about pending phones
def random_alert():
    while True:
        time.sleep(random.randint(30, 90))  # Random interval in seconds
        pending = [p for p in pending_phones if p['status'] == 'pending']
        if pending:
            phone = random.choice(pending)
            reason = simpledialog.askstring("Pending Alert", f"{phone['name']} (Received: {phone['received']}) is pending. Reason?")
            if reason:
                print(f"Reason for {phone['name']}: {reason}")

# Function to mark phone as completed
def mark_completed(phone_index):
    if phone_index is not None:
        pending_phones[phone_index]['status'] = 'completed'
        refresh_list()

# Refresh the displayed list in GUI
def refresh_list():
    listbox.delete(0, tk.END)
    for i, phone in enumerate(pending_phones):
        listbox.insert(tk.END, f"{phone['name']} - {phone['received']} - {phone['status']}")

# GUI setup
root = tk.Tk()
root.title("Phone Repair Reminder")

listbox = tk.Listbox(root, width=50)
listbox.pack(padx=20, pady=20)

complete_button = tk.Button(root, text="Mark as Completed", command=lambda: mark_completed(listbox.curselection()[0] if listbox.curselection() else None))
complete_button.pack(pady=10)

refresh_list()

# Start the random alert thread
alert_thread = threading.Thread(target=random_alert, daemon=True)
alert_thread.start()

root.mainloop()

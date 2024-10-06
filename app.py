import tkinter as tk
import requests
import threading

# Function to fetch the rate and update the UI
def update_currency(currency):
    def fetch_rate():
        loading_label.config(text="Loading...")
        url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/LKR"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            rate = data['conversion_rates'][currency]
            rate_label.config(text=f"1 LKR = {rate} {currency}")

            try:
                lkr_amount = float(lkr_entry.get())
                converted_amount = lkr_amount * rate
                result_label.config(text=f"{converted_amount:.2f} {currency}")
            except ValueError:
                result_label.config(text="Please enter a valid number")
        else:
            result_label.config(text="Error fetching rate")
        loading_label.config(text="")  # Remove the loading text after fetching

    # Run the fetch rate function in a separate thread
    thread = threading.Thread(target=fetch_rate)
    thread.start()

# GUI setup
root = tk.Tk()
root.title("Currency Converter")

# Left panel with currency buttons
frame_left = tk.Frame(root, bg="orange", width=200)
frame_left.pack(side="left", fill="y")

currencies = ["USD", "GBP", "EUR", "JPY", "CAD"]
for currency in currencies:
    button = tk.Button(frame_left, text=currency, command=lambda c=currency: update_currency(c))
    button.pack(pady=10, padx=20)

# Main panel for input and output
frame_main = tk.Frame(root, bg="white")
frame_main.pack(side="right", expand=True, fill="both")

# Labels and entry fields
tk.Label(frame_main, text="Enter LKR Amount:").grid(row=0, column=0, padx=10, pady=10)
lkr_entry = tk.Entry(frame_main)
lkr_entry.grid(row=0, column=1, padx=10, pady=10)

rate_label = tk.Label(frame_main, text="Select a currency", font=("Arial", 12))
rate_label.grid(row=1, column=0, columnspan=2, pady=20)

result_label = tk.Label(frame_main, text="", font=("Arial", 12))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Loading label to indicate processing
loading_label = tk.Label(frame_main, text="", font=("Arial", 10), fg="blue")
loading_label.grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(frame_main, text="Developed by Pasindu Dewviman").grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()


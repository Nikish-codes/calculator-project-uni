
import tkinter as tk

# Main Application Window
# This is the main box that holds everything for our app.
root = tk.Tk()
root.title("Calculator By Nikish")
root.geometry("400x600") # Set the size of the window (width x height)
root.resizable(False, False) # Don't allow resizing the window
root.configure(bg="#2C3E50") # Set a dark background color for the window

#Functions for Calculator Logic

# This function is called whenever a number or operator button is pressed.
def button_click(item):
    "Appends the clicked item (number or operator) to the display."
    # We get whatever is currently in the display and add the new item to it.
    current_expression = display.get()
    display.delete(0, tk.END) # Clear the display
    display.insert(0, current_expression + str(item)) # Insert the new expression

# This function is called when the Clear button is pressed.
def button_clear():
    """Clears the entire display."""
    display.delete(0, tk.END) # Just clear everything in the display box.

# This function is called when the '=' (Equals) button is pressed.
def button_equal():
    """Calculates the expression in the display and shows the result."""
    try:
        # 'eval' is a simple way to take a string like "5 * 3" and calculate the result.
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        # If something goes wrong (like "5 * / 3" or dividing by zero), show an error.
        display.delete(0, tk.END)
        display.insert(0, "Error")

#  GUI Layout 

# Display Screen
display = tk.Entry(root, font=('Arial', 30, 'bold'), bg="#ECF0F1", fg="#2C3E50", bd=0, justify='right')
display.pack(pady=20, padx=10, ipady=10, fill='x') 

# Buttons Frame
buttons_frame = tk.Frame(root, bg="#2C3E50")
buttons_frame.pack(fill='both', expand=True)

#Creating and Placing the Buttons
# We configure the grid columns and rows to have equal weight.
# This makes the buttons expand to fill the available space nicely.
for i in range(4):
    buttons_frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    buttons_frame.grid_rowconfigure(i, weight=1)

# The layout is now more explicit. '0' takes up two cells.
button_layout = [
    ['(', ')', 'C', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '0', '.', '=']
]

# A set to keep track of buttons we've already placed (for those spanning multiple columns)
processed_buttons = set()

# Loop through the button_layout to create and place each button
for r_index, row_content in enumerate(button_layout):
    for c_index, button_text in enumerate(row_content):
        # If the button text is already in our processed set, skip it.
        if button_text in processed_buttons:
            continue

        # Special styling for operator buttons
        if button_text in ['/', '*', '-', '+', '=']:
            bg_color = "#E67E22" # Orange for operators
            fg_color = "white"
        elif button_text == 'C':
            bg_color = "#E74C3C" # Red for Clear
            fg_color = "white"
        else:
            bg_color = "#BDC3C7" # Light grey for numbers
            fg_color = "#2C3E50"

        # Define what each button does when clicked
        if button_text == 'C':
            action = button_clear
        elif button_text == '=':
            action = button_equal
        else:
            # We use a 'lambda' here to pass the button_text to the button_click function.
            action = lambda text=button_text: button_click(text)

        # Define column span for wide buttons
        colspan = 2 if button_text == '0' else 1
        
        # Create the button
        button = tk.Button(buttons_frame, text=button_text, font=('Arial', 18, 'bold'),
                           bg=bg_color, fg=fg_color, bd=0, command=action)
        
        # Place the button on the grid
        # 'sticky="nsew"' makes the button stretch to fill the whole grid cell
        button.grid(row=r_index, column=c_index, columnspan=colspan, padx=1, pady=1, sticky="nsew")

        # If the button spans more than one column, add its text to the processed set
        if colspan > 1:
            processed_buttons.add(button_text)


# --- Start the Application ---
# root.mainloop() tells tkinter to run the application and wait for user actions (like clicks).
root.mainloop()

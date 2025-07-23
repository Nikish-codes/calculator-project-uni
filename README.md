Simple GUI Calculator - Woxsen L.E.A.P. Project

This project is a simple, yet functional, graphical user interface (GUI) calculator built with Python and the tkinter library. It was developed as part of the Woxsen University L.E.A.P. (Learn, Experience, Advance, and Perform) Program.

The application provides a clean, modern interface for performing basic arithmetic operations.

(This is an example screenshot. You can replace this with a screenshot of the running application.)
Features

    Standard Arithmetic Operations: Perform addition (+), subtraction (-), multiplication (*), and division (/).

    Parentheses Support: Handle complex expressions using ( and ) for order of operations.

    Clear and Responsive UI: A clean, dark-themed user interface that is easy to navigate. The buttons are responsive and fill the window space for a professional look.

    Error Handling: The calculator gracefully handles invalid expressions (e.g., division by zero, syntax errors) by displaying an "Error" message instead of crashing.

    Beginner-Friendly Code: The source code is well-commented and structured in a way that is easy for beginners to understand and learn from.

Technologies Used

    Language: Python 3

    GUI Library: tkinter (standard with Python)

How to Run This Project

To run this calculator on your local machine, follow these simple steps.
Prerequisites

You need to have Python 3 installed on your system. tkinter is included by default with most Python installations, so no external libraries are required.
Steps

    Clone the repository:

    git clone <your-repository-url>

    Navigate to the project directory:

    cd <your-project-directory>

    Run the Python script:

    python gui_calculator.py

    The calculator window should now appear on your screen.

Code Structure Overview

The code in gui_calculator.py is organized into three main sections for clarity:

    Main Application Window:

        Initializes the main tkinter window (root).

        Sets the title, size, and background color.

    Functions for Calculator Logic:

        button_click(item): Appends the character of the clicked button to the display.

        button_clear(): Clears the entire display screen.

        button_equal(): Evaluates the expression in the display using eval(). It includes try...except block for robust error handling.

    GUI Layout:

        Creates the display Entry widget where numbers and results are shown.

        Sets up a Frame to hold all the buttons.

        The buttons are laid out in a grid, which is configured to make the buttons expand and fill the window, ensuring a clean and responsive design.

This project serves as a practical introduction to GUI development in Python, demonstrating key concepts like event handling, layout management, and basic application logic.

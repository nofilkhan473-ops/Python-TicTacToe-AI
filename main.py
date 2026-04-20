import tkinter as tk
from ui import TicTacToeUI

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    
    # Launch the Tic Tac Toe User Interface
    app = TicTacToeUI(root)
    
    # Run the application
    root.mainloop()
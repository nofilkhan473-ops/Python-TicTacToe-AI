# 🎮 Python Tic Tac Toe with Minimax AI

A modern, colorful desktop implementation of the classic Tic Tac Toe game built entirely in Python. This project features a custom Graphical User Interface (GUI) and an intelligent AI opponent powered by the **Minimax algorithm**.

## ✨ Features

* 🤖 **Smart AI Opponent:** Uses the classic Minimax algorithm for game theory decision-making, ensuring the "Hard" mode is mathematically unbeatable.
* 🎚️ **Multiple Difficulty Levels:** Choose between Easy (random moves), Medium (mixed), and Hard (Minimax) to match your skill level.
* 🎨 **Modern Custom UI:** Built with Python's `tkinter` library, completely restyled with a sleek dark theme (`#2C3E50`), vibrant grid buttons, and dynamic neon highlights for winning combinations.
* 🔊 **Audio Feedback:** Includes sound effects for button clicks, game wins, and draws (supported on Windows via `winsound`).
* 👥 **Dual Game Modes:** Play locally against a friend (Human vs Human) or test your skills against the computer (Human vs AI).
* ⚙️ **Modular Design:** Clean, Object-Oriented Programming (OOP) structure separating game logic, AI, user interface, and sound management.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **GUI Framework:** Tkinter (Python standard library)
* **Concepts:** Object-Oriented Programming (OOP), Game State Management, Algorithm Design (Minimax)

## 📁 Project Structure

* `main.py` - The entry point of the application that initializes the Tkinter window.
* `ui.py` - Handles all the visual elements, button clicks, and custom color styling.
* `game.py` - Manages the core game state, board updates, and win/draw condition checking.
* `ai.py` - Contains the logic for the AI opponent, including the recursive Minimax function.
* `sound.py` - Manages system sound effects for gameplay actions.
* `constants.py` & `animations.py` - Store configuration variables and visual animation logic.

## 🚀 How to Run

1. **Ensure you have Python installed** on your computer (Python 3.6 or higher is recommended).
2. **Download or clone** this repository to your local machine.
3. Open a terminal or command prompt and navigate to the project folder.
4. Run the following command:
   ```bash
   python main.py

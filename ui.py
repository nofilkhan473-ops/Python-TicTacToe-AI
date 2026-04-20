import tkinter as tk
from tkinter import messagebox
from game import TicTacToeGame
from ai import AIPlayer
from sound import SoundManager

class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        
        # --- NEW: Set main window background color ---
        self.bg_color = "#2C3E50" # Dark slate
        self.root.configure(bg=self.bg_color)

        self.game = TicTacToeGame()
        self.ai_player = AIPlayer()

        self.game_mode = tk.StringVar(value="HUMAN")
        self.ai_difficulty = tk.StringVar(value="HARD")

        self.build_controls()
        self.build_board()
        self.update_game_mode()

    def build_controls(self):
        # --- NEW: Styled the frames and text ---
        mode_frame = tk.LabelFrame(self.root, text="Game Mode", bg=self.bg_color, fg="#ECF0F1", font=("Arial", 10, "bold"))
        mode_frame.pack(pady=10, padx=10, fill="x")

        # Configure radio buttons to match the colorful theme
        radio_style = {"bg": self.bg_color, "fg": "#ECF0F1", "selectcolor": "#34495E", "activebackground": self.bg_color, "activeforeground": "#1ABC9C"}

        tk.Radiobutton(
            mode_frame, text="Human vs Human",
            variable=self.game_mode, value="HUMAN",
            command=self.update_game_mode,
            **radio_style
        ).pack(side="left", padx=6)

        tk.Radiobutton(
            mode_frame, text="Human vs AI",
            variable=self.game_mode, value="AI",
            command=self.update_game_mode,
            **radio_style
        ).pack(side="left", padx=6)

        self.diff_frame = tk.LabelFrame(self.root, text="AI Difficulty", bg=self.bg_color, fg="#ECF0F1", font=("Arial", 10, "bold"))

        for level in ["EASY", "MEDIUM", "HARD"]:
            tk.Radiobutton(
                self.diff_frame,
                text=level.title(),
                variable=self.ai_difficulty,
                value=level,
                command=self.update_difficulty,
                **radio_style
            ).pack(side="left", padx=6)

        # --- NEW: Colorful New Game Button ---
        tk.Button(
            self.root, text="New Game", 
            command=self.reset_game,
            bg="#E74C3C", fg="white", font=("Arial", 12, "bold"),
            activebackground="#C0392B", activeforeground="white",
            relief="flat", padx=10, pady=5
        ).pack(pady=10)

    def build_board(self):
        self.board_frame = tk.Frame(self.root, bg=self.bg_color)
        self.board_frame.pack(pady=10)

        self.buttons = []
        for i in range(9):
            # --- NEW: Colorful Game Grid ---
            btn = tk.Button(
                self.board_frame,
                text="",
                font=("Arial", 36, "bold"),
                width=4,
                height=1,
                bg="#3498DB", # Nice blue background
                fg="white",
                activebackground="#2980B9",
                relief="ridge",
                bd=3,
                command=lambda i=i: self.handle_click(i)
            )
            btn.grid(row=i//3, column=i%3, padx=2, pady=2)
            self.buttons.append(btn)

    def update_game_mode(self):
        if self.game_mode.get() == "AI":
            self.diff_frame.pack(pady=5, padx=10, fill="x")
        else:
            self.diff_frame.pack_forget()

    def update_difficulty(self):
        self.ai_player.set_difficulty(self.ai_difficulty.get())

    def handle_click(self, index):
        if self.game_mode.get() == "AI" and self.game.current_player != "X":
            return

        if not self.game.make_move(index):
            return

        SoundManager.click()
        self.update_button(index)

        if self.process_result():
            return

        self.game.switch_player()

        if self.game_mode.get() == "AI":
            self.root.after(300, self.ai_turn)

    def ai_turn(self):
        self.ai_player.set_difficulty(self.ai_difficulty.get())
        move = self.ai_player.get_best_move(self.game.board)
        if move is not None:
            self.game.make_move(move)
            SoundManager.click()
            self.update_button(move)

            if self.process_result():
                return

            self.game.switch_player()

    def update_button(self, index):
        btn = self.buttons[index]
        mark = self.game.board[index]
        
        # --- NEW: Different colors for X and O ---
        text_color = "#F1C40F" if mark == "X" else "#E67E22" # Yellow for X, Orange for O

        btn.config(
            text=mark,
            fg=text_color,
            disabledforeground=text_color, # Keeps color bright even when disabled
            state="disabled"
        )

    def process_result(self):
        winner, combo = self.game.check_winner()

        if winner:
            if winner == "Draw":
                SoundManager.draw()
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                SoundManager.win()
                for i in combo:
                    # --- NEW: Neon green winning line ---
                    self.buttons[i].config(bg="#2ECC71") 
                messagebox.showinfo("Game Over", f"Player {winner} wins!")

            self.disable_board()
            return True

        return False

    def disable_board(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        SoundManager.restart()
        self.game.reset()
        for btn in self.buttons:
            # --- NEW: Reset to our custom blue color instead of system gray ---
            btn.config(text="", state="normal", bg="#3498DB")
        self.update_game_mode()
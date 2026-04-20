from constants import WIN_COLOR_1, WIN_COLOR_2


class Animator:
    def __init__(self, root, buttons):
        self.root = root
        self.buttons = buttons

    def animate_winner(self, combo, step=0):
        colors = [WIN_COLOR_1, WIN_COLOR_2]

        if step >= 6:
            return

        for index in combo:
            self.buttons[index].config(bg=colors[step % 2])

        self.root.after(200, self.animate_winner, combo, step + 1)

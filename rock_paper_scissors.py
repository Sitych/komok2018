from kivy.app import App
from random import randint
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

x, y = 0, 0


class GameApp(App):

    def attact(self, button):
        global x, y
        text_result = ""
        choise_enemy = randint(1, 3)  # 1- Rock, 2 - Paper, 3 - Scissors
        if choise_enemy == 1:
            if button.text == "Rock":
                text_result = "Draw"
            elif button.text == "Paper":
                text_result = "Win"
            else:
                text_result = "Lose"
        elif choise_enemy == 2:
            if button.text == "Rock":
                text_result = "Lose"
            elif button.text == "Paper":
                text_result = "Draw"
            else:
                text_result = "Win"
        elif choise_enemy == 3:
            if button.text == "Rock":
                text_result = "Win"
            elif button.text == "Paper":
                text_result = "Lose"
            else:
                text_result = "Draw"
        self.result.text = text_result
        if text_result == "Win":
            x = x + 1
            self.score_player.text = str(x)
        elif text_result == "Lose":
            y = y+1
            self.score_enemy.text = str(y)

    def build(self):
        root = BoxLayout()
        box4 = BoxLayout()
        box3 = BoxLayout(orientation="vertical")
        box2 = BoxLayout(orientation="vertical")
        box1 = BoxLayout(orientation="vertical")
        root.add_widget(box3)
        root.add_widget(box2)
        root.add_widget(box1)
        name_player = Label(text="name_player")
        self.score_player = Label(text="0", font_size=50)
        box3.add_widget(name_player)
        box3.add_widget(self.score_player)
        name_enemy = Label(text="name_enemy")
        self.score_enemy = Label(text="0", font_size=50)
        box1.add_widget(name_enemy)
        box1.add_widget(self.score_enemy)
        self.result = Label(text="Choose rock, paper or scissors")
        restart = Button(text="restart")
        box2.add_widget(self.result)
        box2.add_widget(box4)
        # box2.add_widget(restart)
        rock = Button(text="Rock", on_press=self.attact)
        paper = Button(text="Paper", on_press=self.attact)
        scissors = Button(text="scissors", on_press=self.attact)
        box4.add_widget(rock)
        box4.add_widget(paper)
        box4.add_widget(scissors)
        return root


GameApp().run()

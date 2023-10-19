import random

lst =['Keo','Bua','Bao']

class U_play:
    def __init__(self):
        self.userinput = None
    def U_input(self):
        self.userinput = input('Please enter your choise: ')

class Boot_play:
    def __init__(self):
        self.bootinput = None
    def B_input(self):
        self.bootinput = random.choice(lst)

class Play_game:
    def start(self,boot,user):
        if boot.bootinput == user.userinput:
            print('Hoa')
        elif boot.B_input == 'Keo' and user.U_input == 'Bao':
            print('Boot win')
        elif boot.B_input == 'Keo' and user.U_input == 'Bua':
            print('User win')
        elif boot.B_input == 'Bao' and user.U_input == 'Keo':
            print('User win')
        elif boot.B_input == 'Bao' and user.U_input == 'Bua':
            print('Boot win')

if __name__ =='__main__':
    boot = Boot_play()
    user = U_play()
    boot.B_input()
    user.U_input()
    play = Play_game()
    play.start(boot,user)



from appJar import gui
import random
answers=['Can\'t tell you now','It\'s certain',
         'Ask again later','Yes','Don\'t count on it',
         'Doubtful','No change']

win=gui('Magic 8 Ball')
win.setResizable(False)
win.setFont(18)
win.addEntry('Question')
def shake(btn):
    if len(win.getEntry('Question'))==0:
        win.errorBox('Error','You must ask a question')
    else:
        answer=random.choice(answers)
        win.setLabel('Answer',answer)
        win.playSound('buzz.wav')
def clear(btn):
    win.clearEntry('Question')
    win.clearLabel('Answer')
win.addButtons(['Shake','Clear'],[shake,clear])
win.addImage('8ball','8ball.gif')
win.addEmptyLabel('Answer')
win.setLabelBg('Answer','yellow')
win.setFocus('Question')
win.go()

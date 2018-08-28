from appJar import gui
win=gui('Lights!')
def press(name):
    if name=='Exit':
        win.stop()
    elif name=='On':
        win.disableButton('On')
        win.enableButton('Off')
        win.setImage('light','bulb_on.gif')
    elif name=='Off':
        win.disableButton('Off')
        win.enableButton('On')
        win.setImage('light','bulb_off.gif')
win.addImage('light','bulb_off.gif')
win.addButtons(['On','Off'],press)
win.disableButton('Off')
win.addButton('Exit',press)

win.go()

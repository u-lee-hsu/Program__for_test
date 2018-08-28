from appJar import gui
win=gui('窗口','400x300')
win.addLabel('lb1','Hello')
win.addLabel('lb2','World')
win.setLabelBg('lb1','pink')
win.setLabelFg('lb2','blue')
win.setLabelFont(50)
win.setResizable(False)
win.go()

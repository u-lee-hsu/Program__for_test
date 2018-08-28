from appJar import gui
win=gui('Calculator')
win.addLabel('fn','First Number',0,0)
win.addEntry('first',0,1)
win.addLabel('sn','Second Number',0,2)
win.addEntry('second',0,3)
win.setFocus('first')
win.addEmptyLabel('Result',1,0,4)
win.setLabelRelief('Result',win.GROOVE)
win.setLabelAlign('Result',win.NW)
win.setLabelHeight('Result',8)
def press(name):
    if name=='Exit':
        win.stop()
    else:
        try:
            firstNum=int(win.getEntry('first'))
            secondNum=int(win.getEntry('second'))
            message='The results are as follows:\n\n'
            message+='Addition:'+str(firstNum+secondNum)+'\n'
            message+='Subtraction:'+str(firstNum-secondNum)+'\n'
            message+='Multiplication:'+str(firstNum*secondNum)+'\n'
            message+='Division:'+str(firstNum/secondNum)+'\n'

            if name=='Result':
                win.setLabel('Result',message)
            elif name=='MessageBox Result':
                win.infoBox('Result',message)
        except ValueError as e:
            win.errorBox('Error','Invalid number')
            win.setFocus('first')
win.addButtons(['Result','MessageBox Result','Exit'],press,2,0)
win.go()

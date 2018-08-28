from appJar import gui
win=gui('Login')
win.addLabel('lb1','Login Window')
win.setBg('green')
win.setFg('white')
win.setFont(16)
win.addLabelEntry('Username')
win.addSecretLabelEntry('Password')
win.addStatusbar()
win.setStatusbar('New status...')
username=None
password=None
def press(name):
    print(name,'pressed')
    if name=='Cancel':
        win.stop()
    elif name=='Reset':
        win.clearAllEntries()
        win.setFocus('Username')
    elif name=='Submit':
        username=win.getEntry('Username')
        password=win.getEntry('Password')
        if username!='asd':
            win.errorBox('Wrong name','Invalid Username')
        elif password!='password':
            win.errorBox('Wrong Password','Invalid password')
        elif password=='password':
            win.infoBox('Success','Valid password')
    
win.addButtons(['Submit','Reset','Cancel'],press)
win.go()
             

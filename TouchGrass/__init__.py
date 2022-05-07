import requests,os,time
grass = "https://images.pexels.com/photos/413195/pexels-photo-413195.jpeg?cs=srgb&dl=pexels-pixmike-413195.jpg&fm=jpg"
def once():
    r = requests.get(grass)
    open("grass.png", 'wb').write(r.content)
    open("grass.vbs", "w+").write("""
x=MsgBox("You just touched grass !", vbInformation, "Grass")
    """)
    time.sleep(0.3)
    os.system("grass.png");os.system("grass.vbs")
    time.sleep(0.8)
    os.remove("grass.png");os.remove("grass.vbs")
def every(loop):
    loop = loop*60
    while True:
        r = requests.get(grass)
        open("grass.png", 'wb').write(r.content)
        open("grass.vbs", "w+").write("""
x=MsgBox("You just touched grass !", vbInformation, "Grass")
        """)
        time.sleep(0.3)
        os.system("grass.png");os.system("grass.vbs")
        time.sleep(0.8)
        os.remove("grass.png");os.remove("grass.vbs")
        time.sleep(loop)
def remind(loop):
    loop = loop*60
    while True:
        open("grass.vbs", "w+").write("""
x=MsgBox("Its time to go outside and touch some grass !", vbInformation, "Grass")
        """)
        time.sleep(0.3)
        os.system("grass.vbs")
        time.sleep(0.8)
        os.remove("grass.vbs")
        time.sleep(loop)




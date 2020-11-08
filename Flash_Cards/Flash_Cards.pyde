class Textbox:
    
    def __init__(self, x,y, xsize, ysize, string):
        self.x=x
        self.y=y
        self.xsize = xsize
        self.ysize = ysize
        self.string=string
        self.selected=False

sentences = []
complex = [["differences", "comparative"],["jurisdictions", "legislature", "codifies", "consolidates"],["precedent", "occasion", "legislature"],["Historically", "religious", "influenced", "secular", "religious", "communities"],["Islamic","several","including","Arabia"]]
words = []
textbox = Textbox(250,1000,1500,900,"")
sCount = 0
enter = False

def getWords():
    global words
    words = sentences[sCount].split()
    for i in range(len(words)):
        if words[i] in complex[sCount]:
            words[i] = "_____"
    words = " ".join(words)
    
def setup():
    size(2000,2000)
    strokeWeight(4)
    global sentences
    with open('input.txt', 'r') as file:
        data = file.read().replace('\n', '')
    data.replace("!", ".")
    data.replace("?", ".")
    data.replace(";", ".")
    data.replace(":", ".")
    sentences = data.split(".")
    getWords()
    
    

def draw():
    global enter
    global sentences
    global words
    global sCount
    background(128,128,128)
    fill(255)
    rect(textbox.x, textbox.y, textbox.xsize, textbox.ysize)
    if textbox.selected:
        stroke(128,128,128)
    else:
        stroke(0)
    fill(0)
    textSize(48)
    text(textbox.string, textbox.x+50, textbox.y+100)
    
    if len(sentences[sCount]) > 100:
        text(words[:49],250,400)
        text(words[49:100],250,600)
        text(words[100:],250,800)
    elif(len(sentences[sCount])>49 and len(sentences[sCount]) <= 100):
        text(words[:49],250,400)
        text(words[49:],250,600)
    else:
        text(words,250,400)
    
    if enter:
        if textbox.string in complex[sCount]:
            words=words.split()
            for i in range(len(words)):
                if words[i] == "_____":
                    print("hi")
                    words[i] = textbox.string
                    break
            textbox.string = ""
            words = " ".join(words)
        enter = False
    
    if "_____" not in words:
        sCount=sCount+1
        getWords()
    
    
                    

def mousePressed():
    if(mouseX >= textbox.x and mouseX <= textbox.x+textbox.xsize and mouseY >= textbox.y and mouseY <= textbox.y+textbox.ysize):
        textbox.selected = True
    else:
        textbox.selected = False
    

def keyPressed():
    global enter
    if key == BACKSPACE:
        textbox.string = textbox.string[0:len(textbox.string)-1]
    elif key != CODED and textbox.selected and key != ENTER:
        textbox.string = textbox.string +  key
    elif key == ENTER:
        enter = True
        
    
    
    
    
    

    

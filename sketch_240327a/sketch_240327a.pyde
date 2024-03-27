# sprawdziłam stare repozytorium i wygląda na to, że ktoś (Marta?)
# wymusił force push bez dociągnięcia i zaakceptowania zmian od innych
# to zaskutkowało cofnięciem o wszystkie zmieny innych i stąd kazało je wysyłać ponownie jako swoje

# te repozytorium jest kopią wyniku tamtego
def setup():
    size(500, 500)
    background(255)
    textSize(18)
	
def draw():
    s = createShape()
    s.beginShape()
    s.fill(200, 200, 255, 230)
    s.stroke(255, 255, 255, 255)
    s.vertex(250, 50)
    s.vertex(300, 150)
    s.vertex(400, 200)
    s.vertex(300, 250)
    s.vertex(250, 350)
    s.vertex(200, 250)
    s.vertex(100, 200)
    s.vertex(200, 150)
    s.vertex(250, 50)
    s.endShape(CLOSE)
    shape(s, 50, 50)

    fill(50, 70, 60)
    text("Piekne, duze, zolte oczy", width/4, height/1)
    fill(255, 255, 0)
    stroke(255, 255, 0)
    ellipse(150, height/2, 100, 100)
    fill(255, 255, 0)
    stroke(255, 255, 0)
    ellipse(250, height/2, 100, 100)
    fill(255, 192, 203)
    noStroke()
    ellipse(150, height/2, 20, 20)
    fill(255, 192, 203)
    noStroke()
    ellipse(250, height/2, 20, 20)
  
    fill (150, 0, 0)
    text ("good mornin' :)", width/8, height/4)
    stroke (0, mouseX, 0)
    arc (200, 250, 300, 350, 0, HALF_PI)
    noFill()

    shape(s, 0, 0)
    fill(0, 0, 0)
    text("gwiazdeczka :3", 180, 200)
    
    fill(127,18,122)
    noStroke()
    ellipse(width-60,height-51,20,20)
    fill(127,18,122)
    noStroke()
    ellipse(width-42,height-51,20,20)
    fill(127,18,122)
    noStroke()
    triangle(width-70,height-48,width-50,height-23,width-32,height-48)
    
    
     #Sandra
    s.beginShape()
    s.fill(0, 0, 100, 100)
    s.stroke(0, 0, 100, 100)
    s.vertex(width-22, height-58)
    s.vertex(50, height/2)
    s.vertex(150, 100)
    s.vertex(9, 30)
    s.endShape(CLOSE)
    shape(s, 22, 22)
    
    text("hejka", 22,22)
    
    #Agata
    fill(255, 0, 0)
    if mousePressed:
        rect(mouseX, mouseY, 5, 5)
        
    fill(155, 0, 0)
    text("Chryzantemy zlociste", width/2, height/2)
    
    key == "g"
    if key == "g":
        fill(0, 100, 0)
        text("witam", width/2+150, height/2-90)

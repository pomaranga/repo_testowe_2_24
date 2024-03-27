# sprawdziłąm stare repozytorium i wygląda na to, że ktoś (Marta?)
# wymusił force push bez dociągnięcia i zaakceptowania zmian od innych
# to zaskutkowało cofnięciem o wszystkie zmieny innych i stąd kazało je wysyłać ponownie jako swoje

# te repozytorium jest kopią wyniku tamtego
def setup():
    size(400, 400)
    background(255)
    textSize(15)
    
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

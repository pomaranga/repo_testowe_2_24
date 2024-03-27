def setup():
    size(500, 500)
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
    shape(s, 0, 0)
    fill(0, 0, 0)
    text("gwiazdeczka :3", 180, 200)
    # g. przybylek

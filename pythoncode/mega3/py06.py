class TV:
    company = "mega"
    color = "red"
    size = 50
    onoff = "off"

    def __init__(self):
        print("TV가 만들어졌습니다")

    def on(self):
        self.onoff = "on"
        print("TV켬")

    def off(self):
        self.onoff = "off"
        print("TV끔")

    def __str__(self):
        return f"{self.company} 사에서 생산한 {self.size} 인치 {self.color} 색 TV {self.onoff} 됨"


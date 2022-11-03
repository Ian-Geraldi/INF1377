class Tempo:
    BPM = 0
    def __init__(self, bpm = 60) -> None:
        self._basenote = 960*60/bpm
    def SetBPM(self, bpm):
        self._basenote = 960*60/bpm

    
    
    def Time(self, fraction):
        return int(self._basenote*fraction)
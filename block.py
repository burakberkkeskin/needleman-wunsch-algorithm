from collections import defaultdict


class Block:
  points = {"left":None,"up":None,"cross":None}
  rotation = ["origin"]
  mainPoint = 0

  def SetLeftPoint(self, leftPoint):
    self.points["left"] = leftPoint

  def SetUpPoint(self, upPoint):
    self.points["up"] = upPoint
  
  def SetCrossPoint(self, crossPoint):
    self.points["cross"] = crossPoint

  def SetMainPoint(self, mainPoint):
    self.mainPoint = mainPoint

  def SetRotationAndPoint(self):
    self.rotation= self.SetRotation(self.points)
    self.mainPoint = max(self.points.values())

  def SetRotation(self, data):
    d = defaultdict(list)
    for key, value in data.items():
        d[value].append(key)
    return max(d.items())[1]

  def GetRotation(self):
    return self.rotation
  
  def GetMainPoint(self):
    return self.mainPoint

  def GetPoints(self):
    return self.points
  


  


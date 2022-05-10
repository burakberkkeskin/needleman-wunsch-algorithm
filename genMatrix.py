from audioop import reverse
from operator import contains
from numpy import block
from block import Block
from collections import defaultdict

#initiliaze the points
match=1
mismatch=-1
gap=-2

def createMatrix(gen1, gen2):
  blockMatrix = [[Block() for x in range(len(gen1))] for y in range(len(gen2))] 
  blockMatrix = setFirstRowAndCloumn(blockMatrix, gen1, gen2)
  return blockMatrix

def setFirstRowAndCloumn(blockMatrix, gen1, gen2):
  i = 1
  while i < len(gen1):
    tempPoint=blockMatrix[0][i-1].GetMainPoint()
    blockMatrix[0][i].SetMainPoint(tempPoint+gap)
    i+=1
    
  i = 1
  tempPoint=0
  while i < len(gen2):
    tempPoint=blockMatrix[i-1][0].GetMainPoint()
    blockMatrix[i][0].SetMainPoint(tempPoint+gap)
    i+=1

  
  return blockMatrix

def fillMatrix(blockMatrix, gen1, gen2):
  i, j = 1, 1
  while i < len(gen2):
    while j < len(gen1):
      leftBlockPoint = blockMatrix[i][j-1].GetMainPoint()
      upBlockPoint = blockMatrix[i-1][j].GetMainPoint()
      crossBlockPoint = blockMatrix[i-1][j-1].GetMainPoint()
      blockMatrix[i][j].SetLeftPoint(leftBlockPoint+gap)
      blockMatrix[i][j].SetUpPoint(upBlockPoint+gap)

      if gen1[j] == gen2[i]:
        blockMatrix[i][j].SetCrossPoint(crossBlockPoint+match)
      elif gen1[j] != gen2[i]:
        blockMatrix[i][j].SetCrossPoint(crossBlockPoint+mismatch)

      blockMatrix[i][j].SetRotationAndPoint()

      j+=1
    j=1
    i+=1
  return blockMatrix

def printMatrix(blockMatrix, gen1, gen2):
  i, j = 1, 1
  while i < len(gen2):
    while j < len(gen1):
      print(f"Current Block: {j}, {i} ")
      print(f"Current Gen: {gen1[j], gen2[i]}")
      print(f"Current Block Point: {blockMatrix[i][j].GetMainPoint()}")
      print(f"Current Block Rotation: {blockMatrix[i][j].GetRotation()}\n")
      j+=1
    j=1
    i+=1


def SetRotation(data):
  d = defaultdict(list)
  for key, value in data.items():
      d[value].append(key)
  return max(d.items())[1]

def traceBack(blockMatrix, gen1, gen2):
  newGen1 = ""
  newGen2 = ""
  i, j = len(gen2)-1, len(gen1)-1
  while i > 0 and j > 0:
    if len(blockMatrix[i][j].GetRotation()) == 1:
      if 'cross' in blockMatrix[i][j].GetRotation():
        # print("Cross Rotation")
        newGen1 += gen1[j]
        newGen2 += gen2[i]
        i -= 1
        j -= 1
        # print(f"Added Gen1: {newGen1[::-1]}")
        # print(f"Added Gen2: {newGen2[::-1]}\n")
      elif 'left' in blockMatrix[i][j].GetRotation():
        # print("Left Rotation")
        newGen1 += gen1[j]
        newGen2 += '-'
        j -= 1
        # print(f"Added Gen1: {newGen1[::-1]}")
        # print(f"Added Gen2: {newGen2[::-1]}\n")
      elif 'up' in blockMatrix[i][j].GetRotation():
        # print("Up Rotation")
        newGen1 += '-'
        newGen2 += gen2[i]
        i -= 1
        # print(f"Added Gen1: {newGen1[::-1]}")
        # print(f"Added Gen2: {newGen2[::-1]}\n")
    else:
      tempPoint = {"left":None,"up":None,"cross":None}
      if 'cross' in blockMatrix[i][j].GetRotation():
        # print("Multiple Cross Rotation")
        tempPoint["cross"]=blockMatrix[i-1][j-1].GetMainPoint()
      if 'left' in blockMatrix[i][j].GetRotation():
        # print("Multiple Left Rotation")
        tempPoint["left"]=blockMatrix[i][j-1].GetMainPoint()
      if 'up' in blockMatrix[i][j].GetRotation():
        # print("Multiple Up Rotation")
        tempPoint["up"]=blockMatrix[i-1][j].GetMainPoint()

      for key in list(tempPoint):
        if tempPoint[key] == None:
          del tempPoint[key]
      
      rotation = SetRotation(tempPoint)

      if 'cross' in rotation :
        # print("Choosen Cross Rotation")
        newGen1 += gen1[j]
        newGen2 += gen2[i]
        i -= 1
        j -= 1
        # print(f"Added Gen1: {newGen1[::-1]}")
        # print(f"Added Gen2: {newGen2[::-1]}\n")
      elif 'left' in rotation :
        # print("Choosen Left Rotation")
        newGen1 += gen1[j]
        newGen2 += '-'
        j -= 1
        # print(f"Added Gen1: {newGen1[::-1]}")
        # print(f"Added Gen2: {newGen2[::-1]}\n")
      elif 'up' in rotation:
        # print("Choosen Up Rotation")
        newGen1 += '-'
        newGen2 += gen2[i]
        i -= 1
        #print(f"Added Gen1: {newGen1[::-1]}")
        #print(f"Added Gen2: {newGen2[::-1]}\n")
  return newGen1[::-1], newGen2[::-1]
    







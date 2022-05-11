from numpy import block
from block import Block
import genMatrix
import timeit
print("Needleman-Wunsch Algorithm")

#Read the gens
with open("./gens/gen1.txt", "r") as f:
    gen1 = f.read().rstrip()
with open("./gens/gen2.txt", "r") as f:
    gen2 = f.read().rstrip()

#Give Information
print(f"\nGen1: {gen1}\nGen2: {gen2}")

gen1 = "0"+gen1
gen2 = "0"+gen2
print("\nAligning Started...")

#initilaize the 2d gen matrix
print("\nInitializing Matrix")
blockMatrix = genMatrix.createMatrix(gen1, gen2)

#Fill the matrix 
print("\nFilling Matrix")
# t=timeit.Timer(lambda: genMatrix.fillMatrix(blockMatrix, gen1, gen2))
# print("Fill Matrix Took: ", t.timeit(1), " second")
blockMatrix = genMatrix.fillMatrix(blockMatrix, gen1, gen2)

#Print the matrix
#genMatrix.printMatrix(blockMatrix, gen1, gen2)


#TraceBack the matrix
print("\nTracing Back Matrix")
gen1, gen2 = genMatrix.traceBack(blockMatrix, gen1, gen2)

#Show the results
print("\nProccess Finished\nAlligment Results: ")
print(f"Gen1: {gen1}")
print(f"Gen2: {gen2}")

# #Test
# t=timeit.Timer(lambda: blockMatrix[2][2].SetRotation(data=blockMatrix[2][2].points))
# print("Set Rotation: ", t.timeit(2000000), " second")

# t=timeit.Timer(lambda: blockMatrix[2][2].testFunc(data=blockMatrix[2][2].points))
# print("Set Rotation: ", t.timeit(2000000), " second")


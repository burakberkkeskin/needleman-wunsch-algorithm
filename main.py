from block import Block
import genMatrix

print("Needleman-Wunsch Algorithm")

#Read the gens
with open("gen1.txt", "r") as f:
    gen1 = f.read().rstrip()
with open("gen2.txt", "r") as f:
    gen2 = f.read().rstrip()

#Give Information
print(f"Gen1: {gen1}\nGen2: {gen2}\n\n")

gen1 = "0"+gen1
gen2 = "0"+gen2
print("Aligning...")
#initilaize the 2d gen matrix
blockMatrix = genMatrix.createMatrix(gen1, gen2)

#Fill the matrix 
blockMatrix = genMatrix.fillMatrix(blockMatrix, gen1, gen2)

#Print the matrix
#genMatrix.printMatrix(blockMatrix, gen1, gen2)

#TraceBack the matrix
gen1, gen2 = genMatrix.traceBack(blockMatrix, gen1, gen2)
print(f"Gen1: {gen1}")
print(f"Gen2: {gen2}")
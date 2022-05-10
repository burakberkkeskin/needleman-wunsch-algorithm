from numpy import block
from block import Block
import genMatrix

#initialize the gens
gen1 = "CAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGACCAAGAC"
gen2 = "GAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACGAACG"

#Give Information
print(f"Alligning: \nGen1: {gen1}\nGen2: {gen2}\n\n")

gen1 = "0"+gen1
gen2 = "0"+gen2

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
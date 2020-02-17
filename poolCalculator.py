import sys

# Get input

W1 = int(sys.argv[1]) #input image width
H1 = int(sys.argv[2]) #input image height
D1 = int(sys.argv[3]) #No. of channels

F = int(sys.argv[4]) #Spatial extent
S = int(sys.argv[4]) #Stride

# Get output

W2 = int((W1 - F)/S + 1)
H2 = int((H1 - F)/S + 1)
D2 = int(D1)

print('Input Dimensions: '+str(W1)+' x '+str(H1)+' x '+str(D1))
print('Output Dimensions: '+str(W2)+' x '+str(H2)+' x '+str(D2))



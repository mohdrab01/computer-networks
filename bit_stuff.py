
##################################################################################################
### BIT STUFFING ###
##################################################################################################

print("##################################################################################################")
print("                                SENDER SIDE - BIT STUFFING ")
print("##################################################################################################")

n = int(input("Enter frame size:"))

frame = input("Enter the frame in the form of 0 and 1 : ")

def applyBitStuffing(frame,n):
	o = "11111"
	f = "0"
	y = frame.replace(o, o+f, n)
	return y



print("After Bit Stuffing :", applyBitStuffing(frame,n))

##################################################################################################
### REVERSING BIT STUFFING ###
##################################################################################################

print("##################################################################################################")
print("                                RECEIVER SIDE - BIT UNSTUFFING ")
print("##################################################################################################")

frame = input("Enter recieved bit stuffed frame: ")
n = len(frame)

def revBitStuffing(frame, n):
	o = "11111"
	f = "0"
	y = frame.replace(o+f, o, n)
	return y

print("After Unstuffing Bit Stuffed frame :", revBitStuffing(frame, n))

##################################################################################################

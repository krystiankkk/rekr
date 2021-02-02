def BitWise(strArray):
    s1 = (strArray[0])
    s2 = (strArray[1])
    s3 = s1 | s2
    strArray = bin(s3)
    return strArray[2:]


print(BitWise(strArray=[0b1001, 0b0100]))
print(BitWise([0b101001, 0b001010]))
print(BitWise([0b100, 0b000]))
print(BitWise([0b00011, 0b010101]))
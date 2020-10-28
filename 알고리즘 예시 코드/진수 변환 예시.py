# 10진수를 2진수, 8진수, 16진수로 변환

n = int(input())

b = bin(n)
o = oct(n)
h = hex(n)

print(b,o,h)



# 2진수, 8진수, 16진수를 각각 10진수로 변환

b2 = int('0b111100', 2)
o2 = int('0o74', 8)
h2 = int('0x3c', 16)

print(b2, o2, h2)



# 2진수에서 각 진수로 변환

o3 = oct(0b111100)
h3 = hex(0b111100)
s3 = str(0b111100)

print(o3,h3,s3)



# 접두어 제외하기

print(format(42, 'b'))
print(format(42, 'o'))
print(format(42, 'x'))
print(format(42, 'X'))
print(format(42, 'd'))

# 접두어 포함하기
print(format(42, '#b'))
print(format(42, '#o'))
print(format(42, '#x'))
print(format(42, '#X'))

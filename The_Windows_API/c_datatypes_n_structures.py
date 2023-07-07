from ctypes import *
#Prints c_bool(True), c_bool(False)
b0 = c_bool(1)
b1 = c_bool(0)

#Prints max number for uint
i0 = c_uint(-1)
print(i0.value)

print("="*50)
c0 = c_char_p(b"test")
print(c0.value)

print("="*50)
c0 = c_char_p(b"test1")
print(c0.value)

p0 = create_string_buffer(5)
print("="*50)
print(p0)
print(c0)

print(c0.value)
print("="*50)

p0.value = b"a"
print(p0.raw)
print(p0)
print("="*50)

#Pointers
i = c_int(42)
pi = pointer(i)
print(pi.contents)
print("="*50)

print(p0.value)
print(p0)
print(hex(addressof(p0)))
print("="*50)

#Pointers
pt = byref(p0)
print(pt)
print("="*50)

print(cast(pt,c_char_p).value)
print("="*50)

print(cast(pt,POINTER(c_int)).contents)
print("="*50)
print(ord('a'))

#Structure
class POINT(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]
point1 = POINT(10, 20)
print("="*50)
print(point1.x)
print(point1.y)
print("="*50)

#Array
point_array_t = POINT * 3
point_array = point_array_t()
point_array[0] = POINT(0, 0)
point_array[1] = POINT(1, 1)
point_array[2] = POINT(1, 2)
for point in point_array:
    print(point.x)
    print(point.y)
print("="*50)



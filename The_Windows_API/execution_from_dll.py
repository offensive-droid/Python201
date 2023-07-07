from ctypes import *

# Result: 1688429847
print("="*50)
print(windll.msvcrt.time(None))
print("="*50)

windll.msvcrt.puts(b"print this!")
print("="*50)

mut_str = create_string_buffer(b'Hello', 10)
# Result: b'Hello\x00\x00\x00\x00\x00'
print(mut_str.raw)
print("="*50)

windll.msvcrt.memset(mut_str, c_char(b"X"), 10)
windll.msvcrt.puts(mut_str)
print(mut_str.value)
print("="*50)

lib = WinDLL("C:\\Users\\Lenovo\\Documents\\TCM_Security\\Python201\\The_Windows_API\\Dll1.dll")
lib.hello()
print("="*50)

lib.length.argtypes = [c_char_p]
lib.length.restype = c_int

str1 = c_char_p(b"Hello")
print("Length Str 1: ", lib.length(str1))
print("="*50)

str2 = c_char_p(b"test1234")
print("Length Str 2: ", lib.length(str2))
print("="*50)

str3 = c_char_p(b"abc\x00123")
print("Length Str 3: ", lib.length(str3))
print("="*50)

lib.add.argtypes = [c_int, c_int]
lib.add.restype = c_int

print("Add 1: ", lib.add(1, 2))
print("="*50)

lib.add_p.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]

x = c_int(1)
y = c_int(2)
res = c_int(0)

print(res)
print(res.value)
print("="*50)

lib.add_p(byref(x), byref(y), byref(res))
print("Add 2: ", res.value)

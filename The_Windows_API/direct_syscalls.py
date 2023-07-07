from ctypes import *
from ctypes import wintypes

SIZE_T = c_size_t
NTSTATUS = wintypes.DWORD

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40

"""
mov r10, rcx 
mov eax, 18h
syscall
ret
"""

def verify(x):
    if not x:
        raise WinError()
    
buf = create_string_buffer(b"\xB8\x05\x00\x00\x00\xc3")
#Get Address
buf_addr = addressof(buf)
print("Buffer Address: 0x%08x" % buf_addr)
VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = [wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.PDWORD]
VirtualProtect.restype = wintypes.INT

old_protect = wintypes.DWORD(0)
verify(VirtualProtect(buf_addr, len(buf), PAGE_EXECUTE_READWRITE, byref(old_protect)))

asm_type = CFUNCTYPE(c_int)
asm = asm_type(buf_addr)

r = asm()
print(hex(r))

print(hex(old_protect.value))

#Second Buff address
buf2 = create_string_buffer(b"\x4C\x8B\xD1\xB8\x12\x00\x00\x00")
buf_addr2 = addressof(buf2)
print("Buffer Address: 0x%08x" % buf_addr2)

old_protection  = wintypes.DWORD(0)
verify(VirtualProtect(buf_addr2, len(buf2), PAGE_EXECUTE_READWRITE, byref(old_protection)))

input()

syscall_type = asm_type(buf_addr2)
syscall_function = syscall_type()

handle = 0xffffffffffffffff
base_address = wintypes.LPVOID(0x0)
zero_bites = wintypes.ULONG(0)
size = wintypes.PSIZE_T(1024 * 12)
ptr2 = syscall_function(handle, base_address, zero_bites, size, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

if ptr2 != 0:
    print("error!")
    print(ptr2)

print("syscall allocation ", hex(ptr2))
input()
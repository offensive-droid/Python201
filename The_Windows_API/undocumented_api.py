from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
SIZE_T = c_size_t

undoc = kernel32.VirtualAlloc
undoc.argtypes = [wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD]
undoc.restype = wintypes.LPVOID

MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_EXECUTE_READWRITE = 0x40

ptr = undoc(None, 1024 * 4, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
error = kernel32.GetLastError()

if error:
    print(error)
    print(WinError(error))

print("VirtualAlloc() returned: 0x%08x" % ptr)
input()

#NTAllocateVirtualMemory
NSTATUS = wintypes.DWORD
ntallocate = windll.ntdll.NtAllocateVirtualMemory
ntallocate.argtypes = [wintypes.HANDLE, wintypes.LPVOID, wintypes.ULONG, wintypes.PSIZE_T, wintypes.ULONG, wintypes.ULONG]
ntallocate.restype = NSTATUS

handle = 0xffffffffffffffff
base_address = wintypes.LPVOID(0x0)
zero_bites = wintypes.ULONG(0)
size = wintypes.PSIZE_T(1024 * 12)
ptr2 = ntallocate(handle, base_address, zero_bites, size, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
if ptr2 != 0:
    print("NtAllocateVirtualMemory() returned: 0x%08x" % ptr2)
    input()

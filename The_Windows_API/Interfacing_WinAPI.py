from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD, DWORD, HANDLE, BOOL
messageBoxA = windll.user32.MessageBoxA
messageBoxA.argtypes = [HWND, LPCSTR, LPCSTR, UINT]
messageBoxA.restype = INT

getUserNameA = windll.Advapi32.GetUserNameA
getUserNameA.argtypes = [LPSTR, LPDWORD]
messageBoxA.restype = INT

buffer_size = DWORD(255)
buffer = create_string_buffer(buffer_size.value)
get_user_a = getUserNameA(buffer, byref(buffer_size))

lpText = buffer
lpCaption = b"Hello"
MB_OK = 0x00000000
messageBoxA(None, lpText, lpCaption, MB_OK)
error = GetLastError()

if error:
    print(error)
    print(WindowsError(error))


class RECT(Structure):
    _fields_ = [("left",c_long),
("top",c_long),
("right",c_long),
("bottom",c_long)]
rect = RECT()

rect.left = 1

GetWindowRect  = windll.user32.GetWindowRect
GetWindowRect.argtypes = (HANDLE,POINTER(RECT))
GetWindowRect.restype = BOOL

hwnd = windll.user32.GetForegroundWindow()
GetWindowRect(hwnd,byref(rect))

#Prints the size of my window
print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)



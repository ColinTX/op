# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _opEx
else:
    import _opEx

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class libop(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, hinst=None):
        _opEx.libop_swiginit(self, _opEx.new_libop(hinst))
    __swig_destroy__ = _opEx.delete_libop

    def Ver(self):
        return _opEx.libop_Ver(self)

    def SetPath(self, path):
        return _opEx.libop_SetPath(self, path)

    def GetPath(self):
        return _opEx.libop_GetPath(self)

    def GetBasePath(self):
        return _opEx.libop_GetBasePath(self)

    def GetID(self):
        return _opEx.libop_GetID(self)

    def GetLastError(self):
        return _opEx.libop_GetLastError(self)

    def SetShowErrorMsg(self, show_type):
        return _opEx.libop_SetShowErrorMsg(self, show_type)

    def Sleep(self, millseconds):
        return _opEx.libop_Sleep(self, millseconds)

    def InjectDll(self, process_name, dll_name):
        return _opEx.libop_InjectDll(self, process_name, dll_name)

    def EnablePicCache(self, enable):
        return _opEx.libop_EnablePicCache(self, enable)

    def CapturePre(self, file_name):
        return _opEx.libop_CapturePre(self, file_name)

    def AStarFindPath(self, mapWidth, mapHeight, disable_points, beginX, beginY, endX, endY):
        return _opEx.libop_AStarFindPath(self, mapWidth, mapHeight, disable_points, beginX, beginY, endX, endY)

    def FindNearestPos(self, all_pos, type, x, y):
        return _opEx.libop_FindNearestPos(self, all_pos, type, x, y)

    def EnumWindow(self, parent, title, class_name, filter):
        return _opEx.libop_EnumWindow(self, parent, title, class_name, filter)

    def EnumWindowByProcess(self, process_name, title, class_name, filter):
        return _opEx.libop_EnumWindowByProcess(self, process_name, title, class_name, filter)

    def EnumProcess(self, name):
        return _opEx.libop_EnumProcess(self, name)

    def ClientToScreen(self, ClientToScreen):
        return _opEx.libop_ClientToScreen(self, ClientToScreen)

    def FindWindow(self, class_name, title):
        return _opEx.libop_FindWindow(self, class_name, title)

    def FindWindowByProcess(self, process_name, class_name, title):
        return _opEx.libop_FindWindowByProcess(self, process_name, class_name, title)

    def FindWindowByProcessId(self, process_id, class_name, title):
        return _opEx.libop_FindWindowByProcessId(self, process_id, class_name, title)

    def FindWindowEx(self, parent, class_name, title):
        return _opEx.libop_FindWindowEx(self, parent, class_name, title)

    def GetClientRect(self, hwnd):
        return _opEx.libop_GetClientRect(self, hwnd)

    def GetClientSize(self, hwnd):
        return _opEx.libop_GetClientSize(self, hwnd)

    def GetForegroundFocus(self):
        return _opEx.libop_GetForegroundFocus(self)

    def GetForegroundWindow(self):
        return _opEx.libop_GetForegroundWindow(self)

    def GetMousePointWindow(self):
        return _opEx.libop_GetMousePointWindow(self)

    def GetPointWindow(self, x, y):
        return _opEx.libop_GetPointWindow(self, x, y)

    def GetProcessInfo(self, pid):
        return _opEx.libop_GetProcessInfo(self, pid)

    def GetSpecialWindow(self, flag):
        return _opEx.libop_GetSpecialWindow(self, flag)

    def GetWindow(self, hwnd, flag):
        return _opEx.libop_GetWindow(self, hwnd, flag)

    def GetWindowClass(self, hwnd):
        return _opEx.libop_GetWindowClass(self, hwnd)

    def GetWindowProcessId(self, hwnd):
        return _opEx.libop_GetWindowProcessId(self, hwnd)

    def GetWindowProcessPath(self, hwnd):
        return _opEx.libop_GetWindowProcessPath(self, hwnd)

    def GetWindowRect(self, hwnd):
        return _opEx.libop_GetWindowRect(self, hwnd)

    def GetWindowState(self, hwnd, flag):
        return _opEx.libop_GetWindowState(self, hwnd, flag)

    def GetWindowTitle(self, hwnd):
        return _opEx.libop_GetWindowTitle(self, hwnd)

    def MoveWindow(self, hwnd, x, y):
        return _opEx.libop_MoveWindow(self, hwnd, x, y)

    def ScreenToClient(self, hwnd):
        return _opEx.libop_ScreenToClient(self, hwnd)

    def SendPaste(self, hwnd):
        return _opEx.libop_SendPaste(self, hwnd)

    def SetClientSize(self, hwnd, width, hight):
        return _opEx.libop_SetClientSize(self, hwnd, width, hight)

    def SetWindowState(self, hwnd, flag):
        return _opEx.libop_SetWindowState(self, hwnd, flag)

    def SetWindowSize(self, hwnd, width, height):
        return _opEx.libop_SetWindowSize(self, hwnd, width, height)

    def SetWindowText(self, hwnd, title):
        return _opEx.libop_SetWindowText(self, hwnd, title)

    def SetWindowTransparent(self, hwnd, trans):
        return _opEx.libop_SetWindowTransparent(self, hwnd, trans)

    def SendString(self, hwnd, str):
        return _opEx.libop_SendString(self, hwnd, str)

    def SendStringIme(self, hwnd, str):
        return _opEx.libop_SendStringIme(self, hwnd, str)

    def RunApp(self, cmdline, mode):
        return _opEx.libop_RunApp(self, cmdline, mode)

    def WinExec(self, cmdline, cmdshow):
        return _opEx.libop_WinExec(self, cmdline, cmdshow)

    def GetCmdStr(self, cmd, millseconds):
        return _opEx.libop_GetCmdStr(self, cmd, millseconds)

    def BindWindow(self, hwnd, display, mouse, keypad, mode):
        return _opEx.libop_BindWindow(self, hwnd, display, mouse, keypad, mode)

    def UnBindWindow(self):
        return _opEx.libop_UnBindWindow(self)

    def GetCursorPos(self):
        return _opEx.libop_GetCursorPos(self)

    def MoveR(self, x, y):
        return _opEx.libop_MoveR(self, x, y)

    def MoveTo(self, x, y):
        return _opEx.libop_MoveTo(self, x, y)

    def MoveToEx(self, x, y, w, h):
        return _opEx.libop_MoveToEx(self, x, y, w, h)

    def LeftClick(self):
        return _opEx.libop_LeftClick(self)

    def LeftDoubleClick(self):
        return _opEx.libop_LeftDoubleClick(self)

    def LeftDown(self):
        return _opEx.libop_LeftDown(self)

    def LeftUp(self):
        return _opEx.libop_LeftUp(self)

    def MiddleClick(self):
        return _opEx.libop_MiddleClick(self)

    def MiddleDown(self):
        return _opEx.libop_MiddleDown(self)

    def MiddleUp(self):
        return _opEx.libop_MiddleUp(self)

    def RightClick(self):
        return _opEx.libop_RightClick(self)

    def RightDown(self):
        return _opEx.libop_RightDown(self)

    def RightUp(self):
        return _opEx.libop_RightUp(self)

    def WheelDown(self):
        return _opEx.libop_WheelDown(self)

    def WheelUp(self):
        return _opEx.libop_WheelUp(self)

    def GetKeyState(self, vk_code):
        return _opEx.libop_GetKeyState(self, vk_code)

    def KeyDown(self, vk_code):
        return _opEx.libop_KeyDown(self, vk_code)

    def KeyDownChar(self, vk_code):
        return _opEx.libop_KeyDownChar(self, vk_code)

    def KeyUp(self, vk_code):
        return _opEx.libop_KeyUp(self, vk_code)

    def KeyUpChar(self, vk_code):
        return _opEx.libop_KeyUpChar(self, vk_code)

    def WaitKey(self, vk_code, time_out):
        return _opEx.libop_WaitKey(self, vk_code, time_out)

    def KeyPress(self, vk_code):
        return _opEx.libop_KeyPress(self, vk_code)

    def KeyPressChar(self, vk_code):
        return _opEx.libop_KeyPressChar(self, vk_code)

    def Capture(self, x1, y1, x2, y2, file_name):
        return _opEx.libop_Capture(self, x1, y1, x2, y2, file_name)

    def CmpColor(self, x, y, color, sim):
        return _opEx.libop_CmpColor(self, x, y, color, sim)

    def FindColor(self, x1, y1, x2, y2, color, sim, dir):
        return _opEx.libop_FindColor(self, x1, y1, x2, y2, color, sim, dir)

    def FindColorEx(self, x1, y1, x2, y2, color, sim, dir):
        return _opEx.libop_FindColorEx(self, x1, y1, x2, y2, color, sim, dir)

    def FindMultiColor(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        return _opEx.libop_FindMultiColor(self, x1, y1, x2, y2, first_color, offset_color, sim, dir)

    def FindMultiColorEx(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        return _opEx.libop_FindMultiColorEx(self, x1, y1, x2, y2, first_color, offset_color, sim, dir)

    def FindPic(self, x1, y1, x2, y2, files, delta_color, sim, dir):
        return _opEx.libop_FindPic(self, x1, y1, x2, y2, files, delta_color, sim, dir)

    def FindPicEx(self, x1, y1, x2, y2, files, delta_color, sim, dir):
        return _opEx.libop_FindPicEx(self, x1, y1, x2, y2, files, delta_color, sim, dir)

    def FindPicExS(self, x1, y1, x2, y2, files, delta_color, sim, dir):
        return _opEx.libop_FindPicExS(self, x1, y1, x2, y2, files, delta_color, sim, dir)

    def GetColor(self, x, y):
        return _opEx.libop_GetColor(self, x, y)

    def SetDisplayInput(self, mode):
        return _opEx.libop_SetDisplayInput(self, mode)

    def LoadPic(self, file_name):
        return _opEx.libop_LoadPic(self, file_name)

    def FreePic(self, file_name):
        return _opEx.libop_FreePic(self, file_name)

    def LoadMemPic(self, file_name, data, size):
        return _opEx.libop_LoadMemPic(self, file_name, data, size)

    def GetScreenData(self, x1, y1, x2, y2, data):
        return _opEx.libop_GetScreenData(self, x1, y1, x2, y2, data)

    def GetScreenDataBmp(self, x1, y1, x2, y2, data):
        return _opEx.libop_GetScreenDataBmp(self, x1, y1, x2, y2, data)

    def GetScreenFrameInfo(self):
        return _opEx.libop_GetScreenFrameInfo(self)

    def MatchPicName(self, pic_name):
        return _opEx.libop_MatchPicName(self, pic_name)

    def SetDict(self, idx, file_name):
        return _opEx.libop_SetDict(self, idx, file_name)

    def SetMemDict(self, idx, data, size):
        return _opEx.libop_SetMemDict(self, idx, data, size)

    def UseDict(self, idx):
        return _opEx.libop_UseDict(self, idx)

    def Ocr(self, x1, y1, x2, y2, color, sim):
        return _opEx.libop_Ocr(self, x1, y1, x2, y2, color, sim)

    def OcrEx(self, x1, y1, x2, y2, color, sim):
        return _opEx.libop_OcrEx(self, x1, y1, x2, y2, color, sim)

    def FindStr(self, x1, y1, x2, y2, strs, color, sim):
        return _opEx.libop_FindStr(self, x1, y1, x2, y2, strs, color, sim)

    def FindStrEx(self, x1, y1, x2, y2, strs, color, sim):
        return _opEx.libop_FindStrEx(self, x1, y1, x2, y2, strs, color, sim)

    def OcrAuto(self, x1, y1, x2, y2, sim):
        return _opEx.libop_OcrAuto(self, x1, y1, x2, y2, sim)

    def OcrFromFile(self, file_name, color_format, sim):
        return _opEx.libop_OcrFromFile(self, file_name, color_format, sim)

    def OcrAutoFromFile(self, file_name, sim):
        return _opEx.libop_OcrAutoFromFile(self, file_name, sim)

    def FindLine(self, x1, y1, x2, y2, color, sim):
        return _opEx.libop_FindLine(self, x1, y1, x2, y2, color, sim)

    def WriteData(self, hwnd, address, data, size):
        return _opEx.libop_WriteData(self, hwnd, address, data, size)

    def ReadData(self, hwnd, address, size):
        return _opEx.libop_ReadData(self, hwnd, address, size)

# Register libop in _opEx:
_opEx.libop_swigregister(libop)




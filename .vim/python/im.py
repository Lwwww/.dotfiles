from ctypes import c_char_p
import ctypes
import os

class ImSwitcher():
    lib = None

    def __init__(self) -> None:
        try:
            import AppKit
            # 隐藏macos dock栏小火箭
            info = AppKit.NSBundle.mainBundle().infoDictionary()
            info["LSBackgroundOnly"] = "1"
        except ImportError:
            print("隐藏macos dock栏小火箭,需要pip3 install -U PyObjC")

        self.lib = ctypes.CDLL(os.environ['HOME'] + "/.dotfiles/lib/libinput-source-switcher.dylib")
        self.lib.getCurrentInputSourceID.restype = c_char_p

    def getCurrentInputSourceID(self):
        # im_id = str(self.lib.getCurrentInputSourceID(), encoding='utf8')
        # return im_id;
        return os.popen('im-select').read()[0:-1]

    def switchInputSource(self, input_method):
        return self.lib.switchInputSource(input_method.encode('ascii'))

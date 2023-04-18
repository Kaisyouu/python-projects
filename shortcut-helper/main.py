import tkinter as tk
from AppKit import NSWorkspace

TEXT_TERMINAL = '''
Terminal
Ctrl + A：移动光标到行首
Ctrl + E：移动光标到行尾
Ctrl + F：向前移动光标一个字符
Ctrl + B：向后移动光标一个字符
Ctrl + D：删除光标后面的一个字符
Ctrl + H：删除光标前面的一个字符
Ctrl + K：从光标处删除到行尾
Ctrl + U：从光标处删除到行首
Ctrl + W：从光标处删除到前一个空格
Ctrl + L：清屏
Tab 键：自动补全文件或命令名称
'''

TEXT_PYCHARM = '''
PyCharm
Cmd + N：创建新文件
Cmd + Shift + N：创建新目录
Cmd + O：打开文件
Cmd + F12：查看当前文件的结构
Cmd + D：复制当前行并将其粘贴到下一行
Cmd + Shift + 上箭头/下箭头：上下移动当前行
Cmd + /：注释/取消注释选定行或代码块
Ctrl + Space：自动补全代码
Shift + F6：重命名变量、函数等
Cmd + Z：撤销上一步操作
Cmd + Shift + Z：恢复上一步被撤销的操作
'''


class AlwaysOnTopWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.wm_overrideredirect(True)
        self.window.attributes("-alpha", 0.5)
        close_button = tk.Button(self.window, text="×", bg="white", fg="red", font=("Helvetica", 16),
                                 anchor="center", command=self.window.destroy)
        close_button.pack(side=tk.TOP, anchor=tk.NE)
        self.app = tk.Label(self.window, font=("Consolas", 18), anchor="center")
        self.app.pack(expand=True)
        self.label = tk.Label(self.window, font=("Consolas", 14), anchor="w", justify="left")
        self.label.pack(fill="both", expand=True)
        self.update_label_text()
        self.window.bind("<Button-1>", lambda e: self.window.lift())
        self.window.bind("<B1-Motion>",
                         lambda e: self.window.geometry("+{0}+{1}".format(e.x_root, e.y_root)))
        self.window.mainloop()

    def get_active_window_title(self):
        active_app_name = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
        return active_app_name

    def update_label_text(self):
        app = self.get_active_window_title()
        self.app.config(text=app)
        if app == "Terminal":
            self.label.config(text=TEXT_TERMINAL)
        elif app == "PyCharm":
            self.label.config(text=TEXT_PYCHARM)
        else:
            self.label.config(text="暂未添加快捷键")
        self.window.after(200, self.update_label_text)


if __name__ == "__main__":
    AlwaysOnTopWindow()

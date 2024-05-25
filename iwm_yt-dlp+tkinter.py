#!/usr/bin/env python3
#coding:utf-8

PROGRAM = "YT-DLP+Tkinter"
VERSION = "Ver.iwm20240518"

import shutil
import subprocess
import time
import tkinter as Tk
import tkinter.scrolledtext as Tk_St
import tkinter.ttk as Tk_Ttk

from ctypes import *
from ctypes.wintypes import *
from tkinter import messagebox

#-------------------------------------------------------------------------------
# My Config
#-------------------------------------------------------------------------------
# YT-DLP Command & Option
List_Cmd = """
yt-dlp -f b
yt-dlp -x --audio-format mp3
echo
yt-dlp --help
"""

#-------------------------------------------------------------------------------
# Const
#-------------------------------------------------------------------------------
H1_BGN = "\033[97;104m$ " + (" " * 70) + "\033[3G"
H1_END = "\033[49m"

#-------------------------------------------------------------------------------
# Function
#-------------------------------------------------------------------------------
def Sub_Clear():
	# おまじない
	subprocess.run("clear || cls", shell = True)

def Sub_SimpleHelp():
	print(
		"\033[97;104m 簡易ヘルプ \033[0m" +
		"\n" +
		"\033[5G"  + "\033[93mYT-DLP コマンド／オプション" +
		"\n" +
		"\033[9G"  + "\033[96myt-dlp -f b" +
		"\n" +
		"\033[14G" + "\033[37m動画ファイルを最高画質でダウンロード" +
		"\n" +
		"\033[9G"  + "\033[96myt-dlp -x --audio-format mp3" +
		"\n" +
		"\033[14G" + "\033[37m音声ファイルをMP3でダウンロード" +
		"\n" +
		"\033[9G"  + "\033[96mecho" +
		"\n" +
		"\033[14G" + "\033[37mテスト" +
		"\n" +
		"\033[9G"  + "\033[96myt-dlp --help" +
		"\n" +
		"\033[14G" + "\033[37mオプション・ヘルプ" +
		"\n" +
		"\033[97;104m (END) \033[0m" +
		"\n"
	)

def Sub_YtDlp_Update():
	Cmd = "yt-dlp"
	if shutil.which(Cmd):
		# ダイアログは最前面に"固定表示されない"仕様のようなので注意!!!!
		Select = messagebox.askyesno(PROGRAM, "YT-DLP の更新を確認しますか ?")
		if Select == True:
			print(
				"\033[97;104m " + Cmd + " \033[0m" +
				"\n" +
				"    " +
				"\033[97m" + subprocess.run((Cmd + " --update-to nightly"), shell = True, capture_output = True, text = True).stdout.strip().replace("\n", "\n    ") +
				"\n" +
				"\033[97;104m (END) \033[0m" +
				"\n"
			)
		Sub_SimpleHelp()
	else:
		print(
			"\033[97;101m YT-DLP は以下のサイトから入手できます。 \033[0m" +
			"\n" +
			"\033[5G" + "\033[97mhttps://github.com/yt-dlp/yt-dlp#release-files" +
			"\n" +
			"\033[9G" + "\033[92mRecommended（推奨版）" +
			"\033[0m" + "\n"
		)

def Sub_Terminal_Reposition():
	# Windows以外で例外発生
	try:
		hwnd = windll.user32.GetForegroundWindow()
		windll.user32.MoveWindow(hwnd, int(30), int(60), int((Win0.winfo_screenwidth() / 2) - 240), int(Win0.winfo_screenheight() - 120), True)
	except(NameError, SyntaxError):
		pass

def Sub_Win0_Resize(e):
	if e.widget is Win0:
		List_Cmd_Cb1.place(width = e.width - 152)
		List_Cmd_Exec_Btn1.place(x = e.width - 147)
		Args_St1.place(width = e.width - 10, height = e.height - 79)
		Args_Clear_Btn1.place(x = e.width - 147)
		Args_Paste_Btn1.place(x = e.width - 85)

def Sub_List_Cmd_Cb1_ContextMenu(e):
	obj1 = List_Cmd_Cb1
	obj2 = None
	if obj1.selection_present() == True:
		obj2 = Cb_ContextMenu_Select
	else:
		obj2 = Cb_ContextMenu_All
	obj2.post(e.x_root, e.y_root)

def Sub_Cb_Clear_Select(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.delete("sel.first", "sel.last")
	return inner

def Sub_Cb_Clear_All(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.delete("0", "end")
	return inner

def Sub_Cb_Copy_Select(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.selection_get())
	return inner

def Sub_Cb_Copy_All(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get())
	return inner

def Sub_Cb_Cut_Select(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.selection_get())
		obj.delete("sel.first", "sel.last")
	return inner

def Sub_Cb_Cut_All(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get())
		obj.delete("0", "end")
	return inner

def Sub_Cb_Paste_Select(obj = None, e = None):
	if obj == None:
		return
	def inner():
		try:
			text = Win0.selection_get(selection = "CLIPBOARD").rstrip()
			obj.delete("sel.first", "sel.last")
			obj.insert("insert", text)
		except:
			pass
	return inner

def Sub_Cb_Paste_All(obj = None, e = None):
	if obj == None:
		return
	def inner():
		try:
			text = Win0.selection_(selection = "CLIPBOARD").rstrip()
			obj.insert("insert", text)
		except:
			pass
	return inner

def Sub_List_Cmd_Exec_Btn1(e = None):
	obj1 = Args_St1
	obj2 = List_Cmd_Cb1
	s1 = obj1.get("1.0", "end-1c").strip()
	s2 = obj2.get().strip()
	a1 = []
	if len(s1) > 0:
		for _opt in s1.split("\n"):
			_opt = _opt.strip()
			if len(_opt) > 0:
				a1 += [(s2 + " " + _opt)]
	else:
		a1 += [s2]
	Sub_Clear()
	Cnt = 0
	List_PS = []
	# PS実行リスト作成
	for _s1 in a1:
		print(H1_BGN + _s1 + H1_END)
		try:
			List_PS.append(subprocess.Popen(_s1, shell = True))
			Cnt += 1
		except:
			break
	i1 = Cnt
	# PS監視
	for _ps in List_PS:
		###print("Existing PS: " + str(_ps))
		while _ps.poll() is None:
			###print("Waiting PS: " + str(_ps))
			time.sleep(5.0)
		i1 -= 1
		###print(F"Remaining PS Count: {i1}")
	# PS終了処理
	AddStr = "(END) " + str(Cnt) + " Count"
	if Cnt > 1:
		AddStr += "s"
	print(H1_BGN + AddStr + H1_END)

def Sub_Args_St1_ContextMenu(e):
	obj1 = Args_St1
	obj2 = None
	if obj1.tag_ranges("sel"):
		obj2 = St_ContextMenu_Select
	else:
		obj2 = St_ContextMenu_All
	obj2.post(e.x_root, e.y_root)

def Sub_St_Clear_Select(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.delete("sel.first", "sel.last")
	return inner

def Sub_St_Clear_All(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.delete("1.0", "end")
	return inner

def Sub_St_Copy_Select(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get("sel.first", "sel.last"))
	return inner

def Sub_St_Copy_All(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get("1.0", "end-1c"))
	return inner

def Sub_St_Cut_Select(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get("sel.first", "sel.last"))
		obj.delete("sel.first", "sel.last")
	return inner

def Sub_St_Cut_All(obj = None, e = None):
	if obj == None:
		return
	def inner():
		obj.clipboard_clear()
		obj.clipboard_append(obj.get("1.0", "end-1c"))
		obj.delete("1.0", "end")
	return inner

def Sub_St_Paste_Select(obj = None, e = None):
	if obj == None:
		return
	def inner():
		try:
			text = Win0.selection_get(selection = "CLIPBOARD").rstrip()
			obj.delete("sel.first", "sel.last")
			obj.insert("insert", text + "\n")
			obj.see("insert")
		except:
			pass
	return inner

def Sub_St_Paste_All(obj = None, e = None):
	if obj == None:
		return
	def inner():
		try:
			text = Win0.selection_get(selection = "CLIPBOARD").rstrip()
			obj.insert("insert", text + "\n")
			obj.see("insert")
		except:
			pass
	return inner

#-------------------------------------------------------------------------------
# Window [0]
#-------------------------------------------------------------------------------
Win0 = Tk.Tk()

# Window 初期サイズ
min = {
	"W": 480,
	"H": 200
}
# Window 初期ポジション
pos = {
	"X": int((Win0.winfo_screenwidth() - min["W"]) / 2),
	"Y": int((Win0.winfo_screenheight() - min["H"]) / 2)
}
Win0.bind("<Configure>", Sub_Win0_Resize)
Win0.configure(bg = "#555")
Win0.geometry(f'{min["W"]}x{min["H"]}+{pos["X"]}+{pos["Y"]}')
Win0.minsize(width = min["W"], height = min["H"])
Win0.resizable(width = True, height = True)
Win0.title(PROGRAM + " " + VERSION)
# 使用不可：Windows,Linux互換問題
#   Win0.attributes()

#-------------------------------------------------------------------------------
# Command & Option
#-------------------------------------------------------------------------------
List_Cmd_Lbl1 = Tk.Label(text = "YT-DLP コマンド", font = ("Helvetica", 10, "bold"), fg = "white", bg = "#555")

a1 = List_Cmd.strip().split("\n")
List_Cmd_Cb1 = Tk_Ttk.Combobox(Win0, font = ("Courier", 10), values = (a1))
obj1 = List_Cmd_Cb1
obj1.bind("<Button-3>", Sub_List_Cmd_Cb1_ContextMenu)
obj1.insert("end", a1[0])
a1 = []

# 範囲指定あり
Cb_ContextMenu_Select = Tk.Menu(Win0, tearoff = 0, font = ("Helvetica", 10))
obj1 = Cb_ContextMenu_Select
obj1.add_command(label = "クリア", command = Sub_Cb_Clear_Select(obj = List_Cmd_Cb1))
obj1.add_separator()
obj1.add_command(label = "コピー", command = Sub_Cb_Copy_Select(obj = List_Cmd_Cb1))
obj1.add_command(label = "カット", command = Sub_Cb_Cut_Select(obj = List_Cmd_Cb1))
obj1.add_command(label = "ペースト", command = Sub_Cb_Paste_Select(obj = List_Cmd_Cb1))

# 範囲指定なし
Cb_ContextMenu_All = Tk.Menu(Win0, tearoff = 0, font = ("Helvetica", 10))
obj1 = Cb_ContextMenu_All
obj1.add_command(label = "全クリア", command = Sub_Cb_Clear_All(obj = List_Cmd_Cb1))
obj1.add_separator()
obj1.add_command(label = "全コピー", command = Sub_Cb_Copy_All(obj = List_Cmd_Cb1))
obj1.add_command(label = "全カット", command = Sub_Cb_Cut_All(obj = List_Cmd_Cb1))
obj1.add_command(label = "ペースト", command = Sub_Cb_Paste_All(obj = List_Cmd_Cb1))

List_Cmd_Exec_Btn1 = Tk.Button(Win0, text = "実行", font = ("Helvetica", 10), fg = "#ffffff", bg = "crimson", relief = "flat", cursor = "hand2", command = Sub_List_Cmd_Exec_Btn1)

#-------------------------------------------------------------------------------
# Argument
#-------------------------------------------------------------------------------
Args_Lbl1 = Tk.Label(text = "YouTube URL（改行区切り）", font = ("Helvetica", 10, "bold"), fg = "white", bg = "#555")

Args_St1 = Tk_St.ScrolledText(Win0, font = ("Courier", 11), relief = "flat", borderwidth = 0, undo = "true", insertofftime = 0)
obj1 = Args_St1
obj1.bind("<Button-3>", Sub_Args_St1_ContextMenu)
obj1.configure(state = "normal")

# 範囲指定あり
St_ContextMenu_Select = Tk.Menu(Win0, font = ("Helvetica", 10), tearoff = 0)
obj1 = St_ContextMenu_Select
obj1.add_command(label = "クリア", command = Sub_St_Clear_Select(obj = Args_St1))
obj1.add_separator()
obj1.add_command(label = "コピー", command = Sub_St_Copy_Select(obj = Args_St1))
obj1.add_command(label = "カット", command = Sub_St_Cut_Select(obj = Args_St1))
obj1.add_command(label = "ペースト", command = Sub_St_Paste_Select(obj = Args_St1))

# 範囲指定なし
St_ContextMenu_All = Tk.Menu(Win0, font = ("Helvetica", 10), tearoff = 0)
obj1 = St_ContextMenu_All
obj1.add_command(label = "全クリア", command = Sub_St_Clear_All(obj = Args_St1))
obj1.add_separator()
obj1.add_command(label = "全コピー", command = Sub_St_Copy_All(obj = Args_St1))
obj1.add_command(label = "全カット", command = Sub_St_Cut_All(obj = Args_St1))
obj1.add_command(label = "ペースト", command = Sub_St_Paste_All(obj = Args_St1))

Args_Clear_Btn1 = Tk.Button(Win0, text = "クリア", font = ("Helvetica", 9), fg = "white", bg = "navy", relief = "flat", cursor = "hand2", command = Sub_St_Clear_All(obj = Args_St1))
Args_Paste_Btn1 = Tk.Button(Win0, text = "ペースト", font = ("Helvetica", 9), fg = "white", bg = "mediumblue", relief = "flat", cursor = "hand2", command = Sub_St_Paste_All(obj = Args_St1))

#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------
List_Cmd_Lbl1.place(x = 5, y = 3)
List_Cmd_Cb1.place(x = 5, y = 23, height = 20)
List_Cmd_Exec_Btn1.place(y = 23, width = 62, height = 20)
Args_Lbl1.place(x = 5, y = 53)
Args_St1.place(x = 5, y = 73)
Args_Clear_Btn1.place(y = 53, width = 62, height = 20)
Args_Paste_Btn1.place(y = 53, width = 80, height = 20)

# 前処理
Sub_Terminal_Reposition()
Sub_Clear()
Sub_YtDlp_Update()
List_Cmd_Cb1.focus_force()

Win0.mainloop()
Win0.quit()

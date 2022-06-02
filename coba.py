import pyperclip
text = pyperclip.paste()
print(text)
splitText = (text.splitlines())
for x in splitText:
	print(x)
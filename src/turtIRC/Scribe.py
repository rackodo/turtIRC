import turtle
import re

# Mappings from ASCII decimal values to encrypted turtle movement instructions.
AsciiTable = {
	32: "", # 
	# 33: "", # !
	# 34: "", # "
	# 35: "", # #
	# 36: "", # $
	# 37: "", # %
	# 38: "", # &
	# 39: "", # '
	# 40: "", # (
	# 41: "", # )
	# 42: "", # *
	# 43: "", # +
	# 44: "", # ,
	# 45: "", # -
	# 46: "", # .
	# 47: "", # /
	# 48: "", # 0
	# 49: "", # 1
	# 50: "", # 2
	# 51: "", # 3
	# 52: "", # 4
	# 53: "", # 5
	# 54: "", # 6
	# 55: "", # 7
	# 56: "", # 8
	# 57: "", # 9
	# 58: "", # :
	# 59: "", # ;
	# 60: "", # <
	# 61: "", # =
	# 62: "", # >
	# 63: "", # ?
	# 64: "", # @
	65: "F10 R90 F20 R90 U F10 R90 D F20 B10 R90 F10 B10 L90 F10 R90", # A
	66: "F7 R90 F10 L90 F3 R90 F10 R90 F10 R90 F10 R90 F10 B10 L90 F10 R90", # B
	67: "F10 R90 U F20 R90 D F10 R90 F20 R90", # C
	68: "F8 R90 F2 L90 F2 R90 F16 R90 F2 L90 F2 R90 F8 R90 F20 R90", # D
	69: "F10 B10 R90 F10 L90 F5 B5 R90 F10 L90 F10 B10 L90 F20 R90", # E
	70: "F10 B10 R90 F10 L90 F10 B10 R90 F10 B20 L90", # F
	71: "F10 U R90 F10 D R90 F5 B5 L90 F10 R90 F10 R90 F20 R90", # G
	72: "U F10 R90 D F10 R90 F10 B10 L90 F10 R90 U F10 D R90 F20 R90", # H
	73: "F10 R90 U F20 D R90 F5 R90 F20 B20 L90 F5 U R90 F20 R90", # I
	74: "F10 B5 R90 F20 R90 F5 R90 F10 U F10 R90", # J
	75: "R90 F10 L90 F7 L90 F10 B10 R90 F3 R90 F10 B10 L90 B10 L90 B10 F20 R90", # K
	76: "R90 F20 L90 F10 B10 L90 F20 R90", # L
	77: "R90 F20 B20 L90 F5 R90 F15 B15 L90 F5 R90 F20 B20 L90 B10", # M
	78: "F5 R90 F20 L90 F5 L90 F20 L90 U F10 L90 D F20 B20 L90", # N
	79: "F10 R90 F20 R90 F10 R90 F20 R90", # O
	80: "F10 R90 F10 R90 F10 R90 B10 F20 R90", # P
	81: "F10 R90 F20 R90 R45 F10 B10 L45 F10 R90 F20 R90", # Q
	82: "F7 R90 F10 L90 F3 R90 F10 R90 U F10 R90 D F10 R90 F10 B10 L90 F10 R90", # R
	83: "F10 R90 U F10 D F10 R90 F10 R90 U F10 R90 D F10 B10 L90 F10 R90", # S
	84: "F10 B5 R90 F20 B20 L90 B5", # T
	85: "U F10 R90 D F20 R90 F10 R90 F20 R90", # U
	86: "R90 F20 L90 F5 L90 F10 R90 F5 L90 F10 R90 U B10", # V
	87: "R90 F20 L90 F5 L90 F10 B10 R90 F5 L90 F20 R90 U B10", # W
	88: "R66 F22 B22 L66 U F10 D L66 B22 F22 R66 U B10", # X
	89: "U F10 R90 D F10 R90 F10 B10 L90 F10 R90 F10 R90 U F10 D F10 R90", # Y
	90: "F10 R90 F10 R90 F10 L90 F10 L90 F10 B10 L90 U F20 R90", # Z
	# 91: "", # [
	# 92: "", # \
	# 93: "", # ]
	# 94: "", # ^
	# 95: "", # _
	# 96: "", # `
	# 123: "", # {
	# 124: "", # |
	# 125: "", # }
	# 126: "" # ~
}

def ScribeString(
		t: turtle.Turtle, 
		ref: list, 
		string : str, 
		x : int, 
		y : int
		):
	for index, letter in enumerate(string):
		ScribeChar(t, letter, ref[x + index][y])

def ScribeChar(
		t : turtle.Turtle, 
		char : str, 
		pos : tuple[float, float]
		):
	if len(char) > 1: 
		raise ValueError("Provided string is more than one character")
		return

	if ord(char.upper()) not in AsciiTable:
		raise IndexError("Provided character isn't currently supported")
		return
	
	turtleString = AsciiTable[ord(char.upper())]

	turtleCommands = re.findall(r'([FLRUDB])(\d*)', turtleString)

	t.goto(pos)

	t.pendown()
	# Decrypts encrypted turtle instructions and executes upon them.
	for command, value in turtleCommands:
		if command in 'FLRB':  # Movement or Rotation commands
			value = int(value) if value else 0  # Convert number part to integer, default 0 if missing
			if command == 'F':  # Move forward
				t.forward(value)
			elif command == 'B':
				t.backward(value)
			elif command == 'L':  # Turn left
				t.left(value)
			elif command == 'R':  # Turn right
				t.right(value)
		elif command == 'U':  # Pen Up
			t.penup()
		elif command == 'D':  # Pen Down
			t.pendown()
	t.penup()
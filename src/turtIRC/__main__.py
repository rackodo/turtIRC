import turtle
from turtIRC.Scribe import ScribeString

winWidth = 998
winHeight = 498
padding = 2

rows = 22
columns = 82

gridPosReference = [['' for _ in range(rows)] for _ in range(columns)]
gridContents = [['' for _ in range(rows)] for _ in range(columns)]

def main():
	# Screen initialisation
	screen = turtle.Screen()
	screen.tracer(0)

	screen.setup(winWidth, winHeight)

	t = turtle.Turtle()

	t.penup()
	t.goto(-(winWidth / 2) + padding + 1, (winHeight / 2) - padding - 1)

	# Prepares the grid! Sets screen positions for every possible character position and saves it to the grid dictionary for referral.
	for r in range(0, rows):
		for c in range(0, columns):
			gridPosReference[c][r] = (t.pos()[0], t.pos()[1])
			t.forward(10 + padding)
		
		t.goto((-(winWidth / 2) + padding + 1), t.pos()[1])
		t.right(90)
		t.forward(20 + padding)
		t.left(90)

	ScribeString(t, gridPosReference, "abcdefghijklmnopqrstuvwxyz", 0, 0)
	ScribeString(t, gridPosReference, "0123456789", 0, 1)

	turtle.mainloop()

if __name__ == "__main__":
	main()
import turtle
from turtIRC.Scribe import ScribeString

winWidth = 998
winHeight = 498
padding = 2

rows = 22
columns = 82

grid = [[(None, None) for row in range(0, rows)] for col in range(0, columns)]

scale = 1

""" 
Right! Here's the plan:
- IRC client (to be written) will write to a log file that will be then read to draw characters to the screen.
"""

def main():
	screen = turtle.Screen()
	screen.tracer(0)

	screen.setup(winWidth, winHeight)

	t = turtle.Turtle()

	t.penup()
	t.goto(-(winWidth / 2) + padding + 1, (winHeight / 2) - padding - 1)

	for r in range(0, rows):
		for c in range(0, columns):
			grid[c][r] = (t.pos()[0], t.pos()[1])
			t.forward((10 * scale) + padding)
		
		t.goto((-(winWidth / 2) + padding + 1), t.pos()[1])
		t.right(90)
		t.forward((20 * scale) + padding)
		t.left(90)

	ScribeString(t, grid, "according to all known laws of aviation there is", (1, 0))

	turtle.mainloop()

if __name__ == "__main__":
	main()
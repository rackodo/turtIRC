import turtle
from turtIRC.GlobalVars import *
from turtIRC.Scribe import CommitString, RenderContents

winWidth = 998
winHeight = 498
padding = 2

def main():
	# Screen initialisation
	screen = turtle.Screen()
	screen.tracer(0)

	screen.setup(winWidth, winHeight)

	t = turtle.Turtle()

	t.penup()
	t.goto(-(winWidth / 2) + padding + 1, (winHeight / 2) - padding - 1)

	# Prepares the grid! Sets screen positions for every possible character position and saves it to the grid dictionary for referral.
	for r in range(rows):
		for c in range(columns):
			gridPosRef[r][c] = (t.pos()[0], t.pos()[1])
			t.forward(10 + padding)
		
		t.goto((-(winWidth / 2) + padding + 1), t.pos()[1])
		t.right(90)
		t.forward(20 + padding)
		t.left(90)

	f = open('sample.txt')

	for line in f.read().splitlines():
		CommitString(t, line)

	RenderContents(t)

	turtle.mainloop()

if __name__ == "__main__":
	main()
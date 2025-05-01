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

	# ScribeString(t, gridPosReference, "abcdefghijklmnopqrstuvwxyz", 0, 0)
	# ScribeString(t, gridPosReference, "0123456789", 0, 1)

	ScribeString(t, gridPosReference, "<+swee> re: pygame irc cleint", 0, 0 )
	ScribeString(t, gridPosReference, "<+racko> cos that's how the actual client's gonna work, it prints to a buffer file", 0, 1)
	ScribeString(t, gridPosReference, "<+swee> s/ei/ie", 0, 2)
	ScribeString(t, gridPosReference, "<+Cl4ir> [Sed] <swee> re: pygame irc client", 0, 3)
	ScribeString(t, gridPosReference, "<+zoid> s/screenshots/renderings/", 0, 4)
	ScribeString(t, gridPosReference, "<+Cl4ir> [Sed] <zoid> swee: do you have any renderings of what this would look lik", 0, 5)
	ScribeString(t, gridPosReference, "<+zoid> my apologies", 0, 6)
	ScribeString(t, gridPosReference, "<+swee> renderings of what, the pygame irc client? :,3", 0, 7)
	ScribeString(t, gridPosReference, "<+zoid> dammit lol", 0, 8)
	ScribeString(t, gridPosReference, "<+zoid> RACKO", 0, 9)
	ScribeString(t, gridPosReference, "<+zoid> I can’t read swee", 0, 10)
	ScribeString(t, gridPosReference, "<+racko> WHA", 0, 11)
	ScribeString(t, gridPosReference, "<+racko> what", 0, 12)
	ScribeString(t, gridPosReference, "<+zoid> racko do you have any renderings on what a turtle irc client would look li", 0, 13)
	ScribeString(t, gridPosReference, "<+racko> uh", 0, 14)
	ScribeString(t, gridPosReference, "<+racko> gimme a sec", 0, 15)
	ScribeString(t, gridPosReference, "<+shmoo> I was promised non-GUI / TUI only client", 0, 16)
	ScribeString(t, gridPosReference, "<+shmoo> ASSURED…", 0, 17)

	turtle.mainloop()

if __name__ == "__main__":
	main()
from turtIRC.AsciiToTurtle import AsciiTable

message = "Hello world!"

for char in message:
	print(AsciiTable[ord(char)])
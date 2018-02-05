'''
WHEN UPDATING THE PROGRAM, UPDATE "quality", "qualitytheo", and and "qualitieshelp"

True	1	2	3	4	5	6	7	8	9	10	11	12	13
Code	0	2	4	5	7	9	11	12	14	16	17	19	21		

				Notation	True			Code
Major						1,3,5			0,4,7
Minor			m			1,3b,5			0,3,7
Aug				aug			1,3,5+			0,4,8
Diminished		dim			1,3b,5b			0,3,6
Sus				sus			1,3+,5			0,5,7
						
Seventh			7			1,3,5,7b 		0,4,7,10
Ninth,Second	9, 2		1,3,5,7b,9		0,4,7,10,14
Eleventh		11			1,3,5,7b,11		0,4,7,10,17
Thirteenth		13			1,3,5,7b,13		0,4,7,10,21
					
Major Seventh	maj7		1,3,5,7			0,4,7,11
Major Ninth		maj9		1,3,5,7,9		0,4,7,11,14
					
Minor Sixth		m6			1,3b,5,6		0,3,7,9
Minor Seventh	m7			1,3b,5,7b 		0,3,7,10
Minor Ninth		m9			1,3b,5,7b,9		0,3,7,10,14
Minor Major 7	m#7			1,3b,5,7		0,3,7,11
Minor 7th,5b	m7(5b)		1,3b,5b,7b		0,3,6,10
					
Sixth			6			1,3,5,6			0,4,7,9
Sixth w/Ninth	6/9			1,3,5,6,9		0,4,7,9,14
Seventh/5b		7(5b)		1,3,5b,7b		0,4,6,10
Seventh/9b		7(9b)		1,3,5,7b,9b		0,4,7,10,13
Diminished 7th	dim7		1,3b,5b,7bb		0,3,6,9

Major Eleventh	maj11		1,3,5,7,9,11	0,4,7,11,14,17
'''
notenum = {"C":1, "C#":2, "D":3, "D#":4, "E":5, "F":6, "F#":7, "G":8, "G#":9, "A":10, "A#":11, "B":12}
notename = {1:"C", 2:"C#", 3:"D", 4:"D#", 5:"E", 6:"F", 7:"F#", 8:"G", 9:"G#", 10:"A", 11:"A#", 12:"B"}

quality = {"maj":[0,4,7],"m":[0,3,7],"aug":[0,4,8],"dim":[0,3,6],"sus":[0,5,7],"7":[0,4,7,10],\
				"9":[0,4,7,10,14],"2":[0,4,7,10,14],"11":[0,4,7,10,17],"13":[0,4,7,10,21],\
				"maj7":[0,4,7,11],"maj9":[0,4,7,11,14],\
				"m6":[0,3,7,9],"m7":[0,3,7,10],"m9":[0,3,7,10,14],"m#7":[0,3,7,11],"m7(5b)":[0,3,6,10],\
				"6":[0,4,7,9],"6/9":[0,4,7,9,14],"7(5b)":[0,4,6,10],"7(9b)":[0,4,7,10,13],"dim7":[0,3,6,9],\
				"maj11":[0,4,7,11,14,17]}

qualitytheo = {"maj":['1','3','5'],"m":['1','3b','5'],"aug":['1','3','5#'],"dim":['1','3b','5b'],"sus":['1','3#','5'],"7":['1','3','4','7b'],\
				"9":['1','3','5','7b','9'],"2":['1','3','5','7b','9'],"11":['1','3','5','7b','11'],"13":['1','3','5','7b','13'],\
				"maj7":['1','3','5','7'],"maj9":['1','3','5','7','9'],\
				"m6":['1','3b','5','6'],"m7":['1','3b','5','7b'],"m9":['1','3b','5','7b','9'],"m#7":['1','3b','5','7'],"m7(5b)":['1','3b','5b','7b'],\
				"6":['1','3','5','6'],"6/9":['1','3','5','6','9'],"7(5b)":['1','3','5b','7b'],"7(9b)":['1','3','5','7b','9b'],"dim7":['1','3b','5b','7bb'],\
				"maj11":['1','3','5','7','9','11']}

def chord_comps(strChord):
	lstChordComps = strChord.strip().split(" ")
	if len(lstChordComps) == 1:
		lstChordComps.append("maj")
	lstChordComps[0] = lstChordComps[0].upper()
	return lstChordComps

def chord_create(lstChordComps):
	root = lstChordComps[0]
	finalchord = []
	chordaddition = quality[lstChordComps[1]]
	chordnum = [note + notenum[root] for note in chordaddition]
	newchordnum = [x - 12 if x > 12 else x for x in chordnum]
	finalchord = [notename[num] for num in newchordnum]
	return finalchord, qualitytheo[lstChordComps[1]]

def help():
	print("This is a guitar chord construction app!")
	print("Enter 'qualities' to see the library of qualities available in this app.")
	print("Enter 'formatting' for help with formatting chords")

def formatting():
	print("To find the construction of a chord, enter the chord with the root separated from the quality.")
	print("For example, to find F7, enter 'F 7', the F and 7 separated by a space. 'G aug' will return the construction of G augmented.")
	print("Both 'C' and 'C maj' will return the construction for a C major chord.")

def qualitieshelp():
	print("QUALITY			INPUT")
	print("Major			maj")
	print("Minor			m")
	print("Aug			aug")
	print("Diminished		dim")
	print("Sus			sus")				
	print("Seventh			7")
	print("Ninth,Second		9, 2")
	print("Eleventh		11")
	print("Thirteenth		13")		
	print("Major Seventh		maj7")
	print("Major Ninth		maj9")
	print("Minor Sixth		m6")
	print("Minor Seventh		m7")
	print("Minor Ninth		m9")
	print("Minor Major 7		m#7")
	print("Minor 7th,5b		m7(5b)")
	print("Sixth			6")
	print("Sixth w/Ninth		6/9")
	print("Seventh/5b		7(5b")
	print("Seventh/9b		7(9b")
	print("Diminished 7th		dim7")
	print("Major 11th		maj11")

def incorrectinp():
	print("The chord you entered was not entered correctly. Please check the formatting.")
	print("Enter 'formatting' for help with formatting or 'qualities' for a list of qualities available.")
	print("You can also enter 'help' for more help.")

def main():
	print("Enter a guitar chord to find out its construction. To quit, enter q.")
	userinp = input()

	while userinp != "q":
		if userinp == "help":
			help()
		elif userinp == "formatting":
			formatting()
		elif userinp == "qualities":
			qualitieshelp()
		elif chord_comps(userinp)[0] not in notenum or chord_comps(userinp)[1] not in quality:
			incorrectinp()
		else:
			chordOut,qualityOut = (chord_create(chord_comps(userinp)))
			print(chordOut)
			print(qualityOut)
		print()
		print("Enter a guitar chord to find out its construction. To quit, enter q.")
		userinp = input()
main()












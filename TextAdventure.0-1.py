print("\033[2J")    #Clear Console
print("\033[0;0H")  #Move cursor to origin

from gameData import *

userCmd = None
userLoop = True
cmdLoop = True

while userLoop:
	restOfCmd = ''
	userCmd = input("\nWhat would you like to do?  ").lower().strip()
	cmdIN = userCmd
	while cmdLoop:
		print(f"\ncmdLoop cmdIN: '{cmdIN}'")
		print(f"(userCmd: '{userCmd}')")
		firstSpace = cmdIN.find(" ")                                                                                                                                                                                                                                                                                                                                                                                                             
		print (f"firstSpace: {firstSpace}")

		if firstSpace == -1:
			firstWord = cmdIN
		else:                                                                                       
			firstWord = cmdIN[:firstSpace]
			restOfCmd = cmdIN[firstSpace:]
		print(f"firstWord|restOfCmd is '{firstWord}|{restOfCmd}'")

		if firstWord in verbList:
			print(f"'{firstWord}' found in verbList")
			print(f"<Code to process '{firstWord}|{restOfCmd}' here>")
			#<LATER: process the verb + noun cmdIN>
				#<1. cmdIN is verb only?>
				#<2. cmdIN is verb + noun?>
			break

		elif firstWord in dirALT:
			altWord = dirALT[firstWord]
			cmdIN = altWord+ restOfCmd
			print(f"'{firstWord}:{altWord}' found in dirALT.")
			print(f"Substituted cmdIN: '{cmdIN}'")
			continue

		elif firstWord in dirList:
			print(f"'{firstWord}' found in dirList")
			firstWord = 'go ' + firstWord
			cmdIN = firstWord + restOfCmd
			print(f"Substituted cmdIN: '{cmdIN}'")
			continue

		elif firstWord in dirALT:
			altWord = dirALT[firstWord]
			cmdIN = altWord+ restOfCmd
			print(f"'{firstWord}:{altWord}' found in verbDictALT.")
			continue

		else:
			print(f"\n'{userCmd}' is an INVALID COMMAND.  Please try again.")
			break
				
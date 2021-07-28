def formatName(firstName,lastName):
	if firstName == "" or lastName == "":
		return "You didn't type anything"
	proper_first = firstName.title()
	proper_last = lastName.title()
	name = proper_first + " " +proper_last 

	return name


print(formatName("KLAY", "tHOmpSOn"))

function reverse(s){
	// Split -> Separates the elements of the string into an array
	// Reverse -> Reverse the elements of an array
	// Join -> Join the elements of an array into a string, separating they 
	//			using the char passed as arg. Comma is the default, if no arg is passed
    return s.split("").reverse().join("");
}
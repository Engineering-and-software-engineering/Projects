function isPrime(number) {

	var start = 2;
	while (start <= Math.sqrt(number)) {
	if (number % start++ < 1) return false;
	}
	return number > 1;

}

function nextPrime(num){

	num += 1;
	while(!isPrime(num)) num += 1;
	return num;	

}

function printNextPrime(){
		
	var move = true;
	var curr = 1;

	while(move){
		console.log("Current prime:" + curr);
		move = confirm("Press OK to continue:");
		curr = nextPrime(curr);		
	}

};
printNextPrime();

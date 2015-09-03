class CheckPalindrome
=begin
  Author: Jessica Valenti
  Date: September 2, 2015
  Script that determines if a string is a palindrome or not.
=end

  def checkPalindrome(word)
    reversedWord = word.reverse
    if (word == reversedWord)
      puts "#{word} is a palindrome!"
    else
      puts "#{word} is not a palindrome :("
    end
  end

  puts "Which string would you like to check?"
  word = gets.chomp.downcase

  palindromeObject = CheckPalindrome.new
  palindromeObject.checkPalindrome(word)
end
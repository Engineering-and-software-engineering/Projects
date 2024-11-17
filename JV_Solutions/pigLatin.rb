class PigLatin
=begin
        Author : Jessica Valenti
        September 1, 2015
        Script created to "translate" English words into pig latin (based on the pig latin wikipedia page) - in response to Karan's list of projects
=end

puts "please write a word to be translated to pig latin"
word = gets.chomp
length = word.length

while length < 3
  puts "please write a word to be translated to pig latin (longer than two letters)"
  word = gets.chomp
  length = word.length
end

vowels = ["a", "e", "i", "o", "u", "y"]

if vowels.include? word[0, 1]
  pig_latin = word << "yay"
elsif vowels.include? word[1]
  pig_latin = word[1, length] << word[0, 1] << "ay"
else
  pig_latin = word[2, length] << word[0, 2] << "ay"
end

puts pig_latin

end
class ChangeReturn

=begin
  Author: Jessica Valenti
  September 3, 2015
  Change Return Program - user enters a cost and then the amount of money given.  The program
  will figure out the change and the number of quarters, dimes, nickels and pennies needed for the change.
=end

  require 'bigdecimal' # used because Float and Integer data types aren't ideal for money transactions

  puts "What is the cost?"
  cost = BigDecimal(gets.chomp)

  puts "What amount is given?"
  moneyGiven = BigDecimal(gets.chomp)

  while (cost > moneyGiven)
    puts "The amount given must be greater than the cost. What amount is given?"
    moneyGiven = BigDecimal(gets.chomp)
  end

  change = BigDecimal(moneyGiven) - BigDecimal(cost)
  changeDollars = change.to_i
  changeCents = (change - changeDollars)*100 # multiplied by 100 to use pennies

  coin_values = {
      "quarters" => 25,
      "dimes" => 10,
      "nickels" => 5,
      "pennies" => 1
  }

  coinNames = ["quarters", "dimes", "nickels", "pennies"]
  num = 0 # will be used to iterate through the names array above

  puts "Your change is $" << sprintf('%.2f', change)

  coin_values.each do |numCoins, value|
    numCoins = changeCents / value
    numCoins = numCoins.to_i # changed to integer to remove any decimal point on the num of coins
    changeCents -= numCoins*value
    puts "Number of #{coinNames[num]}: #{numCoins}" if numCoins > 0
    num +=1 # to go to the next name in the array
  end
end
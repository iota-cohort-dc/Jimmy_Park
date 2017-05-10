def guess_number guess
    number = 25
    if guess == number
      puts "You got it!"
    elsif guess > number
      puts "Guess was too high!"
    else
      puts "Guess was too low!"
    end
end
puts guess_number 15
puts guess_number 132
puts guess_number 12
puts guess_number 1
puts guess_number 25

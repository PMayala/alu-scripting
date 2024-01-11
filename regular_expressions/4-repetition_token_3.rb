#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Please provide an argument."
else
  # Get the argument
  input_string = ARGV[0]

  # Define the regular expression pattern using Oniguruma syntax
  regex_pattern = /hbt*n/

  # Match the input against the regular expression
  if input_string.match?(regex_pattern)
    puts input_string.scan(regex_pattern).join
  else
    puts "No match found."
  end
end

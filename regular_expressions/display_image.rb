require 'base64'

image_file = File.read("9-passed_linkedin_regex_challenge.jpg")
image_base64 = Base64.strict_encode64(image_file)

puts "<img src='data:image/jpg;base64,#{image_base64}'>"

# count vowels
# a,e,i,o,u

input_string = input(("Enter a string \n"))
vowels = "aeiou"
vowels_count = 0
consonant_count = 0
vowel_list = list()
consonant_list = list()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count + 1
        vowel_list.append(char)
    else:
        consonant_count = consonant_count + 1
        consonant_list.append(char)


print(vowels_count)
print(vowel_list)
print(consonant_count)
print(consonant_list)
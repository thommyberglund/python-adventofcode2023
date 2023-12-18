file = open('input.txt', 'r')
lines = file.read().splitlines()

card_counter = [1] * len(lines)
total_lines = 0

for index, line in enumerate(lines):
   matches = []
   cardnumber = line.lstrip("Card")[:4].strip()
   numbers = line.lstrip("Card")[5:]
   winningnumbers = numbers.partition("|")[0].split()
   mynumbers = numbers.partition("|")[2].split()
   for number in winningnumbers:
      if number in mynumbers:
         matches.append(number)
   for n in range(len(matches)):
      card_counter[index + n  + 1] += card_counter[index]
print(str(sum(card_counter)))
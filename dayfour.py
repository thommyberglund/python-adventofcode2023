class Card:
   def __init__(self,cardnumber, winningnumbers,mynumbers):
      self.cardnumber = cardnumber
      self.mynumbers = mynumbers
      self.winningnumbers = winningnumbers
   def __str__(self):
      return f'Cardnumber: {self.cardnumber}, winning numbers: {self.winningnumbers}, my numbers: {self.mynumbers}'
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
   def insert(self, data):
      if self.data:
         if data.cardnumber < self.data.cardnumber:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data.cardnumber > self.data.cardnumber:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
         else:
            self.data = data
# Print the Tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print(f"Something here"),
      if self.right:
         self.right.PrintTree()
# Preorder traversal
# Root -> Left ->Right
   def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res
   
count = 0
with open('input.txt','r') as reader:
    for line in reader:
      # print(line)
       cardnumber = line.lstrip("Card")[:4].strip()
       numbers = line.lstrip("Card")[5:]
       winningnumbers = numbers.partition("|")[0].split()
       mynumbers = numbers.partition("|")[2].split()
      # print(f"Card: {cardnumber}")
      # print(f"Numbers: {numbers}")
       card = Card(cardnumber,winningnumbers,mynumbers)
       if(count == 0):
           #print(str(card))
           root = Node(card)
       else:
          root.insert(card)
       count = count + 1





""""
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42) """
for item in root.PreorderTraversal(root):
   print(str(item))
   print("\n")

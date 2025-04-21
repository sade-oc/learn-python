#Task 1
def format_file(file):
   with open(file, 'r') as f:
      lines = f.readlines()
      i = 1; 
      for line in f:
         print(i , line.strip)
         i += 1
      f.close()
      return lines

format_file("example.txt")
#Importing packages used in our code
import random #creates random generator
import io #Helps with file making (writing, reading, open)

def dnaSequence():
  #nucleotide list A T C G
  nucList = list("ATCG")

  #empty lists of the first 2 sub sets
  subrepeatA = ""
  subrepeatB = ""

  #first subset to make a sequence for the first subset
  count1 = random.randrange(1,76) #picks a random number/ amount for how many nucleotides there should be
  for i in range(0,count1):
    subrepeatA += random.choice(nucList) #adds the random combination of nucleotides to the empty list

  count2 = 150-count1 #number for amount of nucleotides in second subset
  for i in range(0,count2):
    subrepeatB += random.choice(nucList)#adds the random combination to the string

  largeSubset = subrepeatA + subrepeatB + subrepeatA + subrepeatB #large subset adds the 2 sets together twice to get total of 300

  return(largeSubset) 

#Putting the function into a variable
spidroin = dnaSequence()

# Second function

#Ask the user what they want the file name and heading to be for the file
filename = input("File name is: ")
fileheader = input("file header is: ")

#Second function to make the sequence created in the first function into a fasta file.
def SpidroinFile(filename, fileheader):
  try: #try block helps avoid errors
    with open(filename + ".fasta", "w") as spidroinFile_handle:#includes title of the file inputted and set it as a handle (spidroinFile_handle)
      spidroinFile_handle.write(">"+ fileheader + "\n") #this writes the fileheader and \n helps make the sequence on the next line
      spidroinFile_handle.write(spidroin) #adding the sequence to the file
  except IOError as err:
    print("there's an error")
  return(spidroinFile_handle) #returning the handle

SpidroinFile(filename, fileheader) #calling the function so that it makes the file.


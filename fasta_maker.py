#Importing packages used in our code
import random #creates random generator
import io #Helps with file making (writing, reading, open)

#First function: Generates a random spidroin sequence with 2 smaller subsets (total of 300 nuceotides)
def dnaSequence():
  #creates nucleotide list A T C G
  nucList = list("ATCG")

  #empty lists of the first 2 sub sets
  subrepeatA = ""
  subrepeatB = ""

  #first subset to make a sequence for the first subset

  #random.randrange(1,76) picks a random number/ amount for how many nucleotides there should be
  #the for loop adds the random combination of nucleotides to the empty list
  count1 = random.randrange(1,76) 
  for i in range(0,count1):
    subrepeatA += random.choice(nucList) 
  
  #number for amount of nucleotides in second subset
  #for loop adds the random combination to the string
  count2 = 150-count1 
  for i in range(0,count2):
    subrepeatB += random.choice(nucList)

  #large subset adds the 2 sets together twice to get total of 300
  largeSubset = subrepeatA + subrepeatB + subrepeatA + subrepeatB 

  return(largeSubset) 

#Putting the function into a variable
spidroin = dnaSequence()


#Second function to make the sequence created in the first function into a fasta file.

#Ask the user what they want the file name and heading to be for the file
filename = input("File name is: ")
fileheader = input("file header is: ")

#try block helps avoid errors
#the with open(filename.fasta, "w") includes title of the file inputted and set it as a handle (spidroinFile_handle)
#.write(">"+ fileheader + "\n") writes the fileheader and \n helps make the sequence on the next line
#.write(spidroin) adds the sequence to the file
#return the handle
def SpidroinFile(filename, fileheader):
  try: 
    with open(filename + ".fasta", "w") as spidroinFile_handle:
      spidroinFile_handle.write(">"+ fileheader + "\n") 
      spidroinFile_handle.write(spidroin) 
  except IOError as err:
    print("there's an error")
  return(spidroinFile_handle) 

#calling the function so that it makes the file.
SpidroinFile(filename, fileheader) 


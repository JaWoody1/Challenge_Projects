import string

#Find the longest word in a string
#IGNORE ALL PUNCTUATION
#Numbers are okay


#function that finds the longest word
def LongestWord(sen):

  # splits the string into a list
  long = sen.split(" ")


  #for loop that uses the length of the list to go through each word  
  for i in range(len(long)):

    # Make a translation table that maps all punctuation characters to None
    translator = str.maketrans("", "", string.punctuation)

    # Apply the translation table to each word in the list
    long[i] = long[i].translate(translator)
    
    #if its not the first word
    if i != 0:
      #get the length of the current word in the loop
      length = len(long[i])
      #if that length is greater than the current longest word (sen)
      if length > len(sen):
        #make sen the new word
        sen = long[i]
      else:
        #do nothing if its not longer
        continue


    #first word is set to the longest word
    elif i == 0:
      sen = long[i]
  



  return sen

#calls LongestWord function with user input
print(LongestWord(input()))
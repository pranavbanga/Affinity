#Assumptions:
              1. The given file is csv file and it has single column which includes n number of rows and each row depicts a single tweet.
              2. degree of profanity here shows the count of words that indicates racial slurs.
              3. I've created a test csv file for this program which 5-6 tweets and the set of words that indicate racial slurs 
                  are in the program(in a list as 'x').

# Affinity
Assignment on degree of profanity on twitter file
First I've created a function(named as 'dop') which takes single sentence as input and checks for some racial slurs, and gives output for degree of profanity of that particular sentence
What that function does is : 
                      1. Convert the given sentence into a list of words.
                      2. Then using nested for-loop, it iterates through the list and compares each word with a given
                          list(set of words that indicates racial slurs)
                      3. Wherever a match is found, Count of 'degree of profanity' for that sentence is incremented by 1.
As provided in a question, we have to imagine a file full of tweets, and then find degree of profanity for each sentence in the file, I have created a dataframe while reading csv file using pandas library so that the given function can be applied to each cell or row in dataframe.

And finally we have the output for degree of profanity of each sentence.

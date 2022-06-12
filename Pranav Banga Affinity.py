import pandas as pd
#Making a function which takes single sentence as input and checks for some racial slurs, and gives output for degree of profanity of that sentence
def dop(sentence):
    cheklist=sentence.split()
    degree_of_profanity=0 #Count of single words that indicate racial slurs
    x=['black','nigga','peasant','jews','chinky','Hindu-Musalmaan'] # words which could possibly indicate racial slurs, can add as many as we want
    for i in range(0, len(cheklist)):
        for j in range(0, len(x)):   # Using nested for loop to iterate through each word in the sentence for each word in our racial slurs list
            if(x[j]==cheklist[i]):
                degree_of_profanity=degree_of_profanity+1  # Increasing the count whenever there is a match
    print(f'Degree of profanity in this sentence is {degree_of_profanity}.')

df = pd.read_csv(r"C:\Users\Pranav Banga\Pictures\twitter_assignment.csv") # Creating a dataframe for csv file, so that iteration for each row can be optimized

for i in range(df.shape[0]): # DataFrame stores the number of rows and columns as a tuple (number of rows, number of columns)
    row = str(df.iloc[i]) # Helps to select a particular cell and stores it in 'row'
    # print(row)
    dop(row)
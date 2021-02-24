import pandas as pd 
import markovify
import numpy as np

df = pd.read_csv("./insults.csv")
df.head()

insults = []

m = markovify.NewlineText('\n'.join(df["tweet"]))

for i in range(500):
    tweet = m.make_short_sentence(500, 20)
    insults.append(tweet)
    # print(tweet, '\n')

with open("AI_generated_insults.txt", "w") as f:
    for listitem in insults:
        f.write('%s\n\n' % listitem)
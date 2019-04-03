import markovify
import datetime
now = datetime.datetime.now()
import os
path = os.path.dirname(os.path.realpath(__file__))
text_a = open(path + "/data.txt").read()
generator = markovify.Text(text_a)
length_limit = 700
date = now.strftime("%Y-%m-%d")
print(date)
entry = generator.make_short_sentence(length_limit, 200)
print(entry)
file = open(path + "/" + date + '_journal_entry.txt', 'w')
file.write(str(entry))
file.close()


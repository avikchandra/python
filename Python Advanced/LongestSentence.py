import re

S = "We test coders. Give us a try?"
terminators=['.','?','!']
def splitSentences(text):
	sentences=re.split(terminators, text)


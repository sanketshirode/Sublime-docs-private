#Spellcheck.py
import language_check
from textblob import TextBlob
language_tool = language_check.LanguageTool('en-US')

#checks spelling mistakes
text_file = open("a.txt")
text = text_file.read()
textblob_text = TextBlob(text)
corrected_file = open("corrected_a.txt","w")
corrected_file.write(str(textblob_text.correct()))
corrected_file.close()

#print(textblob_text.correct())

#Checks grammar
text_file_grammar = open("corrected_a.txt")
text_grammar = text_file_grammar.read()
#print(text_grammar)
error_matches = language_tool.check(text_grammar)
print(len(error_matches))
print(error_matches)
grammar_corrected_file = open("corrected_grammar.txt","w")
grammar_corrected_file.write(language_check.correct(text_grammar,error_matches))
grammar_corrected_file.close()

print(language_check.correct(text_grammar,error_matches))


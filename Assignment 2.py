#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
text = 'Python Exercise,PHP exercises.'
print(re.sub("[ ,.]",":",text))


# In[2]:


import pandas as pd
data = {'SUMMARY': ['helloworld!', 'XXXX test','123four, five:; six...']}
df = pd.DataFrame(data)
df['SUMMARY']=df['SUMMARY'].str.replace('[^a-zA-Z\s]','', regex=True)
print(df)


# In[3]:


import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{4,}\b", text))


# In[4]:


import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{3,5}\b", text))


# In[5]:


import re
text = "ImportanceOfRegularExpressionInPython"
print(re.findall('[A-Z][^A-Z]*', text))


# In[6]:


import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))


# In[1]:


import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))


# In[1]:


import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)


# In[1]:


import re

text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

pattern = r"\b([A-Z][a-z]+) \d{1,2}(?:st|nd|rd|th)? \d{4}\b"

matches = re.findall(pattern, text)
print(matches)


# In[1]:


import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')


# In[2]:


import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))
	


# In[1]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


# In[2]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[3]:


import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# In[5]:


import re

def find_decimal_numbers(string):
  pattern = re.compile(r'\d+\.\d{1,2}')
  decimal_numbers = re.findall(pattern, string)
  return decimal_numbers
sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output = find_decimal_numbers(sample_text)
print(output)


# In[1]:


import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())
	


# In[2]:


import re

input_string = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

numeric_values = re.findall(r'\d+', input_string)
numeric_values = [int(value) for value in numeric_values]

max_value = max(numeric_values)

print(max_value)


# In[3]:


import re

def insert_spaces(text):
  # Use regular expression to find words starting with capital letters
  pattern = r'([A-Z][a-z]+)'
  # Replace the found words with the same word followed by a space
  result = re.sub(pattern, r' \1', text)
  # Remove any leading or trailing spaces
  result = result.strip()
  return result
sample_text = "RegularExpressionIsAnImportantTopicInPython"
output = insert_spaces(sample_text)
print(output)


# In[4]:


import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))


# In[5]:


import re

def remove_duplicates(sentence):
  pattern = r'\b(\w+)(\s+\1\b)+'
  result = re.sub(pattern, r'\1', sentence)
  return result

# Example usage
sentence = "Hello hello world world"
output = remove_duplicates(sentence)
print(output)


# In[1]:


import re

def extract_hashtags(text):
  hashtags = re.findall(r'#\w+', text)
  return hashtags

# Sample text
text = 'RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo'

# Extract hashtags
hashtags = extract_hashtags(text)

# Print the extracted hashtags
print(hashtags)


# In[1]:


import re

input_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

pattern = r"<U\+\w{4}>"
output_text = re.sub(pattern, "", input_text)

print(output_text)


# In[5]:


import re

def insert_spaces(text):
  # Use regular expression to find words starting with numbers
  pattern = r'(\d+)([A-Za-z]+)'
  result = re.sub(pattern, r'\1 \2', text)
  return result

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(sample_text)
print(output)


# In[6]:


import re

def remove_words(string):
  pattern = re.compile(r'\b\w{2,4}\b')
  modified_string = re.sub(pattern, '', string)
  return modified_string


sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
expected_output = "following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly."

result = remove_words(sample_text)
print(result == expected_output)  # True


# In[ ]:





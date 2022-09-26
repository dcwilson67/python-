text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
cnumb = text[pos : ]
numb = float(cnumb)
print(numb)

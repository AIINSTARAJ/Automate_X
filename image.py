import pywhatkit as kit
def text_to_write(txt):
    kit.text_to_handwriting(txt)

txt = input("Enter Text to Convert To Image: ")
text_to_write(txt)
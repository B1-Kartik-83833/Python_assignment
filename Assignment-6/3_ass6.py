def function():
    text = 'SHIFT'
    for i in range(0, 6):
        new_text = text[i:] + text[:i]
        print(new_text)


function()

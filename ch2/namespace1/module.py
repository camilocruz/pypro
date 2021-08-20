

'''
function in module
'''

GLOBAL_DIC = {
    "brand": "Ford", 
  "model": "Mustang", 
  "year": 1964
}

def function_text():
    print("I'm a  function in a module")
    model = GLOBAL_DIC['model']
    print("I can use my module global dic "+str(model))
    

def join_names(names):  # <1>
    name_string = ''

    for index, name in enumerate(names):
        if index > 0 and len(names) > 2:
            name_string += ','
        if index > 0:
            name_string += ' '
        if index == len(names) - 1 and len(names) > 1:
            name_string += 'and '
        name_string += name
    return name_string

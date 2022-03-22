import sys


def html_start():
    """
    Every HTML file has this.
    """
    return '''<html>\n<head>\n<title> \nDoc\n </title>\n</head> <body>'''

def html_end():
    return '''</body></html>'''


# Create the html file.

def create_doc(module_name, file_name):
    module_name = module_name.replace('.py', '')
    # Import the module.
    try:
        module = __import__(module_name)
    except Exception as error:
        return "Check the module name"

    with open(file_name, 'w') as mydoc:
        mydoc.write(html_start())
        mydoc.write('<h1>Module {0}:</h1>'.format(module_name))
        if module.__doc__:
            mydoc.write(module.__doc__)
        # Iterate over every callable method.
        for name, method in module.__dict__.items():
            if callable(method):    
                mydoc.write('<h1>Function {0}:</h1>'.format(name))
                if method.__doc__:
                    mydoc.write(method.__doc__)     
                if method.__annotations__:
                    mydoc.write('<h3>Annotations:</h3>'.format(name))  
                    for annotation in method.__annotations__:
                        mydoc.write('{0} <br>'.format(annotation))
        mydoc.write(html_end())


'''
Running examples
'''

if __name__ == '__main__':
    # Retreive the running arguments.
    if len(sys.argv) > 1:
        module_name = str(sys.argv[1])
        file_name = str(sys.argv[2])
        create_doc(module_name, file_name)
    else:
        create_doc('mymodule.py', 'my_doc.html')
        create_doc('module_example.py', 'my_doc_module_example.html')
        create_doc('mymodule2.py', 'my_doc2.html')
        create_doc('mymodule3.py', 'my_doc3.html')
    

# Run as a bash command:
# python3 exercise_1.py mymodule.py mydoc.html
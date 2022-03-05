import sys

# Retreive the running arguments.
module_name = str(sys.argv[1]).replace('.py', '')
file_name = str(sys.argv[2])
# Every HTML file has this.
html_start = '''<html>\n<head>\n<title> \nDoc\n \
</title>\n</head> <body>'''
html_end = '''</body></html>'''
# Import the module.

module = __import__(module_name)

# Create the html file.
with open(file_name, 'w') as mydoc:
    mydoc.write(html_start)
    # Iterate over every callable method.
    for name, method in module.__dict__.items():
        if callable(method):    
            mydoc.write('<h1>Function {0}:</h1>'.format(name))
            mydoc.write(method.__doc__)                         
    mydoc.write(html_end)


'''
Running examples
'''

# Run as a bash command:
# python3 exercise_1.py mymodule.py mydoc.html
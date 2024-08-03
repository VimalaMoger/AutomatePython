import traceback

try:
    raise Exception("Error occured ")
except:
    errorFile = open('hello.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('trace back error  added to hello.txt')
assert False, 'false result'

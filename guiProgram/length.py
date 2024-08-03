FILEPATH = "C:\\Users\\mvmgr\\Documents\\length.txt"

def get_data(filepath = FILEPATH):
    """
    read the file and return list of items
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as data:
        localData = data.readlines()
    return localData
def write_todos(todos_arg,file = FILEPATH):
    with open(file, 'w') as f1:
        f1.writelines(todos_arg)
if __name__ == "__main__":
    print(get_data())
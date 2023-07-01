def perform():
    file_name = "example.txt"
    file = open(file_name, "r")
    content = file.read()
    print(content)


perform()

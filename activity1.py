def add_target(filename, target):
    with open(filename, "a") as file:
        file.write(str(target) + "\n")
        file.close

def view_target(filename):
    file = open(filename, "r")
    data = file.readlines()
    file.close
    return data
    

todo_file = "listahan.txt"

add_target(todo_file, (input("Enter a Target Task: ")))
add_target(todo_file, (input("Next pa: ")))
add_target(todo_file, (input("Next pa jud hilas biya ka: ")))

print("\n My Daily Target Task:")
for target in view_target(todo_file):
    print("*" + target.strip())


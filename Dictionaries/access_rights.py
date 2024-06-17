''' The virus attacked the filesystem of the supercomputer and broke the control of access rights to the files. 
    For each file there is a known set of operations which may be applied to it:
        write W,
        read R,
        execute X.
    The first line contains the number N — the number of files contained in the filesystem. 
    The following N lines contain the file names and allowed operations with them, separated by spaces. 
    The next line contains an integer M — the number of operations to the files. In the last M lines specify 
    the operations that are requested for files. One file can be requested many times.

    You need to recover the control over the access rights to the files. 
    For each request your program should return OK if the requested operation is valid or Access denied if the operation is invalid. '''


def check_access(file_permissions, operation, file_name):
    if operation in file_permissions[file_name]:
        return "OK"
    else:
        return "Access denied"

# Input number of files and their permissions
n = int(input())
file_permissions = {}
for _ in range(n):
    input_data = input().split()
    file_name = input_data[0]
    permissions = set(input_data[1:])
    file_permissions[file_name] = permissions

# Input number of operations and process them
m = int(input())
for _ in range(m):
    operation, file_name = input().split()
    # Convert operation to permission
    permission = {'read': 'R', 'write': 'W', 'execute': 'X'}[operation]
    print(check_access(file_permissions, permission, file_name))

def postorder(node):
    if tree_list[node][1].isdecimal():
        return tree_list[node][1]

    else:
        left = postorder(int(tree_list[node][2]))
        right = postorder(int(tree_list[node][3]))
        poly = eval(left + tree_list[node][1] + right)
        return str(int(poly))

for t in range(1, 11):
    N = int(input())
    tree_list = [0]
    for i in range(1, N+1):
        tree_list.append(input().split())
    result = postorder(1)
    print(f'#{t} {int(result)}')


# def postorder(node):
#     if tree_list[node][1].isdecimal(): return int(tree_list[node][1])
#     left = postorder(int(tree_list[node][2]))
#     right = postorder(int(tree_list[node][3]))
#
#     if tree_list[node][1] == '+':   return left + right
#     elif tree_list[node][1] == '-': return left - right
#     elif tree_list[node][1] == '*': return left * right
#     else:   return left // right
#
# for t in range(1, 11):
#     N = int(input())
#     tree_list = [0]
#     for i in range(1, N+1):
#         tree_list.append(input().split())
#     print(f'#{t} {postorder(1)}')
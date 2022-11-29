vertices_dict = {}

vertices_list = input().split()

for vertex in vertices_list:
    vertices_dict[vertex] = []

links_num = int(input())

for i in range(links_num):
    link_pair = [x for x in input().split()]
    vertices_dict[link_pair[0]].append(link_pair[1])
    vertices_dict[link_pair[1]].append(link_pair[0])

start_pos_list = input().split()
vertices_set = set()

for start_pos in start_pos_list:
    vertices_set.update(vertices_dict[start_pos] + [start_pos])

vertices_list = [int(x) for x in vertices_set]
vertices_list.sort()

for vertex in vertices_list:
    print(vertex, end=' ')

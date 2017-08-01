#!/usr/bin/python

def mystery(sorted_array, left_boundary, right_boundary):
    if left_boundary > right_boundary:
        return -1
    medium = int(left_boundary + right_boundary)
    if sorted_array[medium] == medium:
        return medium
    elif sorted_array[medium] < medium:
        return mystery(sorted_array, medium+1, right_boundary)
    else:
        return mystery(sorted_array, left_boundary, medium-1)

if __name__ == "__main__":
    print mystery([-2, 0, 1, 3, 7, 12, 15], 0, 6)
    print mystery([0,1,2,3,4,5,6,7,8,9],0,9)
    print mystery([0,1,2,3,29,9,2],0,6)

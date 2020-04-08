'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
 You are given the scores. Store them in a list and find the score of the runner-up.
'''

if __name__ == '__main__':
    n = int(input())
    arr_list = list(map(int, input().split()))
    z = max(arr_list)
    while max(arr_list) == z:
        arr_list.remove(max(arr_list))
    print(max(arr_list))
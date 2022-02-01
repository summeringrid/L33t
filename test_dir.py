dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
curr = (0, 0)
for k in range(4): # 搜索四个方向
    nx = curr[0] + dx[k]
    ny = curr[1] + dy[k]

    print('nx=', nx,'ny=', ny)

DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]
curr_r, curr_c = 0,0
for delta_r, delta_c in DIRECTIONS:
    next_r, next_c = curr_r + delta_r, curr_c + delta_c
    print('next_r', next_r, 'next_c', next_c)
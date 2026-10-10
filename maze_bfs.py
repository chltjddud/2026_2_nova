maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

rows = len(maze)
cols = len(maze[0])

queue = [[0, 0, 1]]
visited = []
for r in range(rows):
    visited.append([False] * cols)

visited[0][0] = True
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = -1
while queue:
    curr = queue.pop(0)
    x = curr[0]
    y = curr[1]
    dist = curr[2]
    
    if x == rows - 1 and y == cols - 1:
        result = dist
        break
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < rows and 0 <= ny < cols:
            if maze[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny, dist + 1])

print(result)

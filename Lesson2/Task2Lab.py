#Создайте функцию, которая принимает двумерный массив (лабиринт) и начальную и конечную точки. 
#Функция должна возвращать путь от начальной до конечной точки или сообщение, что путь невозможеy/ 

from collections import deque

def find_path(maze, start, end):
    rows=len(maze)
    cols=len(maze[0])

    visited= [[False]*cols for_range(rows)]

prev = [[None]*cols for_in range(rows)]

offsets=[(1,0), (-1,0), (0,1), (0,-1)]
queue=deque([start])

visited[start[0]][start[1]] = True

while queue:
    x, y = queue.popleft()
    if (x,y)==end: 
        path =[]
        while (x, y)!=start:
            path.append((x, y))
            x, y = prev[x][y]
        path.append(start)
        path.reverse()
        return path
    
for dx, dy in offsets:
    nx, ny = x+dx, y + dy

    if 0 <+ nx < rows and 0 <= ny < cols and maze[nx][ny] == and not visited[nx][ny]:
        queue.append((nx,ny))
        visited[nx][ny] = True
        prev[nx][ny] = (x,y)

return None

maze = [
    ['0' , ' 1' , ' 0' , ' 0' , ' 0' ]
    ['0' , ' 1' , ' 0' , ' 1' , ' 0' ]
    ['0' , ' 0' , ' 0' , ' 1' , ' 0' ]
    ['0' , ' 1' , ' 0' , ' 0' , ' 0' ]
    ['0' , ' 0' , ' 0' , ' 0' , ' 0' ]

]

start = (0, 0)
end = (4, 4)

path = find_path(maze, start, end)

if path:
    print("Путь найден:")

    for x, y in path:
        print(f"({x}, {y})")

else:
    print("Путь не наден")
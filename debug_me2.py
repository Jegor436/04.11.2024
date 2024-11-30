import heapq
import random

# Funkcija režģa ģenerēšanai ar nejaušiem svaru
def generate_grid(rows, cols):
    grid = [[random.randint(1, 10) 
 for _ in range(cols)] for _ in 
 range(rows)]
    return grid

# Dijkstra algoritms režģim
def dijkstra_grid(grid, start):
    rows, cols = len(grid),
    len(grid[0])

  # Kustību virzieni (augšup, lejup, pa kreisi, pa labi)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  # Inicializējam attālumus līdz visām šūnām kā bezgalību
    distances = [[float('inf')] * cols for _ in 
 range(rows)]
    distances[start[0]][start[1]] = 0

   # Izmantojam prioritātes rindu (min-heap)
    priority_queue = [(0, start[0], start[1])] 
   # (attālums, x, y)
    while priority_queue:
        current_distance, x, y = heapq.heappop(priority_queue)

        # Ja pašreizējais attālums ir lielāks nekā jau atrastais, izlaižam
        if current_distance > distances[x][y]: 
            continue

        # Pārbaudām visus kaimiņu šūnas
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Ja kaimiņa šūna ir režģa robežās
            if 0 <= nx < rows and 0 <= ny < cols:
                new_distance = current_distance + grid[nx][ny]

                # Ja atrasts īsāks attālums
                if new_distance < distances[nx][ny]:
                    distances[nx][ny] = new_distance
                    heapq.heappush(priority_queue, (new_distance, nx, ny))
    return distances

# Piemērs izmantošanai:
if __name__ == "__main__":
    # Režģa izmērs
    rows, cols = 100, 100

    # Ģenerējam režģi ar nejaušiem svariem no 1 līdz 10
    grid = generate_grid(rows, cols)

    # Sākuma šūna (piemēram, kreisais augšējais stūris)
    start = (0, 0)

    # Uzsākam Dijkstra algoritmu
    distances = dijkstra_grid(grid, start)

    # Izdrukājam īsākos attālumus līdz visām šūnām pirmajā rindā (piemērs)
    for col in range(cols):
        print(f"Attālums līdz šūnai (0, {col}): 
{distances[0][col]}")
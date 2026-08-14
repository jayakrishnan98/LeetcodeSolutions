class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q.append((sr, sc))
        image[sr][sc] = color
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (
                    0 <= r < ROWS
                    and 0 <= c < COLS
                    and image[r][c] == original_color
                ):
                    image[r][c] = color
                    q.append((r, c))
        return image
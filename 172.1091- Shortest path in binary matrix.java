import java.util.ArrayDeque;

class Tuple{
    public int i;
    public int j;

    public Tuple(int i, int j){
        this.i = i;
        this.j = j;
    }
}

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int res = 0;
        ArrayDeque<Tuple> deque = new ArrayDeque<>();
        deque.addLast(new Tuple(0, 0));

        while(!deque.isEmpty()){
            res += 1;
            int count = 0;
            int size = deque.size();

            while (count < size){
                count += 1;
                Tuple tup = deque.removeFirst();
                int y = tup.i;
                int x = tup.j;
                if ((y < 0) || (y >= grid.length) || (x < 0) || (x >= grid[0].length)){
                    continue;
                }
                if (grid[y][x] != 0){
                    continue;
                }
                if (y == grid.length - 1 && x == grid[0].length - 1){
                    return res;
                }
                grid[y][x] = 1;

                for (int i = -1; i <= 1; i += 1){
                    for (int j = -1; j <= 1; j += 1){
                        deque.addLast(new Tuple(y + i, x + j));
                    }
                }
            }
        }
        return -1;
    }
}
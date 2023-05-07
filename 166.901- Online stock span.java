import java.util.Stack;

class StockSpanner {
    Stack<Integer> stack = new Stack<>();
    Stack<Integer> spans = new Stack<>();

    public StockSpanner() {
        
    }
    
    public int next(int price) {
        int count = 1;
        while (!stack.isEmpty() && stack.peek() <= price){
            count += spans.peek();
            stack.pop();
            spans.pop();
        }
        stack.push(price);
        spans.push(count);
        return count;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */
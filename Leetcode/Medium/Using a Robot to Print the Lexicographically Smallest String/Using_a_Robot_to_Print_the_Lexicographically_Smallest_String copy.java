import java.util.*;

class Solution {
    public static String robotWithString(String s) {
        int n = s.length();
        char[] minSuffix = new char[n];
        minSuffix[n - 1] = s.charAt(n - 1);

        for (int i = n - 2; i >= 0; i--) {
            minSuffix[i] = (char) Math.min(s.charAt(i), minSuffix[i + 1]);
        }

        Deque<Character> stack = new ArrayDeque<>();
        StringBuilder output = new StringBuilder();

        for (int i = 0; i < n; i++) {
            stack.push(s.charAt(i));

            while (!stack.isEmpty() && 
                   (i == n - 1 || stack.peek() <= minSuffix[i + 1])) {
                output.append(stack.pop());
            }
        }

        while (!stack.isEmpty()) {
            output.append(stack.pop());
        }

        return output.toString();
    }
}
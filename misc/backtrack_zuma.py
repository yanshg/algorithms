'''
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty

'''

# Backtrack
from collections import Counter

def get_minimal_steps_to_remove_all_balls(balls, hands):
    if not balls:
        return 0
    
    min_inserted = float('inf')

    def backtrack(balls, hand_counts, inserted):
        nonlocal min_inserted
         
        if not balls:
            min_inserted = min(inserted, min_inserted)
            return 

        i, j = 0, 0
        n = len(balls)
        while i < n:
            c = balls[i]
            j = i
            while j < n and balls[j] == c:
                j += 1
            
            need = 3 - (j - i)
            if need <= 0 or hand_counts[c] >= need:
                # we can collapse the substring containing c from i to j.
                new_balls = balls[:i] + balls[j:]
                if need > 0:
                    backtrack(new_balls, hand_counts - Counter({c:need}), inserted + need)
                else:
                    backtrack(new_balls, hand_counts, inserted)

            i = j

    backtrack(balls, Counter(hands), 0)
    return min_inserted if min_inserted != float('inf') else -1

balls = "WRRBBW"
hands = "RB"
assert get_minimal_steps_to_remove_all_balls(balls, hands) == -1

balls = "WWRRBBWW"
hands = "WRBRW"
assert get_minimal_steps_to_remove_all_balls(balls, hands) == 2

balls = "G"
hands = "GGG"
assert get_minimal_steps_to_remove_all_balls(balls, hands) == 2


balls = "GGGGGG"
hands = "GGG"
assert get_minimal_steps_to_remove_all_balls(balls, hands) == 0

balls = "RBYYBBRRB"
hands = "YRBGB"
assert get_minimal_steps_to_remove_all_balls(balls, hands) == 3

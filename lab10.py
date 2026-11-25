# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
     # Outline:
    # 1. Create an empty list `stack` to hold integer operands.
    # 2. Loop through each `token` in `tokens`:
    #    - If `token` is one of "+", "-", "*", "/":
    #      a. Pop the top two numbers from `stack` (`b` first, then `a`).
    #      b. Apply the operator (`a + b`, `a - b`, `a * b`, or `int(a / b)`).
    #      c. Push the result back onto `stack`.
    #    - Otherwise, convert `token` to an `int` and push it onto `stack`.
    # 3. Return the single remaining number in `stack`.

    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token in operators:
            b = stack.pop()  # Right operand (popped first)
            a = stack.pop()  # Left operand (popped second)

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  # Truncates toward zero
        else:
            stack.append(int(token))

    return stack[0]


def decode_string(s):
     # Outline:
    # 1. Initialize an empty `stack`, `curr_str = ""`, and `curr_num = 0`.
    # 2. Loop through each character `ch` in `s`:
    #    - If `ch` is a digit, update `curr_num` (handles multi-digit numbers like 12[a]).
    #    - Else if `ch == "["`, push `(curr_str, curr_num)` onto `stack`, then reset both.
    #    - Else if `ch == "]"`, pop `(prev_str, k)` from `stack` and set `curr_str = prev_str + curr_str * k`.
    #    - Otherwise (a letter), append `ch` to `curr_str`.
    # 3. Return `curr_str`.

    stack = []
    curr_str = ""
    curr_num = 0

    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        elif ch == "[":
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif ch == "]":
            prev_str, k = stack.pop()
            curr_str = prev_str + (curr_str * k)
        else:
            curr_str += ch

    return curr_str


def daily_temperatures(temps):
     # Outline:
    # 1. Create `result` filled with 0s of the same length as `temps`, and an empty `stack`.
    # 2. Loop through `(i, temp)` in `enumerate(temps)`:
    #    - While `stack` is not empty and `temp > temps[stack[-1]]`:
    #      a. Pop `prev_day` from `stack`.
    #      b. Set `result[prev_day] = i - prev_day`.
    #    - Push current index `i` onto `stack`.
    # 3. Return `result`.

    result = [0] * len(temps)
    stack = []  # Stores indices of days waiting for a warmer temperature

    for i, temp in enumerate(temps):
        while stack and temp > temps[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day
        stack.append(i)

    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()

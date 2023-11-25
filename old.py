from math import inf

TESTCASE_SIZE = 1000
IS_PRINT = True


def exam_solution():
    a = [[0, 0, '', 0], [1, 1, '', 1], [2, 2, '', 2]]
    for i in range(3, TESTCASE_SIZE):
        best_addition = inf
        best_multiply = inf
        addition_source = 0
        mult_source = 0
        for j in range(1, i):
            current_addition = a[j][0] + a[i - j][0]
            if current_addition < best_addition:
                best_addition = current_addition
                addition_source = j
            if i % j == 0 and j != 1:
                current_mult = a[j][0] + a[int(i / j)][0]
                if current_mult < best_multiply:
                    best_multiply = current_mult
                    mult_source = j

        if best_multiply < best_addition:
            a.append([best_multiply, mult_source, 'm', i])
        else:
            a.append([best_addition, addition_source, 'a', i])

    return a


def my_solution():
    a = [[0, 0, '', 0], [1, 1, '', 1], [2, 2, '', 2]]
    for i in range(3, TESTCASE_SIZE):
        best_addition = a[i - 1][0] + 1
        best_multiply = inf
        addition_source = 1
        mult_source = 0
        for j in range(2, i):
            if i % j == 0:
                current_mult = a[j][0] + a[int(i / j)][0]
                if current_mult < best_multiply:
                    best_multiply = current_mult
                    mult_source = j

        if best_multiply >= best_addition:
            a.append([best_addition, addition_source, 'a', i])
        else:
            a.append([best_multiply, mult_source, 'm', i])

    return a


if __name__ == "__main__":
    '''
    Exam recurrence:
    dp[i] = min(for all j+k=i, dp[i]+dp[k], 
                for all j*k=i, dp[i]+dp[k])

    My recurrence:
    dp[i] = min(dp[i-1]+1, 
                for all j*k=i, dp[i]+dp[k])

    Explanation of output:
    a is the list where index 0 to 2 are hardcoded, each element in list are represent as follows:

        a[i][0]:
            The dynamic programming table, the number of 1s.

        a[i][1] and a[i][2]:
            The source and operation to form the number.
            See example below

        a[i][3]:
            Index of the number for visualization purpose.

        Example:
            [9,1,'a',19] means number 19 requires 9 1s, with a calculation from addition of 1 and 18.
            [9,2,'m',20] means number 20 requires 9 1s, with a calculation from multiplying 2 and 10.
    '''
    es = exam_solution()
    ms = my_solution()

    if IS_PRINT:
        print(es)
        print(ms)

    # verifies if two solutions have the same result for dp array
    for c in range(0, TESTCASE_SIZE):
        if es[c][0] != ms[c][0]:
            print("Unmatched for number %i" % c)

    print("done")

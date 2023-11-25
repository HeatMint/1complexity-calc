from math import inf
from math import isqrt


# ---------------tools
def es_next(dp, result):
    length = len(dp)

    result[3] = length

    best_addition = inf
    best_multiply = inf
    addition_source = 0
    mult_source = 0
    for j in range(1, length // 2 + 1):
        current_addition = dp[j] + dp[length - j]
        if current_addition <= best_addition:
            best_addition = current_addition
            addition_source = j

    for j in range(2, isqrt(length) + 1):
        if length % j == 0:
            current_mult = dp[j] + dp[int(length / j)]
            if current_mult < best_multiply:
                best_multiply = current_mult
                mult_source = j

    if best_multiply < best_addition:
        result[0] = best_multiply
        result[1] = 1
        result[2] = mult_source
        return best_multiply
    else:
        result[0] = best_addition
        result[1] = 0
        result[2] = addition_source
        return best_addition


def ms_next(dp, result):
    length = len(dp)

    result[3] = length

    best_addition = inf
    best_multiply = inf
    addition_source = 1
    mult_source = 0
    best_addition = dp[length - 1] + 1

    for j in range(2, isqrt(length) + 1):
        if length % j == 0:
            current_mult = dp[j] + dp[int(length / j)]
            if current_mult < best_multiply:
                best_multiply = current_mult
                mult_source = j

    if best_multiply < best_addition:
        result[0] = best_multiply
        result[1] = 1
        result[2] = mult_source
        return best_multiply
    else:
        result[0] = best_addition
        result[1] = 0
        result[2] = addition_source
        return best_addition


# ---------------initialize

# begin reading data
data_file = open("data.txt", "r")
dp = []
for line in data_file:
    int_line = int(line)
    dp.append(int_line)
data_file.close()

display_file = open("display.txt", "r")
display_best = int(display_file.readline())
display_file.close()

# end reading data

# ---------------endless loop
tmp = 0
while (True):
    tmp += 1
    result_es_data = [0, 0, 0, 0]
    result_ms_data = [0, 0, 0, 0]
    # result_data in the format (1complexity, add(0)/mult(1), source, index)
    ms_next_result = ms_next(dp, result_ms_data)
    es_next_result = es_next(dp, result_es_data)
    if ms_next_result == es_next_result:

        if result_es_data[1] == 0:
            if result_es_data[2] != 1:
                noticeable = open("noticeable.txt", "a")
                noticeable.write("On number:" + str(result_es_data[3]) + \
                                 " is an addition from index " + str(result_es_data[2]) + "\n")
                noticeable.close()

                if result_es_data[2] > display_best:
                    display_best = result_es_data[2]
                    display_file = open("display.txt", "w")
                    display_file.write(str(result_es_data[2]) + "\n")
                    display_file.write(str(result_es_data[0]) + "\n")
                    display_file.write(str(result_es_data[1]) + "\n")
                    display_file.write(str(result_es_data[2]) + "\n")
                    display_file.write(str(result_es_data[3]) + "\n")
                    display_file.close()

        data_file = open("data.txt", "a")
        data_file.write(str(es_next_result) + "\n")
        data_file.close()
        dp.append(es_next_result)

        index_file = open("index.txt", "w")
        index_file.write(str(result_es_data[3])+"\n")
        index_file.close()

        record_file = open("record.txt", "a")
        record_file.write(str(result_es_data) + "\n")
        record_file.close()

    else:
        noticeable = open("noticeable.txt", "a")
        noticeable.write("First differentiation found on number:\n")
        noticeable.write(str(result_ms_data[3]) + "\n")
        noticeable.write("With data(es first, ms next):\n")
        noticeable.write(str(result_es_data) + "\n")
        noticeable.write(str(result_ms_data) + "\n")
        noticeable.close()
        break

from collections import Counter


def convert_hex_binary(hex_text):
    binary_result = ''
    for character in hex_text:
        binary_result += "{0:04b}".format(int(character, 16))
    return binary_result


def monobit_test(bin_string):
    number_of_ones = 0
    for bit in bin_string:
        if bit == '1':
            number_of_ones += 1
    if (number_of_ones > 9654) and (number_of_ones < 10346):
        return True
    else:
        return False


def poker_test(bin_string):
    contiguous_segments = [bin_string[i:i+4] for i in range(0, len(bin_string), 4)]
    contador = Counter(contiguous_segments)

    f_i = 0
    for string, quantidade in contador.items():
        f_i += quantidade*quantidade
    x = ((16/5000) * f_i) - 5000

    if (x > 1.03) and (x < 57.4):
        return True
    else:
        return False


def runs_test(bin_string):
    count = 1
    repetitions = []
    counter_0 = [0, 0, 0, 0, 0, 0]
    counter_1 = [0, 0, 0, 0, 0, 0]
    if len(bin_string) > 1:
        for i in range(1, len(bin_string)):
            if bin_string[i - 1] == bin_string[i]:
                count += 1
            else:
                repetitions.append([bin_string[i - 1], count])
                count = 1
        repetitions.append([bin_string[i], count])

    for rep in repetitions:
        if rep[0] == '0':
            if rep[1] >= 6:
                counter_0[5] += 1
            else:
                counter_0[rep[1]-1] += 1
        if rep[0] == '1':
            if rep[1] >= 6:
                counter_1[5] += 1
            else:
                counter_1[rep[1]-1] += 1

    zero_ok = False
    one_ok = False
    if (counter_0[0] > 2267) and (counter_0[0] < 2733) and (counter_0[1] > 1079) and (counter_0[1] < 1421) and \
        (counter_0[2] > 502) and (counter_0[2] < 748) and (counter_0[3] > 223) and (counter_0[3] < 402) and \
        (counter_0[4] > 90) and (counter_0[4] < 223) and (counter_0[5] > 90) and (counter_0[5] < 223):
        zero_ok = True

    if (counter_1[0] > 2267) and (counter_1[0] < 2733) and (counter_1[1] > 1079) and (counter_1[1] < 1421) and \
        (counter_1[2] > 502) and (counter_1[2] < 748) and (counter_1[3] > 223) and (counter_1[3] < 402) and \
        (counter_1[4] > 90) and (counter_1[4] < 223) and (counter_1[5] > 90) and (counter_1[5] < 223):
        one_ok = True

    if zero_ok and one_ok:
        return True
    else:
        return False


def long_run(bin_string):
    count = 1
    if len(bin_string) > 1:
        for i in range(1, len(bin_string)):
            if bin_string[i - 1] == bin_string[i]:
                count += 1
            else:
                if count >= 34:
                    return False
                count = 1
    return True


if __name__ == '__main__':
    chaves = open('chaves.txt', 'r')
    chaves_filtradas = []
    chaves_binarias = []

    for chave in chaves:
        temp = chave[1:]
        temp = temp[:-2]
        a = len(temp)
        chaves_filtradas.append(temp)
        chaves_binarias.append(convert_hex_binary(temp))

    binary_number = 1
    for binary in chaves_binarias:
        answer_monobit = monobit_test(binary)
        answer_poker = poker_test(binary)
        answer_runs = runs_test(binary)
        answer_long = long_run(binary)
        print('Chave binária ' + str(binary_number))
        if answer_monobit and answer_poker and answer_runs and answer_long:
            print("APROVADO!")
        else:
            print("REPROVADO! Resultados: Monobit Test: " + str(answer_monobit) + ". Poker Test: " +
                  str(answer_poker) + ". Runs Test: " + str(answer_runs) + ". Long Run Test: " + str(answer_long))
        binary_number += 1



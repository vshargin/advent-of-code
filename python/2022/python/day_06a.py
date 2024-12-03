with open("inputs/day_06.txt") as input_file:
    signal = input_file.read()

for i in range(len(signal) - 4):
    test_string = signal[i:i + 4]
    if len(set(test_string)) == len(test_string):
        print(i + 4)
        break

from threading import Timer

text = ["Apple", "Adam", "word", "pitch", "Hello", "okay!", "brother", "hall", "BELL", "Autopilot", "Python", "river",
        "Code", "Savage", "don't", "medicine", "Tiger", "win", "goal", "Strategy", "bring", "grammar", "division",
        "alphabet", "thread", "Mouse", "Microsoft", "to-do", "David", "Pink", "list", "singing", "Joy", "Ray", "miss",
        "world-record"]
print("Typing Tester \nWrite the words given identically \nTime: 10 seconds")

h = 0


def b():
    global h
    h = 1
    print("\nTimes Up! Press Enter to view scores")


def write():
    count1 = 0
    count2 = 0
    count3 = 0
    i = 0
    t = Timer(10, b)
    t.start()
    while h != 1 and i < len(text):
        print("Word: ", text[i])
        word = input("Write: ")
        if word == text[i]:
            count1 += 1
        elif word == "":
            count3 += 1
        else:
            count2 += 1
        i += 1

    if h == 1:
        if count2 + count1 > 0 and count3 > 0:
            acc = count1 / (count1 + count2 + count3)
        else:
            acc = count1 / (count3 + count1)
        print("Scores")
        print("Correct words: ", count1)
        print("Incorrect words: ", count2)
        print("Accuracy: ", acc)


def start():
    begin = input("Press Y to start: ").upper()
    if begin == "Y":
        print("Your time starts now!!!")
        write()
    else:
        print("Press Y")
        start()


# Final Function Call
start()

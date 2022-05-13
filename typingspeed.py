from time import time

# input wala nirawdya thawaya gananaya kirima
def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in(0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors +1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1]== words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

# now to calculate type karana word wala speed eka
def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time

    return speed
# calculate the total elapsed time
def elapsedtime(stime,etime):
    time = etime - stime
    return time

if __name__ == '__main__':
    prompt = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics"
    print("type this :-",prompt," "
          )

    input("Press Enter when you are ready to check your speed!!!")

    # recording time for input
    stime = time()
    inprompt = input()
    etime = time()

    # collect all the information returned by the functions
    time = round(elapsedtime(stime,etime),2)
    speed = speed(inprompt,stime,etime)
    errors = tperror(prompt)

    #print all the required data to see result
    print("Total time elapsed :", time, "seconds")
    print("Your Average Typing speed was", speed, "words per minute (w/m")
    print("with the Total of ", errors, "errors")


























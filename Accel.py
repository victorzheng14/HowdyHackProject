import speech_recognition as sr

r = sr.Recognizer() #recognize audio

with sr.Microphone() as source: #initialize source to sr.Microphone()

    print('What math function would you like to do?')
    audio = r.listen(source) #listen to source and save it in audio

    try:
        text = r.recognize_google(audio)
        print('------------------You said: {}'.format(text))
    except:
        print('Sorry could not recognize your voice')


a = sr.Recognizer()
counter = 0;
sum = 0;
diff = 0;
product = 1;
avg = 0;
keepGoing = 'Yes'


with sr.Microphone() as source:

    # addition
    if(text=='addition' or text == 'add' or text == 'plus'):
        print('How many numbers would you like to add?')
        audio = a.listen(source)
        text = a.recognize_google(audio)
        print('------------------You said: {}'.format(text))

        t1 = str(text)
        numQuantity = int(t1)
        while(counter < numQuantity):
            print('Pick a number: ')
            audio = a.listen(source)
            text = a.recognize_google(audio)
            print('------------------You said: {}'.format(text))
            t2 = str(text)
            num = int(t2)
            sum = sum + num;
            counter = counter + 1;
        print('The total sum: ', sum)

    # subtraction
    elif(text=='subtraction' or text=='subtract' or text=='minus'):
        print('How many numbers would you like to subtract?')
        audio = a.listen(source)
        text = a.recognize_google(audio)
        print('------------------You said: {}'.format(text))

        t1 = str(text)
        numQuantity = int(t1)
        difference = 0;
        while (counter < numQuantity):
            print('Pick a number: ')
            audio = a.listen(source)
            text = a.recognize_google(audio)
            print('------------------You said: {}'.format(text))
            t2 = str(text)
            num = int(t2)

            if(counter==0):
                diff = num
            else:
                diff = diff - num;

            counter = counter + 1;

        print('The total difference: ', diff)

    # multiplication
    elif (text == 'multiplication' or text == 'multiply' or text=='times'):
        print('How many numbers would you like to multiply?')
        audio = a.listen(source)
        text = a.recognize_google(audio)
        print('------------------You said: {}'.format(text))

        t1 = str(text)
        numQuantity = int(t1)
        while (counter < numQuantity):
            print('Pick a number: ')
            audio = a.listen(source)
            text = a.recognize_google(audio)
            print('------------------You said: {}'.format(text))
            t2 = str(text)
            num = int(t2)
            product = product * num;
            counter = counter + 1;
        print('The total product: ', product)

    # division
    elif (text == 'division' or text == 'divide'):
        print('You can only divide 2 numbers at a time. Pick the numerator.')
        audio = a.listen(source)
        text = a.recognize_google(audio)
        print('------------------You said: {}'.format(text))

        fnum = str(text)
        numerator = int(fnum)


        print('Pick a demoninator: ')
        audio = a.listen(source)
        text = a.recognize_google(audio)
        print('------------------You said: {}'.format(text))
        dnum = str(text)
        denominator = int(dnum)
        ans = numerator/denominator
        print('The quotient: ', ans)

    # average
    elif (text == 'average'):
        print('How many numbers would you like to average?')
        audio = a.listen(source)
        text = a.recognize_google(audio)
        print('------------------You said: {}'.format(text))

        t1 = str(text)
        numQuantity = int(t1)
        while (counter < numQuantity):
            print('Pick a number: ')
            audio = a.listen(source)
            text = a.recognize_google(audio)
            print('------------------You said: {}'.format(text))
            t2 = str(text)
            num = int(t2)
            avg = avg + num
            counter = counter + 1;
        average = avg/numQuantity
        print('The average of the numbers is: ', average)

    # multiple functions
    elif (text == 'more than one'):
        while(keepGoing == 'Yes'):
            print('What would you like?')
            audio = a.listen(source)
            text = a.recognize_google(audio)
            print('------------------You said: {}'.format(text))

            # Addition - more than one
            if(text=='addition' or text=='add'):
                print('Pick a number')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                print('------------------You said: {}'.format(text))
                t2 = str(text)
                total = int(t2)

                print('Pick another number')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                print('------------------You said: {}'.format(text))
                t2 = str(text)
                total = total + int(t2)
                print('~~~~~~~Your current total is ', total)


                print('Would you like to keep going? Say yes or no')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                t2 = str(text)
                if(t2 == 'Yes' or t2 == 'yes'):
                    keepGoing = 'Yes'
                if(t2 == 'No' or t2 == 'no'):
                    keepGoing = 'No'

            # Subtraction - more than one
            elif(text == 'subtraction' or text == 'subtract' or text == 'minus'):
                print('Pick a number')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                print('------------------You said: {}'.format(text))
                t2 = str(text)
                total = int(t2)

                print('Pick another number to be subtracted from the number you just chose')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                print('------------------You said: {}'.format(text))
                t2 = str(text)
                total = total - int(t2)
                print('~~~~~~~Your current total is ', total)

                print('Would you like to keep going? Say yes or no')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                print('------------------You said: {}'.format(text))

                if (t2 == 'Yes' or t2 == 'yes'):
                    keepGoing = 'Yes'
                if (t2=='No' or t2 == 'no'):
                    keepGoing = 'No'

            # Multiplication - more than one
            elif (text == 'multiplication' or text == 'multiply' or text == 'times'):
                print('Pick a number')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                print('------------------You said: {}'.format(text))
                t2 = str(text)
                num1 = int(t2)

                print('Pick another number')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                print('------------------You said: {}'.format(text))
                num2 = str(text)
                total = num1 * int(num2)
                print('~~~~~~~Your current total is ', total)

                print('Would you like to keep going? Say yes or no')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                t2 = str(text)
                if (t2 == 'Yes' or t2 == 'yes'):
                    keepGoing = 'Yes'
                if (t2 == 'No' or t2 == 'no'):
                    keepGoing = 'No'

            # Division - more than one
            elif (text == 'division' or text == 'divide'):
                print('Pick a number')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                print('------------------You said: {}'.format(text))
                t2 = str(text)
                num1 = int(t2)

                print('Pick another number')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                print('------------------You said: {}'.format(text))
                num2 = str(text)
                total = num1 / int(num2)
                print('~~~~~~~Your current total is ', total)

                print('Would you like to keep going? Say yes or no')
                audio = a.listen(source)
                text = a.recognize_google(audio)
                t2 = str(text)
                if (t2 == 'Yes' or t2 == 'yes'):
                    keepGoing = 'Yes'
                if (t2 == 'No' or t2 == 'no' or t2=='stop'):
                    keepGoing = 'No'


        print('---------------------------Your FINAL total is ', total)

    elif(text == 'end task'):
        print('Thank you, see you later!')

    else:
        print('That is not a function')





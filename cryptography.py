alpha='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
ALPHA= alpha.upper()

def swap (eng,ch,data,rot) :
    for index in range(len(alpha)) :
        if eng[index] is ch :    
            letter = eng[index+rot]
            data=data+letter
            break
    return data
            
print ('boooot .....')
print ('CEASER is here .....\n')



while True :
    print ('\nWhat do you want sir ?')
    print ('1) encrypt تشفير')
    print ('2) decrypt فك الشفره')
    while True :
        try :
            sel =int(input('Enter the number of your choise :)   '))
        except:
            print('\nWrong input! :(\nmust enter a number')
            continue
        if sel != 2 and sel !=1 :
            print('\nWrong input! :(\nmust enter a number (1 or 2)')
            continue
        break

    data=input('Enter string :)  ')
    while True :
        try :
            rot =int(input('Enter rot :)   '))
        except:
            print('\nWrong input! :(\nmust enter a number')
            continue
        if rot>25 or rot<1 :
            print('\nWrong input! :(\nmust enter a number (from 1 to 25)')
            continue
        break

    if sel ==1 :
        ceaser =''  
        for char in data :
            if char in alpha :
                ceaser = swap (alpha,char,ceaser,rot)
            elif char in ALPHA :
                ceaser = swap (ALPHA,char,ceaser,rot)
            else :
                ceaser=ceaser+char
        print('the encrypted string is',ceaser)

    elif sel ==2:
        ceaser ='' 
        for char in data :
            if char in alpha :
                ceaser = swap (alpha,char,ceaser,(26-rot))
            elif char in ALPHA :
                ceaser = swap (ALPHA,char,ceaser,(26-rot))
            else :
                ceaser=ceaser+char
        print('the decrypted string is',ceaser)
        
    q = input('Enter q to quit , any key to continue  ')
    if q=='q' : break

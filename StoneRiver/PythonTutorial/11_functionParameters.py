

print("\n11:Function Parameter examples")
print("==============================\n")

## define the functions

## ####################################
def noReturnVal(num1, num2):
    print("noReturnVal(", num1, num2, ") : The answer = ",(num1 + num2))

## ####################################
def returnVal(num1, num2):
    answer = num1 + num2
    return answer

## ####################################
def websiteVars(font='TNR',
                background_color='white',
                font_size='11',
                font_color='black'):
    print('      font : ', font)
    print('        bg : ', background_color)
    print(' Font size : ', font_size)
    print('Font color : ', font_color)

## ####################################
##
# ## CALL YOUR FUNCTIONS
##
## ####################################

print("Calling noReturnVal(10.13) - function doesn't return anything, results printed inside")
noReturnVal(10,13)

print("\nCalling ReturnVal(9,4) - function does addition & returns result")
answer = returnVal(9,4)
print("returnVal(9,4) = ", answer)

print("\nCalling websiteVars in order, ie, websiteVars(ComicSans, black, 14, green)")
websiteVars('ComicSans', 'black', '14', 'green')

print("\nCalling websiteVars as websiteVars(font_color=yellow,font=WingDings,bg=dk blue,size=16)")
websiteVars(font_color='yellow',
            font='Wing Dings',
            background_color='dark blue',
            font_size='16')

print("\nCalling websiteVars as websiteVars() - demoing setting default vals in fcn declaration")
websiteVars()

print("\nCalling websiteVars as websiteVars(font=Helvetica) - demoing setting default vals in fcn declaration")
websiteVars(font='Helvetica')

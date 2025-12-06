print('-----  Solve this little quiz  -----')
counter=0
sum1=0
print('1. What is the data?\n a)Raw and unorganized facts\n b)Organized facts \n c)information')
solve=input('1. Enter the solve :').lower()
print(solve)
if solve=='a':
    print('🎊 Congratulations, correct answer!')
    counter+=1
elif solve in['b','c']:
    print('Incorrect answer!')
else:
    print('Error')

print('2. What information is there?\n a)Organized facts \n b)Raw and unorganized facts \n c)Organized data')
solve=input('2. Enter the solve :').lower()
print(solve)
if solve=='c':
    print('🎊 Congratulations, correct answer!')
    counter+=1
if solve in ['b','a']:
    print('Incorrect answer!')
else:
    print('Error')


print('3. Which of the following is one of the main characteristics of Big Data? \n a)Volume \nb)Voltage \n c)Value only')
solve=input('3. Enter the solve :').lower()
print(solve)
if solve=='a':
    print('🎊 Congratulations, correct answer!')
    counter+=1
if solve in['b','c']:
    print('Incorrect answer!')
else:
    print('Error')

print('4. Which technology is commonly used for distributed Big Data processing?\n a)MySQL\n b)Hadoop\n c)Excel')
solve=input('4. Enter the solve :').lower()
print(solve)
if solve=='b':
    print('🎊 Congratulations, correct answer!')
    counter+=1
if solve in['a','c']:
    print('Incorrect answer!')
else:
    print('Error')

print('5. Which of the following is an example of unstructured data?\n a)Sales table\n  b)Excel file\n c)Images and videos')
solve=input('5. Enter the solve :').lower()
print(solve)
if solve=='c':
    print('🎊 Congratulations, correct answer!')
    counter+=1
if solve in ['a','b']:
    print('Incorrect answer!')
else:
    print('Error')
    
print('6. Data Velocity refers to:\n (A) Amount of data\n (B) Speed of data generation\n (C) Data format type')
solve=input('6. Enter the solve :').lower()
print(solve)
if solve=='b':
    print('🎊 Congratulations, correct answer!')
    counter+=1
if solve in['a','c']:
    print('Incorrect answer!')
else:
    print('Error')
    
total= counter+sum1
print(f'Number of correct questions = {counter}')
Error_questions=6-counter
print(f'Number of Error questions = {Error_questions}')
percentage=total/6 *100
print(f'Quiz result = {total}/6\n percentage ={percentage}%')
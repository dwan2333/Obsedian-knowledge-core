```python fold:Logging
# greatway to see waht's heppening in your code. Python logging module make it eazy for user to customize. 
import logging  
logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s ')  
logging.debug('Start of the Program')  
  
def factorial(n):  
    logging.debug('Start of factorial(' + str(n) + ')')  
    total = 1  
    for i in range(1,n + 1):  
       total *= i  
       logging.debug('i is '+ str(i) + ' total is ' + str(total))  
    logging.debug('End of factorial (' + str(n) + ')')  
    return total  
print(factorial(5))  
logging.debug('End of Program')
``` 
```python fold:logging_intoFiles
# they can be imported to a file that makes it ezier to read
import logging  
logging.basicConfig(filename = 'myProgramlog.txt', level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s ')  
logging.debug('Start of the Program')  
  
def factorial(n):  
    logging.debug('Start of factorial(' + str(n) + ')')  
    total = 1  
    for i in range(1,n + 1):  
       total *= i  
       logging.debug('i is '+ str(i) + ' total is ' + str(total))  
    logging.debug('End of factorial (' + str(n) + ')')  
    return total  
print(factorial(5))  
logging.debug('End of Program')

```
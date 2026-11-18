
# Import entire module
import arithmetic

# Import selected functions
from arithmetic import addition, multiplication

# Import package functions
from student import student_details, student_result


# Using entire module
result1 = arithmetic.subtraction(20, 10)

# Using selected functions
result2 = addition(10, 5)
result3 = multiplication(10, 5)

# Using package functions
student_details("Muskan", 30)

marks = [85, 90, 78, 92, 88]

student_result(marks)


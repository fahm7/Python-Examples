def get_func_mult_by_num(num):

    def mult_by(value):
        return num * value
    return mult_by

generated_func = get_func_mult_by_num(5)

print("5 * 10 =", generated_func(10))

li = [['sam',45,'CS201'],['zam',25,'CS203'],
     ['faam',15,'CS204'],
     ['tam',65,'CS205'],['andy',35,'CS301'],
     ['pady',95,'CS303']]

newlit  = [ name+ " is in "+course for name, age, course in li if(course.find("CS3")!=-1) ]

print "__________________"

print newlit


def show_result(func):
    def wrapper(a,b):
        print("result is: " , end ="")
        print(func(a,b))
    return wrapper
@show_result
def add(a,b):
    return(a+b)
add(12,23)

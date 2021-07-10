

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

#div1=smart_div(div)
#div1(2,3)       
div(2,3)
div=smart_div(div)
div(4,8)
div(4,2)
def outer():
    a = 0
    b = 1

    def inner():
        #b = 4
        print(a)
        print(b)
        #b = 4
        
    inner()

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2() 
  return x

print(myfunc1())

outer()
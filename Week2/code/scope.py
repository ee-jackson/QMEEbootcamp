# Variable scope
# One important thing to note about functions, in any language, is that variables inside functions are invisible outside of it, nor do they persist once the function has run. These are called "local" variables, and are only accessible inside their function. However, "global" variables are visible inside and outside of functions. In python, you can assign global variables. Type the following script in scope.py and try it:

_a_global = 10 #naming convention _a 

def a_function():
	_a_global = 5
	_a_local = 4
	print ("Inside the function, the value is ", _a_global)
	print("Inside the function, the value is ", _a_local)
	return None

a_function()

print("Outside the function, the value is ", _a_global)

####################
_a_global = 10

def a_function():
	global _a_global
	_a_global = 5
	_a_local = 4
	print("Inside the function, the value is ", _a_global)
	print ("Inside the function the value is ", _a_local)
return None

a_function()

print("Outside the function, the valuse is", _a_global)

# in general, avoid assigning globals because you run the risk of "exposing" unwanted variables to all functions within your name work/namespace.

_a_global = 10 # a global variable

if _a_global >= 5:
    _b_global = _a_global + 5 # also a global variable

def a_function():
    _a_global = 5 # a local variable
    
    if _a_global >= 5:
        _b_global = _a_global + 5 # also a local variable
    
    _a_local = 4
    
    print("Inside the function, the value of _a_global is ", _a_global)
    print("Inside the function, the value of _b_global is ", _b_global)
    print("Inside the function, the value of _a_local is ", _a_local)
    
    return None

a_function()

print("Outside the function, the value of _a_global is ", _a_global)
print("Outside the function, the value of _b_global is ", _b_global)

# Thus,though _a_global was overwritten inside the function, what happened inside the function remained inside the function (What happens in Vegas...) . Note that _a_global is just a naming convention – nothing special about this variable as such.

# Of course, if you assign a variable outside a function, it will be available inside it even if you don't assign it inside that function:

_a_global = 10

def a_function():
    _a_local = 4
    
    print("Inside the function, the value _a_local is ", _a_local)
    print("Inside the function, the value of _a_global is ", _a_global)
    
    return None

a_function()

print("Outside the function, the value of _a_global is", _a_global)

# So _a_global was available to the function, and you were able to use it in the print command.

# If you really want to modify or assign a global variable from inside a function (that is, and make it available outside the function), you can use the global keyword:

_a_global = 10

print("Outside the function, the value of _a_global is", _a_global)

def a_function():
    global _a_global
    _a_global = 5
    _a_local = 4
    
    print("Inside the function, the value of _a_global is ", _a_global)
    print("Inside the function, the value _a_local is ", _a_local)
    
    return None

a_function()

print("Outside the function, the value of _a_global now is", _a_global)

# Outside the function, the value of _a_global is 10
# Inside the function, the value of _a_global is  5
# Inside the function, the value _a_local is  4
# Outside the function, the value of _a_global now is 5
# So, using the global specification converted _a_global to a truly global variable that became available outside that function (overwriting the original _a_global).

# The global keyword also works from inside nested functions, but it can be slightly confusing:

def a_function():
    _a_global = 10

    def _a_function2():
        global _a_global
        _a_global = 20
    
    print("Before calling a_function, value of _a_global is ", _a_global)

    _a_function2()
    
    print("After calling _a_function2, value of _a_global is ", _a_global)

a_function()

print("The value of a_global in main workspace / namespace is ", _a_global)

# That is, using the global keyword inside the inner function _a_function2 resulted in changing the value of _a_global in the main worspace / namespace to 20, but within the scope of _a_function, remained 10!

# Compare the above with this:

_a_global = 10

def a_function():

    def _a_function2():
        global _a_global
        _a_global = 20
    
    print("Before calling a_function, value of _a_global is ", _a_global)

    _a_function2()
    
    print("After calling _a_function2, value of _a_global is ", _a_global)

a_function()

print("The value of a_global in main workspace / namespace is ", _a_global)

# Now, because _a_global was defined in advance (outside the first function), it get modified when changes in the inner function (it does not exist as a local within the scope of _a_function, but is "inherited" from the main scope / workspace / namespace).

# ⋆
#  Collect all three blocks of code above illustrating variable scope into one script called scope.py and test it (run and check for errors).

# In general, avoid assigning globals because you run the risk of "exposing" unwanted variables to all functions within your workspace / namespace. However, in some cases, you may find it useful to impose one or more global variables that are available across multiple modules/functions. You can do this by assigning the global variables at the start of the script/program, or by creating a separate module (say, called config.py) to hold the global variables and then import it.
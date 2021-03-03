import os

def fun_env_var_and_param(param):
    x = os.environ.get('VALUE')
    print(param)
    print(x)
    resp = str(param)+'somesting'+str(x)
    print(resp)
    return resp

def with_env_var():
    x = os.environ.get('VALUE')
    y = int(x)*2
    print (y)
    return y

def with_input_param(a, b):
    c = a + b
    print(c)
    return c

def without_input_param():
    k = 'hello_test_autodep234567';
    print(k)
    return {"result":k}

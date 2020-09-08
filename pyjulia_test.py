# This is a python script that runs the julia code 'pyjulia_test.jl')
# The output of the julia code is assigned to the variable x below

from julia.api import Julia
jl = Julia(compiled_modules=False)
from julia import Main
x = Main.include("pyjulia_test.jl") #should equal 3 when called in Python interactive window
x
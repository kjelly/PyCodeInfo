PyCodeInfo
==========

introduction
------------

show code info. For example, show how many branch in the function.


count_branch
------------

Count how many branch in the code object. Branch means any behavior like jump_if.
For example, the statement like "if(...){XXX}" will generate the opcode "POP_JUMP_IF_FALSE".
The function which have many branch means that it do many thing and it need many test case.
The function never count anything about loop, like for.


count_branch_in_model
---------------------

Display number of branch for each function(or method) in module(or class).


count_loop
----------

Count how many loop in code object.

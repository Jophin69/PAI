% Addition
add(X, Y, Result) :- Result is X + Y.

% Subtraction
subtract(X, Y, Result) :- Result is X - Y.

% Multiplication
multiply(X, Y, Result) :- Result is X * Y.

% Division
divide(X, Y, Result) :- Y =\= 0, Result is X / Y.


?- add(5, 3, Sum).       % Sum = 8
?- subtract(10, 4, Diff). % Diff = 6
?- multiply(3, 7, Prod).  % Prod = 21
?- divide(10, 2, Quot).   % Quot = 5
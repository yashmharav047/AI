% factorial.pl

fact(0, 1).
fact(N, F) :-
    N > 0,
    N1 is N - 1,
    fact(N1, F1),
    F is N * F1.

start :-
    write('Enter n: '),
    read(N),
    fact(N, F),
    write('Factorial = '), write(F), nl.

:- initialization(start).

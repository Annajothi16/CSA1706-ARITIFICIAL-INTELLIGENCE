hanoi(1, S, D, _) :-
    write('Move disk from '),
    write(S),
    write(' to '),
    write(D),
    nl.

hanoi(N, S, D, A) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, S, A, D),
    write('Move disk from '),
    write(S),
    write(' to '),
    write(D),
    nl,
    hanoi(N1, A, D, S).
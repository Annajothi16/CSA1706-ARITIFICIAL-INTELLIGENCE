fact(human(socrates)).

rule(mortal(X), [human(X)]).

forward_chain :-
    fact(human(X)),
    assertz(known(mortal(X))),
    write(X),
    write(' is mortal'),
    nl.

% Forward Chaining Program

% Initial known facts
:- dynamic known/1.

known(fever).
known(cough).

% Inference rule
rule([fever, cough], common_cold).

% Apply rules to generate new facts
apply_rule :-
    rule(Conditions, Conclusion),
    maplist(known, Conditions),
    \+ known(Conclusion),
    assertz(known(Conclusion)),
    write('New fact added: '),
    write(Conclusion),
    nl.

% Forward chaining process
forward_chaining :-
    (   apply_rule
    ->  forward_chaining
    ;   write('No more rules can be applied.'), nl
    ).

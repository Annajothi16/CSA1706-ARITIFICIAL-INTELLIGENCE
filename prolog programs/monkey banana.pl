% Monkey Banana Problem

move(state(P, floor, B, no),
     walk(P, Q),
     state(Q, floor, B, no)) :-
    member(Q, [door, window, middle]),
    P \= Q.

move(state(P, floor, P, no),
     push(P, Q),
     state(Q, floor, Q, no)) :-
    member(Q, [door, window, middle]),
    P \= Q.

move(state(middle, floor, middle, no),
     climb,
     state(middle, box, middle, no)).

move(state(middle, box, middle, no),
     grasp,
     state(middle, box, middle, yes)).

% Main solving predicate

solve(State, Steps) :-
    path(State, [State], Steps).

% Goal condition

path(state(_, _, _, yes), _, []).

% Avoid revisiting previous states

path(State, Visited, [Action | Rest]) :-
    move(State, Action, NextState),
    \+ member(NextState, Visited),
    path(NextState, [NextState | Visited], Rest).
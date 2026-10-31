edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(e, g).
edge(f, g).

heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 2).
heuristic(d, 5).
heuristic(e, 3).
heuristic(f, 1).
heuristic(g, 0).

connected(X, Y) :- edge(X, Y).
connected(X, Y) :- edge(Y, X).

best_first(Start, Goal, Path) :-
    search([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

search([[Goal|Rest]|_], Goal, [Goal|Rest]).

search([[Current|Rest]|Other], Goal, Path) :-
    findall([Next,Current|Rest],
        (connected(Current,Next),
         \+ member(Next,[Current|Rest])),
        New),
    append(Other, New, All),
    predsort(compare_paths, All, Sorted),
    search(Sorted, Goal, Path).

compare_paths(Order, [A|_], [B|_]) :-
    heuristic(A, HA),
    heuristic(B, HB),
    compare(Order, HA, HB).
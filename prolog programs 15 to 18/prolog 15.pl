
% Marcus and Caesar Problem

% 1. Marcus was a man
man(marcus).

% 2. Marcus was a Pompeian
pompeian(marcus).

% 3. All Pompeians were Romans
roman(X) :-
    pompeian(X).

% 4. Caesar was a ruler
ruler(caesar).

% 5. All Romans are either loyal to Caesar or hate Caesar
loyal(X, caesar) :-
    roman(X),
    \+ not_loyal(X, caesar).

hates(X, caesar) :-
    roman(X),
    not_loyal(X, caesar).

% 6. Everyone is loyal to someone
loyal_to_someone(X) :-
    loyal(X, _).

% 7. People try to assassinate only rulers
% to whom they are not loyal
not_loyal(X, Y) :-
    person(X),
    ruler(Y),
    try_assassinate(X, Y).

% 8. Marcus tried to assassinate Caesar
try_assassinate(marcus, caesar).

% 9. All men are people
person(X) :-
    man(X).

% Queries:
% ?- loyal(marcus, caesar).
% ?- hates(marcus, caesar).
% ?- not_loyal(marcus, caesar).

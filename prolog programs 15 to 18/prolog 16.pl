
% 1. John likes all kinds of food
likes(john, X) :- food(X).

% 2. Apple and vegetables are food
food(apple).
food(vegetable).

% 3. Anything eaten by a living person is food
food(Y) :- eats(X, Y), alive(X).

% 4. Anil eats peanuts
% 5. Harry eats everything Anil eats
eats(anil, peanuts).
eats(harry, X) :- eats(anil, X).

% Anil is alive
alive(anil).


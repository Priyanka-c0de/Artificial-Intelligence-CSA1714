%set 1 input student : ?- professor(kirke, charlie).
%set 1 Q4: Towers of Hanoi
% Move N disks from rod X to rod Y using rod Z as auxiliary
move(1, X, Y, _) :- 
    write('Move top disk from '), write(X), write(' to '), write(Y), nl.
move(N, X, Y, Z) :- 
    N > 1, 
    M is N - 1, 
    move(M, X, Z, Y), 
    move(1, X, Y, _), 
    move(M, Z, Y, X).
    %input : ?- move(3, a, c, b).
%---------------------------------
%set bird input:?- fly(penguin).
%----------------------------------
% set 2 Family Tree
female(pam).
female(liz).
female(ann).
female(pat).
male(tom).
male(bob).
male(jim).

% (Assumed parent relations to make the tree function)
parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

% Rules required by Set 2
mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).
grandfather(X, Z) :- father(X, Y), parent(Y, Z).
grandmother(X, Z) :- mother(X, Y), parent(Y, Z).
sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), X \= Y.
brother(X, Y) :- parent(Z, X), parent(Z, Y), male(X), X \= Y.
%input :  ?- grandfather(Grandpa, ann).
%---------------------------------
%Set 3Q3: Monkey and Banana Problem
% state(MonkeyLocation, MonkeyOn, BananaLocation, HasBanana)
move(state(middle, onbox, middle, hasnot), grasp, state(middle, onbox, middle, has)).
move(state(P, onfloor, P, H), climb, state(P, onbox, P, H)).
move(state(P1, onfloor, P1, H), push(P1, P2), state(P2, onfloor, P2, H)).
move(state(P1, onfloor, B, H), walk(P1, P2), state(P2, onfloor, B, H)).

canget(state(_, _, _, has)).
canget(State1) :- 
    move(State1, _, State2), 
    canget(State2).
    %input ?- canget(state(atdoor, onfloor, atwindow, hasnot)).
%-----------------------------------------
%Set 3 Q4: Forward Chaining (Criminal Inference)
american(robert).
enemy(countryA, america).
missile(m1).
owns(countryA, m1).

sells(robert, X, countryA) :- missile(X), owns(countryA, X).
weapon(X) :- missile(X).
hostile(X) :- enemy(X, america).

criminal(X) :- american(X), weapon(Y), sells(X, Y, Z), hostile(Z).
%input : ?- criminal(robert).
%--------------------------------------
%Set 6 : Q3: Forward Chaining (Weather)
rainy(chennai).
rainy(coimbatore).
rainy(ooty).
cold(ooty).

% Rule inference
stay_inside(X) :- rainy(X), cold(X).
%------------------------------------
%Set 7 Pattern Matching 
first_name(tonyblair, tony).
first_name(georgebush, georgedubya).
second_name(tonyblair, blair).
second_name(georgebush, bush).

% Retrieve full name details
full_name(ID, First, Last) :- first_name(ID, First), second_name(ID, Last).
%------------------------------
%Set 8 Items and Loactions
location(desk, office).
location(apple, kitchen).
location(flashlight, desk).

% Rule to find item recursively (e.g., flashlight is in the office)
in_room(Item, Room) :- location(Item, Room).
in_room(Item, Room) :- location(Item, Container), in_room(Container, Room).
%------------------------------------------
%Set 8 Disease
symptom(amit, fever).
symptom(amit, rash).

hypothesis(Patient, measles) :- symptom(Patient, fever), symptom(Patient, rash).
hypothesis(Patient, cold) :- symptom(Patient, fever).
%------------------------------------------------------

% Set 9 Inference engine
interpret(true) :- !.
interpret((GoalA, GoalB)) :- !,
    interpret(GoalA),
    interpret(GoalB).
interpret(Goal) :- 
    clause(Goal, Body), 
    interpret(Body).
%----------------------------------------
%Set 9 : Vowels
sentence("This is my first Degree in Saveetha School of Engineering.").

is_vowel(Char) :- member(Char, "aeiouAEIOU").

count_vowels([], 0).
count_vowels([Char|Tail], Count) :-
    is_vowel(Char), !,
    count_vowels(Tail, TailCount),
    Count is TailCount + 1.
count_vowels([_|Tail], Count) :-
    count_vowels(Tail, Count).

% Query string: ?- sentence(S), count_vowels(S, Count).
%-----------------------------------------------------
%Set 10 Q3: Resolution Refutation (Happy Student Problem)  
% Anyone passing history exams and winning the lottery is happy.
happy(X) :- pass_history(X), win_lottery(X).

% Anyone who studies or is lucky can pass all exams.
pass_history(X) :- studies(X).
pass_history(X) :- lucky(X).

% Anyone who is lucky wins the lottery.
win_lottery(X) :- lucky(X).

% John did not study, but he is lucky.
lucky(john).
% (Omit studies(john) entirely since he did not study)

% Query to prove: ?- happy(john).
%---------------------------------------------
%Q4: Mortal or Not  Prolog
person(socrates).
person(einstein).
person(alexander).

mortal(X) :- person(X).
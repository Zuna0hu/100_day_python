Hurdles race
Reeborg has entered a hurdle race. Make him run the course, following the path shown.

The position, the height and the number of hurdles changes each time this world is reloaded.
What you need to know
You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.

Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3


Lost in a maze
Reeborg was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

What you need to know
The functions move() and turn_left().
Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).

The main idea in my solution is to move forward until there's a wall in front, and then prioritize turning right if there is no wall on the right. However, to avoid getting stuck in a loop, I also incorporate the occasional left turn and move after a certain number of iterations. This ensures that the robot explores different paths and has a higher chance of finding the exit.
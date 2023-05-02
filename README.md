# 100 Day Python
This repository contains my solutions to the projects in the "100 Days of Code - The Complete Python Pro Bootcamp" course on Udemy. In the following, I will provide some highlights of my solutions.

# Day 6
The main idea in my solution is to move forward until there's a wall in front, and then prioritize turning right if there is no wall on the right. However, to avoid getting stuck in a loop, I also incorporate the occasional left turn and move after a certain number of iterations. This ensures that the robot explores different paths and has a higher chance of finding the exit.

If we don't incorporate the occasional left turn and move after a certain number of iterations, the code may get stuck in a loop, as illustrated by the following scenario.
<div style="display: flex; justify-content: center;">
  <img src="https://user-images.githubusercontent.com/124393973/235746142-dd2dfd3f-4807-4139-b4d6-fd70129d257a.png"
 alt="reeborg" width="240" height="240">
</div>

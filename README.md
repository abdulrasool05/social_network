Each file is a sorted "network". Each row in the file represents two user IDs where the first user is friends with the second user. Each friendship is only listed once in the file such that the ID of the first user is less than the second user. For example, if ID 4 and 7 are friends:

The file would display:
4  7

NOT:
7  4

The program uses these files to create a network where each user ID has all their friends. With this network, the program can:

-List common friends of two users in a given network 
-Recommend new friends. A recommended friend is a person you are not already friends with and with whom you have the most friends in common in the whole network.
-Display stats about the network.

*Further explanations for each of the specific functions is provided in the docstrings of the python file.


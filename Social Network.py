
import random

def getuserFriends(userId, network):
    '''
    (int, 2D list)->list
    Precondition: User id exists in network and network is sorted by id's.
    Returns a sorted list of friends for a given user, provided the user id and network. 
    '''
    b=0
    e=len(network)-1
    notFound=True
    
    while b<=e and notFound:
        mid=e-b//2
        if userId>network[mid][0]:
            b=mid+1
        elif userId<network[mid][0]:
            e=mid-1
        else:
            userFriends=network[mid][1]
            notFound=False

    return userFriends

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    
    friends = open(file_name).read().splitlines()
    network=[]
    friendslist=[]
    first=True
    tempnetwork=[]
    
    for i in friends:
        if first:
            numPeople=int(i)
            first=False
        else:
            friendslist.append(i.split())

    for i in friendslist:
        exists1=False
        exists2=False
        for x in tempnetwork:
            if int(i[0])==x[0]:
                exists1=True
                index=tempnetwork.index(x)
                tempnetwork[index].append(int(i[1]))
            if int(i[1])==x[0]:
                exists2=True
                index=tempnetwork.index(x)
                tempnetwork[index].append(int(i[0]))
                

        if exists1==False:
            tempnetwork.append([int(i[0]),int(i[1])])
        if exists2==False:
            tempnetwork.append([int(i[1]),int(i[0])])
       

    tempnetwork.sort()

    for y in tempnetwork:
        firstId=y[0]
        addTup=((y[0]),y[1:])
        network.append(addTup)
        
    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''

    common=[]


    user1Friends=getuserFriends(user1, network)

    user2Friends=getuserFriends(user2, network)

   
    total=user1Friends+user2Friends
    total.sort()

    for i in range(len(total)-1):
        if total[i]==total[i+1]:
            common.append(total[i])

    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    userFriends=getuserFriends(user, network)
    maxId=-1
    maximum=0
    alreadyFriends=False
    
    for i in network:
        if user!=i[0]:
            friends=0
            alreadyFriends=False
            total=userFriends+i[1]
            total.sort()
            for x in range(len(total)-1):
                if total[x]==user:
                    alreadyFriends=True
                else:
                    if total[x]==total[x+1]:
                        friends=friends+1
            if alreadyFriends==False:
                if friends>maximum:
                    maximum=friends
                    maxId=i[0]
                elif friends==maximum and i[0]<maxId:
                    maxId=i[0]

    if maxId==-1:
        return None
    else:
        return maxId

    


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    counter=0
    for i in network:
        if len(i[1])>=k:
            counter=counter+1
    return counter
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    maximum=len(network[0][1])
    for i in network:
        if len(i[1])>maximum:
            maximum=len(i[1])
    return maximum
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]

    maximum=maximum_num_friends(network)
    for i in network:
        if len(i[1])==maximum:
            max_friends.append(i[0])
            
    return    max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''
    adder=[]
    for i in network:
        adder.append(len(i[1]))
    return sum(adder)/len(adder)
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    for i in network:
        if len(i[1])==len(network)-1:
            return True
    return False

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    allId=[]
    invalid=True
    for i in network:
        allId.append(i[0])

    while invalid:
        try:
            userId=int(input("Enter an input for a user ID: "))
            invalid=False
        except ValueError:
            print("That was not an integer. Please try again.")
            invalid=True
        else:
            if userId not in allId:
                print("That user ID does not exist. Try again.")
                invalid=True

    return userId


file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    

import sys,os

files = (sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])


votes = dict()
posts = next(os.walk('./Candidates'))[1] # [Gsec Academics , Gsec Cultural, Gsec Sports]

for each_post in posts :
    votes[each_post] = dict()
    persons = []

    for person in os.listdir('./Candidates/' + str(each_post)) :
        if person == '.DS_Store' :
            continue

        name_of_person = os.path.splitext(os.path.basename(str(person)))[0]
        persons.append(name_of_person)

    for each_name in persons :
        votes[each_post][each_name] = 0

	votes[each_post][None] = 0

print votes
for i in files :
    with open(i,"r") as fileout :
        a = fileout.read().strip()
        a= a.split("\n")

        for per_person in a :
            per_vote = per_person.strip(",").split(",")
            for j in per_vote :
                k = j.split(":")
                print k
                try :
                    votes[k[0]][k[1]] += 1
                except :
                    votes[k[0]][eval(k[1])] += 1

print votes
print
print "------------------------"
print

for i in votes :
    print "Post : ",i
    print "name\t|\tvotes"
    for j in votes[i] :
        print "%s\t:\t%s"%(j,votes[i][j])
    print "\n____________________________________\n\n"



print "Winners :- "
for i in votes :
    maxi_val = None
    maxi = None

    for j in votes[i] :
        if votes[i][j] > maxi_val and j != None :
            maxi_val = votes[i][j]
            maxi = j
    print i , " ==> ", maxi , " : ",maxi_val

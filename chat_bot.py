#!/usr/bin/python
import sys


files = len(sys.argv)
dict = []
s = ""
i = 0
s2 = ""
list2 = []
c1 = ''

if files <= 1 :
    print "please enter correct arguments"
    sys.exit()

#build list
d=1
while d < files:
    c = ''
    try:
        f = file(sys.argv[d],'r')
    except:
        print "please enter correct arguments"
        sys.exit()
    else:
        while (len(c) > 0)|(i==0):
            i = 1
            c1 = c
            c = f.read(1)
            if c.isalpha():
                s += str(c)
            else:
                if (c == ' ')or(c == '-')or(c == '\n')or(len(c)==0):
                    if s != "":
                        list2.append(s.lower())
                    if (c1 == '.')or(c1 == '?')or(c1 == '!'):
                        list2.append('.')
                    s = ""
    i = 0
    d += 1

#build end_pair
key = ""
j = 0
past1 = ""
past2 = ""
end_pair = []
length = len(list2)-1
for index in range(length):
    j+= 1
    if(list2[index] != '.'):
        if(j>2):
            past1 = list2[index-1]
            past2 = list2[index]
    else:
        end_pair.append(past1+"-"+past2)
        
if(list2[length]=='.'):#handle exception
    end_pair.append(list2[length-2]+"-"+list2[length-1])

list2[:] = (value for value in list2 if value != '.')#remove .

#build dict
for index in range(len(list2)-1):
    dict.append((list2[index],list2[index+1]))

k = 1

while k==1 :

    print "Send:",
    #extract word from stdin
    line = sys.stdin.readline()
    if len(line)!=1 and line:
        last_word2 = line.split()[-1]
        last_word = filter(str.isalpha,last_word2)
        response = []
        t = ()
        u = 0
        track1 = ""#to track if has end_pair
        track2 = ""
        v = 0
        while u<20:
            u += 1
            for index in range(len(dict)):
                t=dict[index]
                if(last_word == t[0]):
                    response.append(t[1])
                    track1 = track2
                    track2 = t[1]
                    last_word = t[1]
                    break
                if(index == len(dict)-1):#arbitary case
                    if v ==0 :
                        response.append(dict[index-1][1])
                        track1 = track2
                        track2 = dict[index-1][1]
                        last_word = dict[index-1][1]
                        v += 1
                    else:
                        break

            if(end_pair.count(track1+"-"+track2) > 0):#check if need to be end
                break
        print "receive:",
        for index in range(len(response)):
            if index == 0:
                print response[index].capitalize(),
            else:
                print response[index],

        print '.'
    elif line=='' :
        sys.exit()
    else :
        print "please enter correct message"



import csv
import codecs

objects = ["chips","pringles","peanuts","chocolate","mints","chocolate egg","noodles","apple","paprika","melon"
           ,"sushi","tea","beer","coke","shampoo","cloth","sponge","bowl","mug","glass","box","tray"
           ,"bag"]
category = ["snack","candies","freshfood","drinks","toiletries","containers"]
placements = ["bedside", "living shelf", "TV Stand","living table","center table", "bar","drawer","desk","bar",
              "cupboard","sink","sideshelf","bookcase","dining table","fridge","counter","cabinet"]
room = ["bedroom", "living room","office","kitchen","corridor","bathroom"]
beacon = ["bed", "living table", "TV stand","living table","bar","desk","sink","dining table","cabinet","cupboard"]
comparativ = ['heaviest','smallest','biggest','lightest']
superlatif = ['heavier','smaller','bigger','lighter']
people = ['children','adults','elders','males','females','men','women','boys','girls']
pospers = ['standing', 'sitting', 'lying']
color = ['red','blue','white','black','green','yellow','brown','pink','opaque']

questions = open("questions_objets.txt", "w")


for obj in objects:
    questions.write("\n" + "Where can I find a %s ?" % obj)
    questions.write("\n" + "What's the colour of the %s ?" % obj)
    questions.write("\n" + "To which category belong the %s ?" % obj)

for cat in category:
    questions.write("\n" + "Where can I find a %s ?" % cat)
    questions.write("\n" + "How many %s there are ?" % cat)

for loc in placements:
    questions.write("\n" + "What objects are stored in the %s ?" % loc)

for cat in category:
    for adja in comparativ:
        questions.write("\n" + "Which is the %s %s ?" % (adja, cat))

for cat in category:
    for plac in placements:
        questions.write("\n" + "How many %s are in the %s ?" % (cat, plac))

for obj in objects:
    for obj2 in objects:
        questions.write("\n" + "Do the %s and %s belong to the same category ?" % (obj, obj2))

for obj in objects:
    for obj2 in objects:
        for a in superlatif:
            questions.write("\n" + "Between the %s and %s which one is %s ?" % (obj, obj2, a))

questions.close()

questions_arene = open("questions_arene.txt", "w")

for loc in placements:
    questions_arene.write("\n" + "Where is the located the %s ?" % loc)
    questions_arene.write("\n" + "In which room is the %s ?" % loc)

for loc in placements:
    for r in room:
        questions_arene.write("\n" + "How many %s are in the %s ?" % (loc,r))

for beac in beacon:
    questions_arene.write("\n" + "Where is the located the %s ?" % beac)
    questions_arene.write("\n" + "In which room is the %s ?" % beac)

for beac in beacon:
    for r in room:
        questions_arene.write("\n" + "How many %s are in the %s ?" % (beac, r))

for r in room:
    questions_arene.write("\n" + "How many doors has the %s ?" %r)

questions_arene.close()

questions_crowd = open("questions_crowd.txt", "w")

for p in people:
    questions_crowd.write("\n" + "How many %s are in the crowd ?" %p)
    questions_crowd.write("\n" + "Tell me the number of %s in the crowd ?" % p)

for p in pospers:
    questions_crowd.write("\n" + "How many people in the crowd are %s ?" % p)

for p in pospers:
    for peop in people:
        questions_crowd.write("\n" + "Was the %s person %s ?" %(p,peop))
        questions_crowd.write("\n" + "Tell me if the %s person was a %s ?" % (p,peop))

for col in color:
    questions_crowd.write("\n" + "Tell me how many people were wearing %s ?" % col)
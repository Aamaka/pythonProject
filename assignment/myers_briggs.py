counter = "a"
counter1 = "b"
colm = None
myers_briggs = [{"Question 1: (a) expend energy, enjoy group     (b)  conserve energy, enjoy one on one"},
                {"Question 2: (a)  interpret literally           (b) look for meaning and possibilities"},
                {"Question 3: (a)  logical,thinking,Questioning  (b)  empathetic,feeling,accommodating"},
                {"Question 4: (a)  organized,orderly             (b) flexible,adaptable "},
                {"Question 5: (a) more outgoing,think aloud      (b)more reserved,think to yourself "},
                {"Question 6: (a) practical,realistic,experiential (b) . imaginative,innovative,theoretical"},
                {"Question 7: (a) candid,straight forward, frank   (b)  tactful, kind ,encouraging "},
                {"Question 8: (a) plan,schedule                     (b) unplanned spontaneous "},
                {"Question 9: (a) seek many tasks,public activities,interaction with others (b) seek private,"
                 "solitary activities with quite to concentrate"},
                {"Question 10: (a)standard,usual,conventional            (b) different,novel,unique"},
                {"Question 11: (a) firm,tend to criticize,hold the line  (b) gentle,tend to appreciate,conciliate"},
                {"Question 12: (a) regulated                             (b) easygoing, 'live' and 'let live'"},
                {"Question 13: (a)  external,communicative,express yourself   (b)internal,reticent,keep to yourself "},
                {"Question 14: (a) focus on here-and-now     (b)look to the future,global perspective,'big picture'"},
                {"Question 15: (a) tough-minded,just         (b)tender-heart,merciful "},
                {"Question 16: (a) preparation,plan ahead    (b) go with the flow,adapts as you go"},
                {"Question 17: (a)  active,initial           (b) reflective,deliberate"},
                {"Question 18: (a) facts,things,'what is'    (b) ideas,dreams,'what could be',philosophy  "},
                {"Question 19: (a) matter of facts,issue-oriented  (b)  sensitive,people-oriented,compassionate"},
                {"Question 20: (a) control,govern                (b) latitude,freedom"},
                ]

for myers in myers_briggs:
    answer = input(myers)
    print(answer)

    if answer[:17:4] == counter or counter1:
        if counter > counter1:
            colm = "E"
        else:
            colm = "I"
            answer.index(answer, 0, 14)
    print(colm)

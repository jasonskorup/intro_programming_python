s1 = "For instance, on the planet Earth, man had always assumed that he was more intelligent than dolphins because" \
     " he had achieved so much — the wheel, New York, wars and so on — whilst all the dolphins had ever done was muck" \
     " about in the water having a good time. But conversely, the dolphins had always believed that they were far" \
     " more intelligent than man — for precisely the same reasons."

s2 = "The last ever dolphin message was misinterpreted as a surprisingly sophisticated attempt to do a" \
     " double-backwards-somersault through a hoop whilst whistling the ‘Star Spangled Banner’, but in fact the" \
     " message was this: So long and thanks for all the fish."

unique_s1 = set(s1.split(" "))

unique_s2 = set(s2.split(" "))

print(unique_s1)

print("Unique Word Count S1: ", len(unique_s1))

print(unique_s2)

print("Unique Word Count S2: ", len(unique_s2))

print(unique_s1.intersection(unique_s2))

print("Inner Join Count: ", len(unique_s1.intersection(unique_s2)))

print(unique_s1 ^ unique_s2)

print("Outer Join Count: ", len(unique_s1 ^ unique_s2))

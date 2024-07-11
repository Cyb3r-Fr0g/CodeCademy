#Lists -- Gradebook -- Cyb3r_Fr0g -- 7/11/24

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 97], ["calculus", 97], ["poetry", 85], ["history", 88]]

#print(gradebook)

#Add more subjects

gradebook.append(["computer science", 100])
#ctr+c ctr+v
gradebook.append(["visual arts", 93])
#print(gradebook)

gradebook[-1][-1] += 5
#print(gradebook)

gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook, "\n\n")

#One Big Gradebook

full_gradebook = last_semester_gradebook + gradebook
#print(full_gradebook)

full_gradebook.append(["Python, 100"])
print(full_gradebook)



python_students = {"Ravi", "Anu", "Sai", "Kiran", "Teja"}
sql_students = {"Sai", "Teja", "Rahul", "Anu", "Priya"}

# 1. Both courses
print(python_students & sql_students)   # {'Sai', 'Teja', 'Anu'}

# 2. Only Python
print(python_students - sql_students)   # {'Ravi', 'Kiran'}

# 3. Only SQL
print(sql_students - python_students)   # {'Rahul', 'Priya'}

# 4. Either course
print(python_students | sql_students)   # {'Ravi','Anu','Sai','Kiran','Teja','Rahul','Priya'}

# 5. Exactly one course
print(python_students ^ sql_students)   # {'Ravi','Kiran','Rahul','Priya'}







teamA = {"Python", "SQL", "Git", "Docker"}
teamB = {"Java", "SQL", "AWS", "Git"}

# 1. Common skills
print(teamA & teamB)   # {'SQL','Git'}

# 2. Only Team A
print(teamA - teamB)   # {'Python','Docker'}

# 3. Only Team B
print(teamB - teamA)   # {'Java','AWS'}

# 4. All skills
print(teamA | teamB)   # {'Python','SQL','Git','Docker','Java','AWS'}

# 5. Add Linux to Team A, remove Java from Team B
teamA.add("Linux")
teamB.discard("Java")
print(teamA)  # {'Python','SQL','Git','Docker','Linux'}
print(teamB)  # {'SQL','AWS','Git'}





amazon = {"Ravi","Anu","Kiran","Sai","Teja"}
flipkart = {"Sai","Teja","Rahul","Priya","Anu"}

# 1. Both stores
print(amazon & flipkart)   # {'Sai','Teja','Anu'}

# 2. Only Amazon
print(amazon - flipkart)   # {'Ravi','Kiran'}

# 3. Only Flipkart
print(flipkart - amazon)   # {'Rahul','Priya'}

# 4. All unique customers
print(amazon | flipkart)   # {'Ravi','Anu','Kiran','Sai','Teja','Rahul','Priya'}

# 5. Exactly one store
print(amazon ^ flipkart)   # {'Ravi','Kiran','Rahul','Priya'}





batch1 = {"Python","Java","C","SQL"}
batch2 = {"Python","Java","React","JavaScript"}

# 1. Known by both
print(batch1 & batch2)   # {'Python','Java'}

# 2. Only Batch 1
print(batch1 - batch2)   # {'C','SQL'}

# 3. Only Batch 2
print(batch2 - batch1)   # {'React','JavaScript'}

# 4. Is Batch1 subset of Batch2?
print(batch1.issubset(batch2))   # False

# 5. Is Batch2 superset of Batch1?
print(batch2.issuperset(batch1)) # False




day1 = {"user1","user2","user3","user4","user5"}
day2 = {"user3","user4","user5","user6","user7"}

# 1. Returning visitors
print(day1 & day2)   # {'user3','user4','user5'}

# 2. Only Day 1
print(day1 - day2)   # {'user1','user2'}

# 3. Only Day 2
print(day2 - day1)   # {'user6','user7'}

# 4. All unique visitors
print(day1 | day2)   # {'user1','user2','user3','user4','user5','user6','user7'}

# 5. Exactly one day
print(day1 ^ day2)   # {'user1','user2','user6','user7'}

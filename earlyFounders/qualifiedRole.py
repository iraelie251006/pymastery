job_roles = [
    {'role': 'Data Analyst', 'skills': ['Python', 'SQL', 'Excel']},
    {'role': 'Data Scientist', 'skills': ['Python', 'R', 'Machine Learning', 'Deep Learning']},
    {'role': 'Machine Learning Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-Learn']},
    {'role': 'Data Engineer', 'skills': ['Python', 'Apache Spark', 'Hadoop', 'SQL']},
    {'role': 'Business Intelligence Analyst', 'skills': ['Python', 'SQL', 'Tableau', 'Power BI', 'Excel']},
    {'role': 'Quantitative Analyst', 'skills': ['R', 'Python', 'MATLAB', 'Statistics']},
    {'role': 'Operations Analyst', 'skills': ['Python', 'SQL', 'Data Visualization', 'Process Improvement']},
    {'role': 'Database Administrator', 'skills': ['SQL', 'Oracle', 'MySQL', 'Database Management']},
    {'role': 'AI Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Computer Vision']},
    {'role': 'Statistician', 'skills': ['R', 'SAS', 'Python', 'Statistical Modeling']}
]

my_skills = ['Python', 'SQL', 'Excel']

# Finding roles that match all my skills using all() function

qualified = []
for job in job_roles:
    if all(skill in job["skills"] for skill in my_skills):
        qualified.append(job["role"])
print(qualified)
qualified_roles = []

# Finding roles that match all my skills using a for loop

for job in job_roles:
    qualified = True
    for skill in my_skills:
        if skill not in job["skills"]:
            qualified = False

    if qualified:
        qualified_roles.append(job["role"])

print("Roles that match all my skills:", qualified_roles)

# Using list comprehension to find qualified roles based on skills

qualified_roles = [job['role'] for job in job_roles if all(skill in job["skills"] for skill in my_skills)]

print('Qualified for the following roles: ', ', '.join(qualified_roles))
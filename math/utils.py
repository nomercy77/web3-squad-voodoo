import numpy as np

# Defining Information theoritic KL divergence between two skill distributions in bits. This wil be useful later

def get_KL(p_skills, q_skills):
  # log(negative or 0) leads to -infinity, therefore replacing by infinitesimal values, 
  # this will change bit value slightly but all by constant degree, hence order will remain intact  
  p_skills = np.where(p_skills > np.exp(-100), p_skills, np.exp(-10))
  q_skills = np.where(q_skills > np.exp(-100), q_skills, np.exp(-10))

  try:
    return sum(p_skills[i] * np.log2(p_skills[i]/q_skills[i]) for i in range(len(p_skills)))

  except:
    return "Not valid distribution(s). Try changing the values."


# Defining Degree of symmetry between two vectors as their . product

def get_symmetry(p_skills,q_skills, degree):
  aligned = np.dot(p_skills,q_skills)
  degree_of_symmetry = degree*aligned
  return degree_of_symmetry

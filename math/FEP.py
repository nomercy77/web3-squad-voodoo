import numpy as np
from pymdp import utils,maths


def variational_free_energy(prior, likelihood_dist):
  joint_prob = likelihood_dist * prior # element-wise product of the likelihood of each hidden state, given the observation, with the prior probability assigned to each hidden state
  p_o = joint_prob.sum()

  try:
    posterior = joint_prob / p_o
    surprise = -np.log(p_o)
    return surprise.round(3)

  except:
    return None


def FE_threshold(FEs, top_n):
  sorted_FEs = dict(sorted(FEs.items(), key=lambda item: item[1]))
  top_n_people = {k: sorted_FEs[k] for k in list(sorted_FEs)[:top_n]}

  return top_n_people

WITHIN_GATE_PEOPLE = FE_threshold(FEs, 5)
WITHIN_GATE_PEOPLE


def find_partners(searchee_name, degree_of_symmetry):
  searchee_skills = list(filter(lambda person: person['Name'] == searchee_name, FE_analysis))[0]['L matrix']

  suited_partners = {}
  for peep in FE_analysis:
    if peep['FE value']!=None and peep['Name']!=searchee_name:
      peep_skills = peep['L matrix']
      
      KL = get_KL(searchee_skills, peep_skills)
      DOS = get_symmetry(searchee_skills, peep_skills, degree_of_symmetry)
      
      suited_partners[peep['Name']] = KL + DOS
  return dict(sorted(suited_partners.items(), key=lambda item: item[1]))
# web3-squad-voodoo

One of the key aspects to Active Inference framework is autopoietic creation and maintenance of a complex system. This could be leveraged for team formation in research environments.

A clear objective: finding lab members to involve for synergistic collaboration.

Stepwise simulation :

At t = 0, Proposer comes with a project and establishes required skill-set distribution, which is matched with preference distribution of lab members concurrently on a coordinate space of homogeneous abscissa (discrete skills) by geometric transposing. For instance, here, area under the green curve (overlap) is directly proportional to collaboration fit index for individual agents and the project [fig a].
At t when group strength just turns > 1, we calculate the stability of the formed system by calculating its marginal likelihood of research objective (o) and overlapping skill-set (s) [in equation i] for involved researchers.


Since, computing marginal probabilities is often computationally intractable, we do some neat math to find a way around by introducing logarithms and negating it (a corollary to surprise minimization in ActInf theory, eqn. ii).

Using Jensen’s inequality identity to establish an upper-bound (eqn iii).
Free Energy (F). Optimization problem for the system’s stability is now minimizing the Free Energy. This process is iterative on state change (like adding or removal of a member).

Now, for a functioning research niche we need to form sub-groups. This could be done by algorithmic permutation over the possible spectrum of configurations, from perfectly symmetrical sub-groups (each with the same number of people) to perfectly asymmetrical (each with different number). The Free Energy quantized stability quotient for concurrent formation and existence is depicted in Fig. b. This “selection of project groups” is enacted by Humans (via Affordances, in Roles), however can be considered as a policy selection from the organizational scale (whether university or DAO). In this case the set of possible teams (policy evaluation at lab scale over team composition) is the combinatorics related to all possible assignment affordances of eligible participants into project-specific roles. As this is a discrete and finite space of affordances, it may be possible to specify and execute this group formation policy selection exactly.
Does this require/imply a lab-level generative model?
Participant (entity-level) generative model, and interacting Organizational generative models?
Nested models (Ecosystem → Institution → Organizational Unit → Project → Team → Individual) and multiscale policy selection.

By
Amit Singh (metamyth)
Researcher at Active Inference Lab
Twitter: https://twitter.com/not_amyth?t=BSpbbssQAIkrRAgg1ZTUIQ&s=09

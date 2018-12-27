+++
date = "28 Dec 2018"
draft = false
title = "Syllabus"
slug = "syllabus"
+++

<div class="printing"><a href="/docs/syllabus.pdf">PDF for Printing</a></div>

**CS 4501/ECON 4559: _Markets, Mechanisms, and Machines_**  
University of Virginia, Spring 2019

**Meetings:** Tuesdays and Thursdays, 9:30-10:45AM, MEC 213.

**Intructors:** <a href="http://people.virginia.edu/~dn4w/">Denis Nekipelov</a> and
<a href="https://www.cs.virginia.edu/evans">David Evans</a>.

**Prerequisites:** Computer Science majors should register for the CS
4501 course, which has CS 2150 as a prerequisite. Economics majors
should register for the ECON 4559 course, which has ECON 3010 or 3110
and ECON 3720 or 4720 as a prerequisite.


**Course description:**

Many modern systems that were designed to help people ranging from
Internet search platforms to car navigation or restaurant recommendation
apps rely on learning from its user past behavior to improve future user
experience. They use these past data to make inferences regarding the
choices that users will make in the future. The building blocks of these
system include Machine Learning tools for prediction, Econometrics
techniques to identify what causes humans to make particular choices and
algorithms from Computer Science to provide fast and efficient matchings
between users and their choices. Users in these systems can interact
with each other that requires concepts from Game Theory to analyze their
behavior and be able to forecast the evolution of these systems in the
short and long run. Finally, users may care about how exactly these
systems use and exploit their personal information to make those
predictions and inferences. The analysis of user privacy combines the
concepts from Economics of Information and formal privacy concepts from
Computer Science Theory while concepts from Cryptography can be used to
design systems that are protected from privacy breaches.

This course will present a collection of topics from Economics and
Computer Science that constitute the building blocks of modern
user-facing electronic systems. Many examples will come from modern
digital advertising platforms that have both created huge success in
user reach and effectiveness for advertisers and, at the same time, have
generated a trail user privacy concerns.   

**Evaluation:** Course performance will be evaluated based on
the final exam that will account for 50% of the final grade and 4 course
projects that account for another 50%. Course projects will be based on
the analysis of data from real electronic platforms (for
example, <a href="https://webscope.sandbox.yahoo.com/">Yahoo!'s Webscope
data</a>). For most assignments, students will be grouped into teams of
two or four students, including students in both the CS and ECON
sections of the course in each team. This assignment will emulate the
work of real interdisciplinary teams at leading companies. It will be
the team's responsibility to distribute the tasks, communicate with each
other and explain in the project report what part of the project was
completed by what team member. 

**Outline of topics:** (this is very preliminary, and likely to
change before the semester starts)


<b>Week 1:</b> Causal inference: concepts, models and tools
<blockquote>
Causal inference vs. prediction. Treatment effects. Treatment effects in
heterogeneous population. Endogeneity and instrumental
variables. Measuring consumer responses and ROI on advertising as
treatment effect. Other notions of causality: Granger causality and
Pearl's idea of causality.
<p>
<b>Reading:</b> Rubin, Donald B. "Causal inference using potential outcomes:
Design, modeling, decisions." Journal of the American Statistical
Association 100.469 (2005): 322-331.<br>
Blake, Thomas, Chris Nosko, and Steven Tadelis. "Consumer heterogeneity
and paid search effectiveness: A large-scale field experiment."
Econometrica 83.1 (2015): 155-174.
</blockquote>
<p>
<b>Week 2:</b> Machine learning and prediction
<blockquote>
The concept of the learning machine and the concept of risk
minimization. Empirical risk minimization. Types of problems of
Statistical learning theory: pattern recognition, regression and density
estimation. Examples and properties of common algorithms for statistical
learning. Click prediction algorithms, Google's DoubleClick and AdSense.
<P>
<b>Reading:</b> Vapnik, Vladimir. The nature of statistical learning
theory. Springer science & business media, 2013. (Chapter 1)
</blockquote>
<p>
<b>Weeks 3-4:</b> Matching problems
<blockquote>
Introduction to graph theory. Directed and undirected graphs. Graph
degree. Paths and cycles on graphs. Sorting and searching
algorithms. Tree graphs. Matching on bipartite graphs. Common algorithms
for matching on bipartite graphs.
<p>
<b>Reading:</b> Norman L. Biggs, "Discrete Mathematics", Oxford University
Press. (Chapters 15-17)
</blockquote>
</p><p>
<b>Weeks 5-6:</b> Competitive advertising markets
<blockquote>
Introduction to game theory. Games of complete information. Notion of
Nash equilibrium. Games of incomplete information. Notion of Bayes-Nash
equilibrium. Discrete and continuous games. Auctions. Common types of
auctions by design of allocation and payment rules. Multi-unit
auctions. Auctions used for online advertising. Generalized second price
auction and Vickrey-Clarke-Groves mechanism. Recent developments in
online advertising auctions.
<p>
<b>Reading:</b> Gibbons, Robert. Game theory for applied economists. Princeton
University Press, 1992. (Chapters 1 and 3)<br>
M. Gentry, T. Hubbard, D. Nekipelov, H. Paarsch, "Structural
Econometrics of Auctions". MIT Press 
</blockquote>
</p><p>
<b>Week 7:</b> From Game theory to Algorithmic Game Theory
<blockquote>
Approximating best responses and utility guarantees. Possibility (and
impossibility) of implementation of Nash equilibria. Approximating Nash
equilibria.
<p>
<b>Reading:</b> Jason Hartline, "Mechanism Design and Approximation".
http://jasonhartline.com/MDnA (Chapter 1)
</blockquote>
</p><p>
<b>Week 8:</b> Introduction to Economics of Information 
<blockquote>
Informational content of Nash equilibria. Competition and user
information. Information and user privacy. Resent evidence on behavioral
response (and non-response) to changes in privacy.
<p>
<b>Reading:</b> Hal Varian, "Economics of Information Technology"
http://people.ischool.berkeley.edu/~hal/Papers/mattioli/mattioli.html<br>
Tucker, Catherine E. "The economics of advertising and privacy". International journal of Industrial organization 30.3 (2012): 326-329. 
</blockquote>
</p><p>
<b>Week 9:</b> Formal concepts of privacy
<blockquote>
Privacy and privacy threats. Risk of disclosure and a concept of
adversarial attacks. K-anonymity and related concepts. Analyzing
K-anonymous data. Differential privacy. Differential privacy and
robustness. Differential privacy and Machine learning.
<p>
<b>Reading:</b> Lambert, Diane. "Measures of disclosure risk and harm." Journal
of Official Statistics 9.2 (1993): 313.<Br>
Dwork, Cynthia. "Differential privacy: A survey of results."
International Conference on Theory and Applications of Models of
Computation. Springer, Berlin, Heidelberg, 2008.
</blockquote>
</p><p>
<b>Week 10-11:</b> Cryptography and data protection
</p>
<p>
<b>Week 12:</b> Privacy-aware mechanism design
<blockquote>
Differential privacy as condition on strategic responses of
agents. Differentially private prediction of user choices. Designing
mechanisms with formal privacy guarantees.
<p>
<b>Reading:</b> Nissim, Kobbi, Claudio Orlandi, and Rann
Smorodinsky. "Privacy-aware mechanism design." Proceedings of the 13th
ACM Conference on Electronic Commerce. ACM, 2012.<br>
Dwork, Cynthia, and Aaron Roth. "The algorithmic foundations of
differential privacy." (Chapter 10)
</blockquote>






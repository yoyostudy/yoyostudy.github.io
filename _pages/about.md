---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
I'm a 1st year PhD student in Computer Science at Simon Fraser University, fortunate to be supervised by Dr. [Linyi Li](https://cs.sfu.ca/~linyi/) in the [Trustworthy AI (TAL) Lab](https://sfu-tai.github.io/). 

My primary interest lies in the theoretical foundations of model structure, interpretability, learning algorithms, and reinforcement learning. At the same time, I aim to translate these ideas into practice through socially responsible AI, with applications in red teaming, safety, and AI governance.

# 🔥 News
- *2025.06*: &nbsp;🎉🎉 Participated in a hackathon with developers from my team at SAP about AI model governance. 

# 📝 Publications 

<div style="display:flex;gap:12px;align-items:flex-start;">
  <img src="../images/autored.png" alt="AutoRed" style="width:200px;border-radius:6px;object-fit:cover;">
  <div>
    <strong><a href="https://ieeexplore.ieee.org/abstract/document/10825267" target="_blank">AutoRed: Automated Attack Scenario Generation Framework for Red Teaming of LLMs</a></strong><br>
    <strong>Zhe Wang</strong>, M. A. Tayebi<br>
    <em>IEEE BigData 2024</em><br>
    We present <strong>AutoRed</strong>, a framework that generates diverse adversarial prompts to evaluate LLM defenses.
  </div>
</div>


<!-- # 🎖 Honors and Awards
- *2017.10* **First Prize**, Zhoushan division of the Zhejiang Provincial High School Mathematics Olympiad. -->

# 📖 Educations
- *2025.09 – 2029.8* (Expected), Ph.d., Computer Science at Simon Fraser University
- *2022.09 – 2024.05*, M.Sc., Computer Science at Simon Fraser University
- *2018.09 – 2022.07*, B.Sc., Mathematics and Applied Mathematics at The Chinese University of Hong Kong, Shenzhen

# 💬 Invited Talks
- *2025.06*, _The Art of LLM Evaluation_, AI lunch and learn at SAP Canada, Vancouver office. 

# 💻 Internships
- *2024.09 - 2025.08*, Data Scientist Intern, SAP, Canada.
- *2023.07 - 2023.09*, Machine Learning Researcher Intern, Hanglok-Tech, China

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
I'm a 2nd year PhD student in Computer Science at Simon Fraser University, fortunate to be supervised by Dr. [Linyi Li](https://cs.sfu.ca/~linyi/) in the [Trustworthy AI (TAI) Lab](https://sfu-tai.github.io/). 

I am broadly interested in large language models. My current research interests include:

- **Looped models & model depth** ([blog](s5_blog_preview_conclusion.html), [slides](files/astrm_slides.pdf))
- **Test-time training & continual learning**
- **Curriculum learning** ([blog](s5_blog_preview_conclusion.html), [slides](files/astrm_slides.pdf))
- **LLM alignment:** red teaming ([paper](https://ieeexplore.ieee.org/abstract/document/10825267)), potential threats that frontier LLMs may pose to society

# 🔥 News
- *2026.11*: Dumped my first blog on model depth: [When Attention Learns Group Composition](s5_blog_preview_conclusion.html).
- *2026.01*: Completed PhD coursework and breadth exam requirements.
- *2025.06*: &nbsp;🎉🎉 Participated in a hackathon with developers from my team at SAP about AI model governance.

# 📝 Publications 

<div style="display:flex;gap:12px;align-items:flex-start;">
  <img src="../images/autored.png" alt="AutoRed" style="width:200px;border-radius:6px;object-fit:cover;">
  <div>
    <strong><a href="https://ieeexplore.ieee.org/abstract/document/10825267" target="_blank">AutoRed: Automated Attack Scenario Generation Framework for Red Teaming of LLMs</a></strong><br>
    <strong>Zhe Wang</strong>, M. A. Tayebi<br>
    <em>IEEE BigData 2024</em><br>
    We present <strong>AutoRed</strong>, a red-teaming framework that proactively generates adversarial prompts to challenge LLMs’ refusal strategies and safety alignment.
  </div>
</div>

<!-- # 🎖 Honors and Awards
- *2017.10* **First Prize**, Zhoushan division of the Zhejiang Provincial High School Mathematics Olympiad. -->

# 📖 Educations
- *2025.09 - Present*, Ph.D., Computer Science at Simon Fraser University
- *2022.09 - 2024.05*, M.Sc., Computer Science at Simon Fraser University
- *2018.09 - 2022.07*, B.Sc., Mathematics and Applied Mathematics at The Chinese University of Hong Kong, Shenzhen

# 💬 Talks & Presentations
- *2026.10*, Paper Forward Session, SFU: _Ongoing work on looped models_ ([slides](files/astrm_slides.pdf))
- *2026.09*, RBC office: _Ongoing work on looped models_ ([slides](files/astrm_slides.pdf))
- *2025.06*, AI Lunch and Learn, SAP Canada, Vancouver office: _The Art of LLM Evaluation_

# 📝 Blog
- [When Attention Learns Group Composition](s5_blog_preview_conclusion.html)

# 💻 Internships
- *2026.01 - 2026.09*, Mitacs Research Intern, RBC Borealis, Canada.
- *2024.09 - 2025.08*, Research and Development Intern, SAP, Canada.
- *2023.07 - 2023.09*, Machine Learning Research Intern, Hanglok-Tech, China.

# 🖋️Services
- Conference Reviewer: WWW, EMNLP

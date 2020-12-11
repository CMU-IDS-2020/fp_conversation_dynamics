# CMU Interactive Data Science Final Project
**Project title**: Tracing Interdisciplinary Design Conversations

* **Online URL**: https://cmu-ids-2020.github.io/fp_hu_giesa_erdolu/
* **Team members**:
  * Contact person: kigesa@andrew.cmu.edu
  * eerdolu@andrew.cmu.edu
  * meijieh@andrew.cmu.edu
* **Track**: Narrative
* **Link to video demo**: https://drive.google.com/drive/folders/18pRqbyy4Dg9TUiT8VgUD3CHqKHcBQw3w
  * For the best resolution, please switch to 1080HD or watch the video in full screen mode.
* **Running Instructions**:
  * Click the online URL above and start navigating the interactive narrative.
  * We recommend 50% or 67% zoomed out view on a Chrome browser.
  * You will find tips on how to interact with the visualizations. 
  
 ![imageHere](ng_mfk_2.png)

## Abstract

With the increasing convergence of digital and architectural practices, a common interdisciplinary encounter of today is between architects and tech designers. Tech companies, startups, designers, and entrepreneurs are increasingly interested in homes, offices, infrastructures, and cities as sites of deployment; and architecture offices and architects in return engage with software, sensors, robots, and devices as their instruments. The mutual interest in each other's work and artifacts start to bring these two figures more often in conversations, debates, or collaborations within labs or projects. Because of different knowledge backgrounds and discourses, an interdisciplinary conversation can at times involve low levels of engagement as well as exchanges and gaps. Producing insights on these between the disciplinary discourses of architects and tech designers is a crucial first step towards constructing a more productive communication between the two groups, which could help to produce distinct perspectives, artifacts, and knowledge out of their collaborations. This paper reports on a case study of an interdisciplinary conversation between two architects and a tech designer. Within the case study, we investigated the engagement, exchanges, and gaps between these actors’ disciplinary discourses by text processing and visualization. By doing this through text processing and visualization, we also explored the potential of these methods in understanding these conversational dynamics. The case study and visualizations revealed that, even though the architects and the tech designer engage through a sharing and exchange across their discourses, there are issues in the qualities of that sharing and exchange.

## Work distribution

### Discussions on Scope 

Early on, we got together and brainstormed project ideas, soon settling on the analysis of interdisciplinary design conversations. After discussing affordances and limitations of analyzing multiple conversations, we decided that the ability to dive deeply into the text was of particular importance to our work, and would fit better into our mixed-method approach of computational and qualitative analysis of conversations. So, we chose to focus on a single conversation. We were interested in the encounters between architects, designers, and tech designers. So we found a few potential conversations that involve these disciplinary figures. As mentioned, qualitative evaluation was an important part of our work. So we each watched the conversation, and got together over zoom to discuss where we might be able to draw out interesting insights through visualization. Based on these discussions, we prepared our proposal. These were all collective efforts where each member took equal roles.

### Designing the framework and study

To begin the process, we briefly looked at background literature in linguistics, computational linguistics, and text visualization in order to understand analytical approaches to conversation analysis. Parallel to that, we identified a list of questions to guide the study. To investigate these questions, we operationalized key dimensions in a conversation based on linguistics and other relevant literature. This was also important to frame the text processing part of the project. A few of the dimensions required us to identify what we called as “disciplinary words” in the conversation. That required each member to go through the text again, and we had to have a few meetings to reach a consensus on these words.

This was followed by discussions on the technical framework. NLTK / Python for text processing was a no brainer for us. For visualizations, we debated Streamlit versus D3.js, and we ended up choosing HTML / CSS / D3.js both for its capabilities as well as for a learning opportunity for ourselves. Each member had to do work to learn more about D3.js. These were also collective efforts where each member took equal roles.

### First Round of Work 

As the technical framework was ready, we had a few design discussions on the type of visualizations that would be effective to visualize the dimensions we identified. We first decided on bar graphs to create histograms of the conversations. We also felt network graphs would be especially meaningful in showing relations between actors and words and between actors, or showing levels of engagement and exchange when one conceptualizes a conversation as a connection between actors. These networks also opened potentials for interaction by highlighting weights or frequencies of use, or degrees of connections, sharing or exchange between nodes (in our case, words or actors). We also felt a tree diagram would be a good way of highlighting word categorizations. Buttons to switch layers, dragging through timelines, and sliders were pretty effective for us to represent several layers of information within this set of visualizations. 

We worked on the details of those diagrams through sketches together with the structure of the narrative, and where each diagram sits. Then we shared the work based on the dimensions and by different parts of text processing. Initially, Katherine worked heavily on the text processing part and producing JSONs and less on the visualizations, while Emek and Meijie focused on developing the draft website for interactive narrative by HTML / CSS / Javascript, and less on text processing. This is how we reached the design review. After the text processing was finished, all three members focused on producing the visualizations and we started to push the work towards completion.  

### Final production

We collectively discussed the analysis and findings of the study by reflecting on the visualizations. After that, final production began. Throughout this stage, we routinely met over zoom. These meetings were used to help each other overcome learning obstacles with the d3 library and to update each other about the visualization process. In these meetings we also discussed design decisions such as color and formatting, and interaction potentials such as the effectiveness of zooming or using a tooltip. Finally, in these discussions, we were keenly aware of the narrative and the ways that narrative and visualization would best augment each other. In the final production, Emek took the lead on network graphs and interactions along with narrative writing and producing the video. Meijie worked with bar charts and interactions; and Katherine worked with the final part of text processing, visualizations, and interactions. This final production part was an even share of executing the parts of the interactive narrative. 

## Deliverables

### Proposal

- [ ] The URL at the top of this readme needs to point to your application online. It should also list the names of the team members.
- [ ] A completed proposal. The contact should submit it as a PDF on Canvas.

### Design review

- [ ] Develop a prototype of your project.
- [ ] Create a 5 minute video to demonstrate your project and lists any question you have for the course staff. The contact should submit the video on Canvas.

### Final deliverables

- [ ] All code for the project should be in the repo.
- [ ] A 5 minute video demonstration.
- [ ] Update Readme according to Canvas instructions.
- [ ] A detailed project report. The contact should submit the video and report as a PDF on Canvas.

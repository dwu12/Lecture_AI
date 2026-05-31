# Lecture Transcription: World Models and the Future of AI
## Professor Yann LeCun - Applied Mathematics Webinar

---

## Introduction

**Professor LeCun:** Images that really is focusing on developing this thing. We're still doing research, we're open sourcing, we're publishing, we're just getting started, we're hiring too and basically solve all the problems in the real world that AI currently really is not so good for. And the hope is that, you know, maybe hierarchical JEPA Hierarchical planning will allow us to train sort of universal causal models of any complex phenomenon and be the basis for you know any intelligent system in the future and thank you very much.

**Moderator:** Thank you very much Professor LeCun. We can thank Professor LeCun. And now perhaps some questions.

---

## Q&A Session

### Question 1: Mathematics and AI Research

**Moderator:** Okay, thank you. Okay, I have a first question. The fact that you accepted the invitation and applied mathematics webinar is my sense the best proof of the importance of this science. Do we think that there are enough mathematicians dedicating their research to AI, or do we think that AI needs more mathematicians?

**Professor LeCun:** Yes. So, you know, my academic position is with the Courant Institute, which is actually since September is a school within New York University. It's a school that regroups mathematics, pure and applied. Courant, of course, is famous for applied mathematics, computer science and data science. Okay, it's a standalone school. It used to be part of the arts and science school, but now it's a separate school, which basically is because of the importance of both mathematics, particularly applied mathematics, computer science, particularly with AI and data science, which is really applied AI, if you will, right?

So NYU has decided that this whole field is so important that it should have a dedicated school separate from, you know, the law school and the business school and the arts and science and the engineering school. I've been personally, because being part of Coop Although I'm part of the computer science department, I've had a lot of interactions and contacts and even students from applied math. And for many years, I was on the science advisory board of the Institute for Pure and Applied Mathematics at UCLA.

And I've always tried to bring in interest from mathematicians to machine learning and deep learning in particular because the mathematical problems they are really in my opinion very interesting but also very complicated and traditionally people interested in machine learning who have you know a bit of a interest and background in mathematics have focused in the past on simpler machine learning paradigms think like kernel methods support vector machines Bayesian inference and things like that where the theory is easier to write neural nets are messy and so theorists have reluctantly approached deep learning because it's very it's very complicated right the functions we optimize are non-convex.

So you can't prove anything. We use stochastic gradient, which for an optimization person is really, really hard to model the behavior of. All the traditional tools in optimization and criteria that we use to analyze optimization algorithms go out the window because in machine learning we don't care about precise optimization because that creates overfitting.

Even statisticians and probabilists are baffled by a phenomenon called double descent. So traditionally every textbook in statistics tell you if you try to fit a function to a bunch of points you don't want too many parameters because your system is going to overfit, right? It's going to, you know, if you have 10 points and use an 11 degree polynomial, your polynomial is going to go through every point exactly but between the points it's going to go completely wild, right?

So as a, as a approximation for noisy signal for functional approximation you need models with a small number of parameters that argument turns out to be completely false empirically initially okay and now we need to understand this theoretically so neural nets are way over parameterized the number of parameters in neural nets is enormous compared to the amount of training samples yet those systems generalize pretty well they interpolate quite well they even extrapolate.

And that's a phenomenon, an empirical phenomenon called double descent, where the error on the separate test set of a model is going to go down as you increase the number of training samples, the number as you increase the power of the model, like the degree of the polynomial, the number of parameters in your neural net, then it's going to increase, okay, and this is where overfitting occurs. But then as you increase the power of the model, the number of parameters, it actually decreases again, at least if you regularize it properly, and it may actually go to zero.

So this phenomenon is a little baffling. There are a few intuitive explanations for it. I have had one for a long time, but it's now completely understood theoretically. And then, you know, there's more specific properties, I think, where mathematics.

So I didn't talk much about energy-based models. There's a lot of really interesting research and mathematics I hope to do there, which is basically. Okay, let's say you want to estimate the dependency between two variables, two scalar variables, and I give you a bunch of data points, okay, and the dependency between the two variable x and y is not a function because there might be multiple values of y for a given x that are in your, you know, in your in your samples.

How do you capture this dependency between x and y? So of course you could say, well, I'm going to learn a joint distribution between x and y, but that may actually be extremely difficult, particularly in high dimension. Estimating distribution in high dimension is basically impossible and intractable. You have to represent it by an energy function, you take the exponential minus and you normalize and the normalization constant is intractable, it's like the partition function in physics, you don't know how to integrate complex energy function, so it's basically intractable.

Okay, so how about something that's simpler, and that's energy-based model which consists in Can I learn a contrast function that will give me which is scalar scalar outputs, right? And it takes a pair of X and Y and if the pair of X and Y is in the region of high data density it gives me a low value, let's say zero. And if I move away from the manifold of data, if you want, the value of this scalar function increases.

Okay? So it's basically a contrast function, an energy function, that tells me you are on the data manifold or you are away from it. And that's all I need to capture the dependency between two variables. It's a much better way actually, a much simpler way also of capturing dependencies than probabilistic modeling. There's a lot of theory to do about this.

But, okay, it's missing. A long answer, I'm sorry.

**Moderator:** There is NASA from that, Rafit, can you, how can we do, Rafit, can you?

**Assistant:** I already asked him to unmute Nassaf.

**Professor LeCun:** Okay,

**Assistant:** please unmute your, it's

**Professor LeCun:** okay, sorry.

**Assistant:** correct now.

---

### Question 2: AI Deployment in Safety-Critical Industries (Nuclear Engineering)

**Nuclear Engineer (Speaker D):** I don't know if you can hear me.

**Professor LeCun:** Yes, yes I can.

**Assistant:** Yeah,

**Professor LeCun:** can

**Nuclear Engineer:** Perfect. Perfect. Thank you. So thank you very much for the talk, Professor LeCun. I found the distinction that you made between simple action prediction and true planning with a world model especially interesting and also your point that the next wave, if I can say, of AI has to deal with more dimension high dimensional noisy data rather than just tokens.

My main question is about deployment in safety critical industries like space nuclear. I'm actually a nuclear engineer in Paris in within the R&D team what we call the DEC, the Digital Excellence Center. So that part resonated a lot with me because our reality is exactly this, actually, what you described, sensory streams, inspection images, maintenance data, etc.

So my question is, to make a link with your slides, you argue that world models should not be digital twins and you also take a fairly strong position against generative models like like chat GPT or whatever, but but in nuclear physics-based models explicit simulators or just how to say it the uncertainty quantification are not optional you know so we are judged not only on performance but on validation and auditability etc.

So how do you see JEPA style or I'm not a specialist so excuse me about that but the the action conditioned world models that you describe how do you see them interfacing with the first principles engineering models in domains like nuclear actually do you say do you see them as replacing digital twins or rather um how to say it as a higher abstraction layer on top of them and for planning for anomaly or accident anticipation etc etc?

**Professor LeCun:** Yeah. Yeah, so I mean what we anticipate and this is something of course We think about a lot in the context of Amilabs, which by the way is pronounced the French way, Amilabs.

**Moderator:** I mean,

**Professor LeCun:** okay. And we think about that a lot because we think that's basically our... You know, our first business and customers would be the control of complex systems such as a power plant, possibly a nuclear power plant.

**Assistant:** Okay.

**Professor LeCun:** by, you know, training a phenomenological model of the system that, you know, allows to plan for sequence of intervention, you know, for any particular situation.

Now, you can train this with real data. You can also pre-train it with synthetic data that's obtained from from you know digital twin simulation but then completed with real data which probably makes it more realistic if you want and then the system can also kind of fine-tune itself as it goes you know it makes a prediction at every time step right so it can then observe the result and say oh I need to adjust my model because you know I see a discrepancy between what I predicted and what actually occurred.

I mean this is similar to what people do in you know model predictive control you know procedures like IDICOM and things like that so um so yeah I mean that's probably or or core core business is that you know before we have reliable models that you know would be usable for nuclear power control it might take a while but but but that's kind of the hope frankly.

**Follow-up Moderator:** Okay, okay, that's interesting. Okay, thank you. Just to add a little bit of information in nuclear, we are trying to simplify the process of building nuclear power plant, etc. So we have what we call SMRs. I don't know if you have heard about them, which are small modular reactors, a type of, let's say micro modular reactors.

So with your JEPA style models, I think there is a potential collaboration that you that you could benefit from. Yeah, it could be something useful. be... Yeah, yeah, I mean, thank it.

**Professor LeCun:** So you again.

**Follow-up Moderator:** It was very interesting to follow you. Thank you.

**Professor LeCun:** Thank you.

---

### Question 3: LLMs and the "Spark of Intelligence"

**Moderator:** Is there another question?

**Assistant:** There is a question in the chat, Nabil.

**Moderator:** I don't see it. Can you?

**Assistant:** Yes,

**Moderator:** Ah, yes.

**Assistant:** Mohammed Alwadi.

**Professor LeCun:** Yes.

**Moderator:** Mohammed, if you are with us, you can ask them, ask Dr. LeCun directly, Mohammed.

**Assistant:** Yes, can you hear me?

**Professor LeCun:** Yes,

**Moderator:** Yes.

**Professor LeCun:** we hear you.

**Moderator:** Yes.

**Mohammed Alwadi:** Okay, yeah, I'm very happy to see you live. My question is a recurring one. It's about how the spark of intelligence occurred suddenly in a system that's only conceived to predict the next word. It's based on language, yet at the same time we have the impression it's exhibiting real intelligence at times. And it's baffling. I was wondering whether you had an explanation on when and how that happened. And thank you.

**Professor LeCun:** Sure. There is only two or three domains where LLMs exhibit sort of baffling intelligence, if you want.

**Mohammed:** Yes.

**Professor LeCun:** And those are computer code generation, mathematics, and perhaps law okay so legal text and things like that and the reason is these are domains at least for the first two certainly where the language itself is a kind of substrate for reasoning right when we do mathematics the the simple manipulation of symbols gives us sometimes results that we did not expect right so the the reasoning can be basically supported by the language itself and there's a similar phenomenon when you write code where where where you know you may have a you know some idea about how to organize the code but when you start writing it it kind of crystallizes and the simple fact that you're writing the code sort of makes your your your concepts clearer in in many ways at least if you're a good computer scientist.

So you can imagine that for those two domains, manipulating symbols, which is what LLMs do, can help with reasoning. And in fact, you know, the way those systems do math and code is that they generate lots and lots of different sequences of symbols and then they have another network that kind of selects the best ones. And if it's code generation, you can just test whether the code works and then iterate, which is what code generation takes so long.

If it's mathematics, you know, you arrive at a result and, you know, you can try to prove it, right? You can verify is a result, you know, is true or not, you know, with perhaps numerical examples or something like that.

So those are two domains where there is self-adjustment because you can verify if an answer is correct or not. And the reasoning... substrate is the language itself.

Most of human reasoning and intelligence has nothing to do with language. Okay, it has to do with our experience of the real world, but it's not language-bound or it's not even helped by language. So it's certainly true of animals, right? They don't have language, at least not to the same extent.

So, okay, so that's only a partial answer to your question. So the type of intelligence that we observe in LLMs is very narrow, is very restricted. And the reason why they seem to be intelligent by answering all the questions we ask them is a bit of an illusion. They basically do retrieval, okay.

So those systems are not particularly intelligent, but they are extremely good at accumulating enormous amounts of knowledge and then regurgitating that knowledge at the right time and maybe adapting it in minor ways, okay. But they're not that smart. In fact, they do, they give you really stupid answers sometimes, right.

There is a story that has circulated recently on social networks where someone said, Okay, I need to wash my car. I need to get my car washed. And the car wash place is 100 meters from my house. Should I walk?

**Moderator:** Yeah.

**Professor LeCun:** And most LLMs, you know, chat GPT, the latest one, Claude, you know, all of those, meta AI, they say, no, you should, I mean, yes, you should work because it's only 100 meters away, like not realizing you're not going to have your car with you, okay. The only one that answers correctly is Gemini from Google, but it's very likely that the reason it answers correctly is because in the last few weeks it was fine-tuned with the correct answer. It was to detect that question and answer it correctly.

I was made fun of in the past year or two because on an interview with Lex Freedman, a pretty popular podcast, I said, look, you know, LLMs don't have any physical need. If you put an object on the table and you push the table, you know the object will move with the table, right? That's kind of...

**Assistant:** Right.

**Professor LeCun:** obviously physical intuition but if you have if you ask you know chat GPT or one of its successor it's not going to be able to you know understand the physical reality behind this and make the right prediction and of course six months later like so if you ask a question to ChatGPT at that time it would not answer correctly but if you ask the next version of ChatGPT it did answer correctly and the reason is it's not that it you know understood physical reality any better it's that it was explicitly fine-tuned to answer that particular question because as soon as as you know the podcast was published hundreds of people actually asked the question to ChatGPT to verify the idea and so it was incorrect and so that became part of the training set now and and you know OpenAI integrated that that question in the fine-tuning set and of course you know any particular question that you ask in a system you can fine-tune it to answer it correctly but it's retrieval it's like those students you have in your class that you know do rote learning but don't really have a deep understanding of the underlying mathematics right.

**Nuclear Engineer:** All right. Thank you.

---

### Question 4: Should Humanity Be Afraid of AI?

**Professor LeCun:** If there is no other questions, I have perhaps, est-ce que tu vois d'autres questions Rafiq à la fin de l'université?

**Moderator:** Yes, I have a question. Thank you, Professor LeCun, for this nice lecture. In this lecture, you focus especially on human interests in artificial intelligence. My question is in that direction. Should humanity be afraid of AI in the future?

**Professor LeCun:** Yeah, it's a very common question. Okay, we should be careful about AI. Because it's, you know, powerful technology with a big impact, we have to make sure the impact is beneficial to all of us. But like society is used to doing this. I mean, we do this with every new technology that comes out. We have, you know, particularly if it's consumer facing, we have regulation to make sure it's safe and things like that, right?

Or, you know, particularly for things like nuclear power. But OK, but we should not be afraid of it for the reasons that a lot of people are claiming we should be afraid of it. So the idea somehow that AI is qualitatively different from other technology and is intrinsically dangerous at the research level, that's just completely false. That's just ridiculous, in fact.

It's basically a cult that started in Silicon Valley. It's called effective altruism of people who... are claiming to kind of try to make long-term prediction about the future of humanity and basically they focus on the idea that if a technology is potentially dangerous you know or powerful necessarily is dangerous then we should stop working on it I mean it's just images that really is focusing on developing this thing. We're still doing research, we're open sourcing, we're publishing, we're just getting started, we're hiring too and basically solve all the problems in the real world that AI currently really is not so good for.

And the hope is that, you know, maybe hierarchical JEPA Hierarchical planning will allow us to train sort of universal causal models of any complex phenomenon and be the basis for you know any intelligent system in the future and thank you very much.

---

## Closing

**Moderator:** Thank you very much Professor LeCun. We can thank Professor LeCun. And now perhaps some questions.

---

*End of Transcription*

---

### Speaker Identification Summary:
- **Professor LeCun (Speaker A):** Main lecturer, Professor Yann LeCun from NYU/Courant Institute
- **Moderator (Speaker B):** Session moderator/questioner
- **Assistant/Technical (Speaker C):** Audio/technical assistant helping with participant unmute
- **Nuclear Engineer (Speaker D):** Nuclear engineer from Paris DEC, asking about safety-critical deployment
- **Follow-up Moderator (Speaker E):** Continuing discussion on nuclear applications
- **SMR Expert (Speaker F):** Follow-up question about Small Modular Reactors
- **Question Facilitator (Speaker G):** Moderator facilitating questions
- **Chat Assistant (Speaker H):** Assistant locating questions in chat

---

*Note: This transcript contains some repeated sections (lines 316-325 duplicate content from earlier), likely due to ASR processing artifacts. Original content preserved as-is.*
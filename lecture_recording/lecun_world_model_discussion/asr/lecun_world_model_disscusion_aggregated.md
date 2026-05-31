Speaker A:  images that really is focusing on developing this thing. We're still doing research, we're open sourcing,
Speaker A:  we're publishing,
Speaker A:  we're just getting started,
Speaker A:  we're hiring too and basically solve all the problems in the real world that AI currently really is not so good for.
Speaker A:  And the hope is that, you know, maybe hierarchical JEPPA
Speaker A:  Hierarchical planning will allow us to train sort of universal causal models of any complex phenomenon and be the basis for you know any intelligent system in the future and thank you very much.
Speaker B:  Thank you very much Professor Lacan.
Speaker B:  We can thank Professor Lacan.
Speaker B:  And now perhaps some questions.
Speaker A:  Sure.
Speaker B:  Okay, thank you.
Speaker B:  Okay,
Speaker B:  I have a first question.
Speaker B:  The fact that you accepted the invitation and applied mathematics webinar is my sense the best proof of the importance of this science.
Speaker B:  Do we think that there are enough mathematicians dedicating their research to AI,
Speaker B:  or do
Speaker A:  No.
Speaker B:  we think that AI needs more mathematicians?
Speaker A:  Yes.
Speaker A:  So,
Speaker A:  you know, my academic position is with the Courant Institute, which is actually since September is a school within New York University.
Speaker A:  It's a school that regroups mathematics,
Speaker A:  pure and applied.
Speaker A:  Courant, of course, is famous for applied mathematics,
Speaker A:  computer science and data science.
Speaker A:  Okay, it's a standalone school.
Speaker A:  It used to be part of the arts and science school, but now it's a separate school, which basically is because of the importance of both
Speaker A:  mathematics, particularly applied mathematics,
Speaker A:  computer science,
Speaker A:  particularly with AI and data science, which is really applied AI,
Speaker A:  if you will,
Speaker A:  right?
Speaker A:  So NYU has decided that this whole field is so important that it should have a dedicated school separate from, you know, the law school and the business school and the arts and science and the engineering school.
Speaker A:  I've been personally,
Speaker A:  because being part of Coop
Speaker A:  Although I'm part of the computer science department,
Speaker A:  I've had a lot of interactions and contacts and even students from applied math.
Speaker A:  And for many years, I was on the science advisory board of the Institute for Pure and Applied Mathematics at UCLA.
Speaker A:  And I've always tried to bring in...
Speaker A:  interest from mathematicians to machine learning and deep learning in particular because the mathematical problems they are really in my opinion very interesting but also very complicated and traditionally people interested in machine learning who have you know a bit of a interest and background in mathematics have focused in the past on simpler
Speaker A:  machine learning paradigms think like kernel methods support vector machines Bayesian inference and things like that where the theory is easier to write neural nets are messy and so theorists have reluctantly approached deep learning because it's very it's very complicated right the functions we optimize are non-convex
Speaker A:  So you can't prove anything.
Speaker A:  We use stochastic gradient,
Speaker A:  which for an optimization person is really,
Speaker A:  really hard to model the behavior of.
Speaker A:  All the traditional tools in optimization and criteria that we use to analyze optimization algorithms go out the window because in machine learning we don't care about precise optimization because that creates overfitting.
Speaker A:  Even statisticians and probabilists are baffled.
Speaker A:  by a phenomenon called double descent.
Speaker A:  So traditionally every textbook in statistics tell you if you try to fit a function to a bunch of points
Speaker A:  you don't want too many parameters because your system is going to overfit,
Speaker A:  right?
Speaker A:  It's going to, you know, if you have 10 points and use an 11 degree polynomial,
Speaker A:  your polynomial is going to go through every point exactly but between the points it's going to go completely wild,
Speaker A:  right?
Speaker A:  So as a,
Speaker A:  as a
Speaker A:  approximation for noisy signal for functional approximation you need models with a small number of parameters that argument turns out to be completely false empirically initially okay and now we need to understand this theoretically so neural nets are way over parameterized the number of parameters in neural nets is enormous compared to the amount of training samples yet those systems generalize pretty well they interpolate quite well they even extrapolate
Speaker A:  And that's a phenomenon,
Speaker A:  an empirical phenomenon called double decide,
Speaker A:  where the error on the separate test set.
Speaker A:  of a model is going to go down as you increase the number of training samples,
Speaker A:  the number as you increase the power of the model,
Speaker A:  like the degree of the polynomial,
Speaker A:  the number of parameters in your neural net,
Speaker A:  then it's going to increase,
Speaker A:  okay,
Speaker A:  and this is where overfitting occurs.
Speaker A:  But then as you increase the power of the model,
Speaker A:  the number of parameters,
Speaker A:  it actually decreases again,
Speaker A:  at least if you regularize it properly,
Speaker A:  and it may actually go to zero.
Speaker A:  So this phenomenon is a little baffling. There are a few intuitive explanations for it. I have had one for a long time, but it's now completely understood theoretically.
Speaker A:  And then, you know, there's more specific properties,
Speaker A:  I think, where mathematics.
Speaker A:  So I didn't talk much about energy-based models.
Speaker A:  There's a lot of really interesting research and mathematics I hope to do there,
Speaker A:  which is basically.
Speaker A:  Okay, let's say you want to estimate the dependency between two variables,
Speaker A:  two scalar variables,
Speaker A:  and I give you a bunch of data points,
Speaker A:  okay,
Speaker A:  and the dependency between the two variable x and y is not a function because there might be multiple values of y for a given x that are in your,
Speaker A:  you know, in your in your samples.
Speaker A:  How do you capture this dependency between x and y?
Speaker A:  So of course you could say, well, I'm going to learn a joint distribution between x and y,
Speaker A:  but that may actually be
Speaker A:  Extremely difficult, particularly in high dimension.
Speaker A:  Estimating distribution in high dimension is basically impossible and intractable.
Speaker A:  You have to represent it by an energy function,
Speaker A:  you take the exponential minus and you normalize and the normalization constant is intractable, it's like the partition function in physics, you don't know how to integrate complex energy function,
Speaker A:  so it's basically intractable.
Speaker A:  Okay,
Speaker A:  so how about something that's simpler,
Speaker A:  and that's energy-based model which consists in
Speaker A:  Can I learn a contrast function that will give me which is scalar scalar outputs,
Speaker A:  right?
Speaker A:  And it takes a pair of X and Y and if the pair of X and Y is in the region of high data density it gives me a low value,
Speaker A:  let's say zero.
Speaker A:  And if I move away from the manifold of data,
Speaker A:  if you want,
Speaker A:  the value of this scalar function increases.
Speaker A:  Okay?
Speaker A:  So it's basically a contrast function,
Speaker A:  an energy function,
Speaker A:  that tells me you are on the data manifold or you are away from it.
Speaker A:  And that's all I need to capture the dependency between two variables.
Speaker A:  It's a much better way actually,
Speaker A:  a much simpler way also of capturing dependencies than probabilistic modeling.
Speaker A:  There's a lot of theory to do about this.
Speaker A:  But, okay,
Speaker A:  it's missing.
Speaker A:  A long answer,
Speaker A:  I'm sorry.
Speaker B:  There is NASA from that, Rafit, can you, how can we do,
Speaker B:  Rafit,
Speaker B:  can you?
Speaker C:  I already asked him to unmute Nassaf,
Speaker A:  Okay,
Speaker C:  please unmute your, it's
Speaker A:  okay, sorry.
Speaker C:  correct now.
Speaker D:  I don't know if
Speaker A:  Yes,
Speaker D:  you can hear me.
Speaker A:  yes, yes I
Speaker C:  Yeah,
Speaker A:  can
Speaker D:  Perfect.
Speaker C:  yeah.
Speaker D:  Perfect.
Speaker D:  Thank you.
Speaker D:  So thank you very much for the talk,
Speaker D:  Professor Lucan. I found the distinction that you made between simple action, prediction and true planning with a world model especially interesting and also your point that the next wave,
Speaker D:  if I can say, of AI has to deal with.
Speaker D:  more dimension high dimensional noisy data rather than just tokens i my main question is about deployment in safety critical industries like space nuclear i i'm actually a nuclear engineer in paris in in within within the um the r&d team
Speaker D:  what we call the DEC, the Digital Excellence Center. So that part resonated a lot with me because our reality is exactly this, actually, what you described,
Speaker D:  sensory streams,
Speaker D:  inspection images,
Speaker D:  maintenance data,
Speaker D:  etc.
Speaker D:  So my question is, to make a link with your slides, you argue that word models should not be digital twins and you also take a fairly strong position against generative models like
Speaker D:  like chat GPT or whatever and but but in nuclear physics-based models explicit simulators or just how to say it the uncertainty quantification are not optional you know so we are judged not only on performance but on validation and auditability etc so how do you see GEPA style or I'm not a specialist so excuse me
Speaker D:  about that but the the action conditioned word models that you describe how do you see them interfacing with the first principles engineering models in domains like nuclear actually do you say do you see them as replacing digital twins or rather um how to say it as a higher abstraction layer on top of them and for planning for anomaly or accident anticipation etc etc
Speaker A:  Yeah
Speaker A:  Yeah, so I mean what we anticipate and this is something of course
Speaker A:  We think about a lot in the context of Amilabs,
Speaker A:  which by the way is pronounced the French way,
Speaker A:  Amilabs.
Speaker B:  I mean,
Speaker A: 
Speaker B:  okay.
Speaker A:  And we think about that a lot because we think that's basically our...
Speaker A:  You know, our first business and customers would be the control of complex systems such as a power plant,
Speaker A:  possibly a nuclear power plant,
Speaker C:  Okay.
Speaker A:  by,
Speaker A:  you know, training a phenomenological model of the system that, you know, allows to plan for sequence of intervention,
Speaker A:  you know, for any particular situation.
Speaker A:  Now, you can train this with real data.
Speaker A:  You can also pre-train it with synthetic data that's obtained from
Speaker A:  from you
Speaker D:  Hmm.
Speaker A:  know digital twin simulation but then completed with real data which probably makes it more realistic if you want and then the system can also kind of fine-tune itself as it goes you know it makes a prediction at every time step right so it can then observe the result and say oh I need to adjust my model because you know I see a discrepancy between what I predicted and what actually occurred I mean this is similar to what people do in you know model predictive control
Speaker D:  Yes,
Speaker A:  you know
Speaker D:  yes.
Speaker A:  you know procedures like IDICOM and things like that so um so yeah I mean that's probably or or core core business is
Speaker E:  Okay,
Speaker A:  that
Speaker E:  yeah
Speaker A:  you know before we have reliable models that you know would be usable for nuclear power control it might take a while but but but that's kind of the hope frankly
Speaker F:  Okay, okay,
Speaker F:  that's interesting.
Speaker F:  Okay, thank you. Just to add a little bit of information in nuclear, we are trying to simplify the process of building nuclear power plant, etc.
Speaker F:  So we have what we call SMRs. I don't know if you have heard about them, which are small modular reactors, a type of, let's say micro modular reactors. So with your JAPA style models,
Speaker F:  I think there is a potential collaboration that you
Speaker F:  that you could benefit from.
Speaker F:  Yeah,
Speaker F:  it could
Speaker A:  Yeah,
Speaker F:  be something
Speaker A:  that would useful. be... Yeah, yeah,
Speaker F:  So
Speaker A:  I mean, thank it.
Speaker F:  you again.
Speaker F:  It was very interesting to follow you. Thank you.
Speaker A:  Thank you.
Speaker G:  Is there another question?
Speaker H:  There is a question in the chat, Nabil.
Speaker G:  I don't see it.
Speaker G:  Can you?
Speaker H:  Yes,
Speaker G:  Ah, yes.
Speaker H:  Mohammed Alwadi.
Speaker A:  Yes.
Speaker G:  Mohammed,
Speaker G:  if you are with us, you can ask them, ask Dr.
Speaker G:  LeCun directly,
Speaker G:  Mohammed.
Speaker H:  Yes, can you hear me?
Speaker A:  Yes,
Speaker G:  Yes.
Speaker A:  we hear you.
Speaker G:  Yes.
Speaker G:  Okay, yeah, I'm very happy to see you live.
Speaker G:  My question is a recurring one.
Speaker G:  It's about how the spark of intelligence occurred suddenly in a system that's only conceived to predict the next word.
Speaker G:  It's based on language,
Speaker G:  yet at the same time we have the impression it's exhibiting real intelligence at times.
Speaker G:  And it's baffling.
Speaker G:  I was wondering whether you had an explanation on
Speaker A:  Yeah.
Speaker G:  when and how that happened.
Speaker G:  And
Speaker A:  Okay.
Speaker G:  thank you.
Speaker A:  Sure.
Speaker A:  There is only two or three domains where LLMs exhibit sort of baffling intelligence,
Speaker A:  if you want.
Speaker G:  Yes.
Speaker A:  And those are computer code generation,
Speaker A:  mathematics.
Speaker A:  and perhaps law okay so legal text and things like that and the reason is these are domains at least for the first two certainly where the language itself is a kind of substrate for reasoning right when we do mathematics the the simple manipulation of symbols gives us sometimes results that we did not expect right so the the reasoning
Speaker A:  can be basically supported by the language itself and there's a similar phenomenon when you write code where where where you know you may have a you know some idea about how to organize the code but when you start writing it it kind of crystallizes and the simple fact that you're writing the code sort of makes your your your concepts clearer in in many ways at least if you're a good computer scientist so
Speaker A:  You can imagine that for those two domains,
Speaker A:  manipulating symbols,
Speaker A:  which is what LLMs do,
Speaker A:  can help with reasoning.
Speaker A:  And in fact, you know, the way those systems do math and code is that they generate lots and lots of different sequences of symbols and then they have another network that kind of selects the best ones.
Speaker A:  And if it's code generation,
Speaker A:  you can just test whether the code works and then iterate,
Speaker A:  which is what code generation takes so long.
Speaker A:  If it's mathematics,
Speaker A:  you know, you arrive at a result and,
Speaker A:  you know, you can try to prove it, right?
Speaker A:  You can verify is a result, you know, is true or not, you know, with perhaps numerical examples or something like that.
Speaker A:  So those are two domains where there is self-adjustment because you can verify if an answer is correct or not. And the reasoning...
Speaker A:  Substrate is the language itself.
Speaker A:  Most of human reasoning and intelligence has nothing to do with language.
Speaker A:  Okay,
Speaker A:  it has to do with our experience of the real world,
Speaker A:  but it's not language-bound or it's not even helped by language.
Speaker A:  So it's certainly true of animals,
Speaker A:  right?
Speaker A:  They don't have language,
Speaker A:  at least not to the same extent.
Speaker A:  So, okay,
Speaker A:  so that's only a partial answer to your question.
Speaker A:  So the type of intelligence that we observe in LLMs is very narrow,
Speaker A:  is very restricted.
Speaker A:  And the reason why they seem to be intelligent by answering all the questions we ask them is a bit of an illusion.
Speaker A:  They basically do retrieval,
Speaker A:  okay.
Speaker A:  So those systems are not particularly intelligent,
Speaker A:  but they are extremely good at accumulating enormous amounts of knowledge and then regurgitating that knowledge at the right time and maybe adapting it in minor ways,
Speaker A:  okay.
Speaker A:  But they're not that smart. In fact, they do, they give you really stupid answers sometimes,
Speaker A:  right.
Speaker A:  There is a story that has circulated recently on social networks where someone said,
Speaker A:  Okay,
Speaker A:  I need to wash my car.
Speaker A:  I need to get my car washed.
Speaker A:  And the car wash place is 100 meters from my house. Should I walk?
Speaker B:  Yeah.
Speaker A:  And most LLMs, you know, chat GPT,
Speaker A:  the latest one, Claude, you know, all of those,
Speaker A:  meta AI,
Speaker A:  they say, no,
Speaker A:  you should, I mean, yes, you should work because it's only 100 meters away,
Speaker A:  like not realizing you're not going to have your car with you, okay.
Speaker A:  The only one that answers correctly is Gemini from Google,
Speaker A:  but it's very likely that the reason it answers correctly is because in the last few weeks it was fine-tuned with the correct answer.
Speaker A:  It was to detect that question and answer it correctly.
Speaker A:  I was made fun of in the past year or two because on an interview with Lex Freedman,
Speaker A:  a pretty popular podcast,
Speaker A:  I said, look,
Speaker A:  you know,
Speaker A:  LLMs don't have any physical need.
Speaker A:  If you put an object on the table and you push the table, you know the object will move with the table,
Speaker A:  right? That's kind of...
Speaker A:  GPT
Speaker C:  Right.
Speaker A:  obviously physical intuition but if you have if you ask you know chat GPT or one of its successor it's not going to be able to you know
Speaker A:  understand the physical reality behind this and make the right prediction and of course six months later like so if you ask a question to ChagiPT at that time it would not answer correctly but if you ask the next version of ChagiPT it did answer correctly and the reason is it's not that it you know understood physical reality any better it's that it was explicitly fine-tuned to answer that particular question because as soon as as you know the podcast was published hundreds of people actually asked the question to ChagiPT to verify the
Speaker A:  idea and so it was incorrect and so that became part of the training set now and and you know open ai integrated that that question in the fine-tuning set and of course you know any particular question that you ask in a system you can fine-tune it to answer it correctly but it's retrieval it's like those students you have in your class that you know do rote learning but don't really have a deep understanding of the underlying mathematics right
Speaker D:  All right. Thank you.
Speaker A:  If there is no other questions,
Speaker A:  I have perhaps,
Speaker A:  est-ce que tu vois d'autres questions Rafiq à la fin de l'université
Speaker D:  Yes, I have a question.
Speaker D:  Thank you, Professor Jan,
Speaker D:  for this nice lecture.
Speaker D:  In this lecture, you focus especially on human interests in artificial intelligence.
Speaker D:  My question is in that direction.
Speaker D:  Should humanity be afraid of AI in the future?
Speaker A:  Yeah, it's a very common question.
Speaker A:  Okay,
Speaker A:  we should be careful about AI.
Speaker A:  Because it's, you know, powerful technology with a big impact,
Speaker A:  we have to make sure the impact is beneficial to all of us.
Speaker A:  But like society is used to doing this.
Speaker A:  I mean, we do this with every new technology that comes out.
Speaker A:  We have, you know, particularly if it's consumer facing,
Speaker A:  we have regulation to make sure it's safe and things like that, right?
Speaker A:  Or, you know, particularly for things like nuclear power.
Speaker A:  But OK,
Speaker A:  but we should not be afraid of it for the reasons that a lot of people are claiming we should be afraid of it.
Speaker A:  So the idea somehow that AI is qualitatively different from other technology and is intrinsically dangerous at the research level,
Speaker A:  that's just completely false.
Speaker A:  That's just ridiculous,
Speaker A:  in fact.
Speaker A:  It's basically a cult that started in Silicon Valley.
Speaker A:  It's called effective altruism of people who...
Speaker A:  are claiming to kind of try to make long-term prediction about the future of humanity and basically they focus on the idea that if a technology is potentially dangerous you know or powerful necessarily is dangerous then we should stop working on it I mean it's just
Speaker A:  images that really is focusing on developing this thing. We're still doing research, we're open sourcing,
Speaker A:  we're publishing,
Speaker A:  we're just getting started,
Speaker A:  we're hiring too and basically solve all the problems in the real world that AI currently really is not so good for.
Speaker A:  And the hope is that, you know, maybe hierarchical JEPPA
Speaker A:  Hierarchical planning will allow us to train sort of universal causal models of any complex phenomenon and be the basis for you know any intelligent system in the future and thank you very much.
Speaker B:  Thank you very much Professor Lacan.
Speaker B:  We can thank Professor Lacan.
Speaker B:  And now perhaps some questions.
Speaker A:  Sure.
Speaker B:  Okay, thank you.
Speaker B:  Okay,
Speaker B:  I have a first question.
Speaker B:  The fact that you accepted the invitation and applied mathematics webinar is my sense the best proof of the importance of this science.
Speaker B:  Do we think that there are enough mathematicians dedicating their research to AI,
Speaker B:  or do
Speaker A:  No.
Speaker B:  we think that AI needs more mathematicians?
Speaker A:  Yes.
Speaker A:  So,
Speaker A:  you know, my academic position is with the Courant Institute, which is actually since September is a school within New York University.
Speaker A:  It's a school that regroups mathematics,
Speaker A:  pure and applied.
Speaker A:  Courant, of course, is famous for applied mathematics,
Speaker A:  computer science and data science.
Speaker A:  Okay, it's a standalone school.
Speaker A:  It used to be part of the arts and science school, but now it's a separate school, which basically is because of the importance of both
Speaker A:  mathematics, particularly applied mathematics,
Speaker A:  computer science,
Speaker A:  particularly with AI and data science, which is really applied AI,
Speaker A:  if you will,
Speaker A:  right?
Speaker A:  So NYU has decided that this whole field is so important that it should have a dedicated school separate from, you know, the law school and the business school and the arts and science and the engineering school.
Speaker A:  I've been personally,
Speaker A:  because being part of Coop
Speaker A:  Although I'm part of the computer science department,
Speaker A:  I've had a lot of interactions and contacts and even students from applied math.
Speaker A:  And for many years, I was on the science advisory board of the Institute for Pure and Applied Mathematics at UCLA.
Speaker A:  And I've always tried to bring in...
Speaker A:  interest from mathematicians to machine learning and deep learning in particular because the mathematical problems they are really in my opinion very interesting but also very complicated and traditionally people interested in machine learning who have you know a bit of a interest and background in mathematics have focused in the past on simpler
Speaker A:  machine learning paradigms think like kernel methods support vector machines Bayesian inference and things like that where the theory is easier to write neural nets are messy and so theorists have reluctantly approached deep learning because it's very it's very complicated right the functions we optimize are non-convex
Speaker A:  So you can't prove anything.
Speaker A:  We use stochastic gradient,
Speaker A:  which for an optimization person is really,
Speaker A:  really hard to model the behavior of.
Speaker A:  All the traditional tools in optimization and criteria that we use to analyze optimization algorithms go out the window because in machine learning we don't care about precise optimization because that creates overfitting.
Speaker A:  Even statisticians and probabilists are baffled.
Speaker A:  by a phenomenon called double descent.
Speaker A:  So traditionally every textbook in statistics tell you if you try to fit a function to a bunch of points
Speaker A:  you don't want too many parameters because your system is going to overfit,
Speaker A:  right?
Speaker A:  It's going to, you know, if you have 10 points and use an 11 degree polynomial,
Speaker A:  your polynomial is going to go through every point exactly but between the points it's going to go completely wild,
Speaker A:  right?
Speaker A:  So as a,
Speaker A:  as a
Speaker A:  approximation for noisy signal for functional approximation you need models with a small number of parameters that argument turns out to be completely false empirically initially okay and now we need to understand this theoretically so neural nets are way over parameterized the number of parameters in neural nets is enormous compared to the amount of training samples yet those systems generalize pretty well they interpolate quite well they even extrapolate
Speaker A:  And that's a phenomenon,
Speaker A:  an empirical phenomenon called double decide,
Speaker A:  where the error on the separate test set.
Speaker A:  of a model is going to go down as you increase the number of training samples,
Speaker A:  the number as you increase the power of the model,
Speaker A:  like the degree of the polynomial,
Speaker A:  the number of parameters in your neural net,
Speaker A:  then it's going to increase,
Speaker A:  okay,
Speaker A:  and this is where overfitting occurs.
Speaker A:  But then as you increase the power of the model,
Speaker A:  the number of parameters,
Speaker A:  it actually decreases again,
Speaker A:  at least if you regularize it properly,
Speaker A:  and it may actually go to zero.
Speaker A:  So this phenomenon is a little baffling. There are a few intuitive explanations for it. I have had one for a long time, but it's now completely understood theoretically.
Speaker A:  And then, you know, there's more specific properties,
Speaker A:  I think, where mathematics.
Speaker A:  So I didn't talk much about energy-based models.
Speaker A:  There's a lot of really interesting research and mathematics I hope to do there,
Speaker A:  which is basically.
Speaker A:  Okay, let's say you want to estimate the dependency between two variables,
Speaker A:  two scalar variables,
Speaker A:  and I give you a bunch of data points,
Speaker A:  okay,
Speaker A:  and the dependency between the two variable x and y is not a function because there might be multiple values of y for a given x that are in your,
Speaker A:  you know, in your in your samples.
Speaker A:  How do you capture this dependency between x and y?
Speaker A:  So of course you could say, well, I'm going to learn a joint distribution between x and y,
Speaker A:  but that may actually be
Speaker A:  Extremely difficult, particularly in high dimension.
Speaker A:  Estimating distribution in high dimension is basically impossible and intractable.
Speaker A:  You have to represent it by an energy function,
Speaker A:  you take the exponential minus and you normalize and the normalization constant is intractable, it's like the partition function in physics, you don't know how to integrate complex energy function,
Speaker A:  so it's basically intractable.
Speaker A:  Okay,
Speaker A:  so how about something that's simpler,
Speaker A:  and that's energy-based model which consists in
Speaker A:  Can I learn a contrast function that will give me which is scalar scalar outputs,
Speaker A:  right?
Speaker A:  And it takes a pair of X and Y and if the pair of X and Y is in the region of high data density it gives me a low value,
Speaker A:  let's say zero.
Speaker A:  And if I move away from the manifold of data,
Speaker A:  if you want,
Speaker A:  the value of this scalar function increases.
Speaker A:  Okay?
Speaker A:  So it's basically a contrast function,
Speaker A:  an energy function,
Speaker A:  that tells me you are on the data manifold or you are away from it.
Speaker A:  And that's all I need to capture the dependency between two variables.
Speaker A:  It's a much better way actually,
Speaker A:  a much simpler way also of capturing dependencies than probabilistic modeling.
Speaker A:  There's a lot of theory to do about this.
Speaker A:  But, okay,
Speaker A:  it's missing.
Speaker A:  A long answer,
Speaker A:  I'm sorry.
Speaker B:  There is NASA from that, Rafit, can you, how can we do,
Speaker B:  Rafit,
Speaker B:  can you?
Speaker C:  I already asked him to unmute Nassaf,
Speaker A:  Okay,
Speaker C:  please unmute your, it's
Speaker A:  okay, sorry.
Speaker C:  correct now.
Speaker D:  I don't know if
Speaker A:  Yes,
Speaker D:  you can hear me.
Speaker A:  yes, yes I
Speaker C:  Yeah,
Speaker A:  can
Speaker D:  Perfect.
Speaker C:  yeah.
Speaker D:  Perfect.
Speaker D:  Thank you.
Speaker D:  So thank you very much for the talk,
Speaker D:  Professor Lucan. I found the distinction that you made between simple action, prediction and true planning with a world model especially interesting and also your point that the next wave,
Speaker D:  if I can say, of AI has to deal with.
Speaker D:  more dimension high dimensional noisy data rather than just tokens i my main question is about deployment in safety critical industries like space nuclear i i'm actually a nuclear engineer in paris in in within within the um the r&d team
Speaker D:  what we call the DEC, the Digital Excellence Center. So that part resonated a lot with me because our reality is exactly this, actually, what you described,
Speaker D:  sensory streams,
Speaker D:  inspection images,
Speaker D:  maintenance data,
Speaker D:  etc.
Speaker D:  So my question is, to make a link with your slides, you argue that word models should not be digital twins and you also take a fairly strong position against generative models like
Speaker D:  like chat GPT or whatever and but but in nuclear physics-based models explicit simulators or just how to say it the uncertainty quantification are not optional you know so we are judged not only on performance but on validation and auditability etc so how do you see GEPA style or I'm not a specialist so excuse me
Speaker D:  about that but the the action conditioned word models that you describe how do you see them interfacing with the first principles engineering models in domains like nuclear actually do you say do you see them as replacing digital twins or rather um how to say it as a higher abstraction layer on top of them and for planning for anomaly or accident anticipation etc etc
Speaker A:  Yeah
Speaker A:  Yeah, so I mean what we anticipate and this is something of course
Speaker A:  We think about a lot in the context of Amilabs,
Speaker A:  which by the way is pronounced the French way,
Speaker A:  Amilabs.
Speaker B:  I mean,
Speaker A: 
Speaker B:  okay.
Speaker A:  And we think about that a lot because we think that's basically our...
Speaker A:  You know, our first business and customers would be the control of complex systems such as a power plant,
Speaker A:  possibly a nuclear power plant,
Speaker C:  Okay.
Speaker A:  by,
Speaker A:  you know, training a phenomenological model of the system that, you know, allows to plan for sequence of intervention,
Speaker A:  you know, for any particular situation.
Speaker A:  Now, you can train this with real data.
Speaker A:  You can also pre-train it with synthetic data that's obtained from
Speaker A:  from you
Speaker D:  Hmm.
Speaker A:  know digital twin simulation but then completed with real data which probably makes it more realistic if you want and then the system can also kind of fine-tune itself as it goes you know it makes a prediction at every time step right so it can then observe the result and say oh I need to adjust my model because you know I see a discrepancy between what I predicted and what actually occurred I mean this is similar to what people do in you know model predictive control
Speaker D:  Yes,
Speaker A:  you know
Speaker D:  yes.
Speaker A:  you know procedures like IDICOM and things like that so um so yeah I mean that's probably or or core core business is
Speaker E:  Okay,
Speaker A:  that
Speaker E:  yeah
Speaker A:  you know before we have reliable models that you know would be usable for nuclear power control it might take a while but but but that's kind of the hope frankly
Speaker F:  Okay, okay,
Speaker F:  that's interesting.
Speaker F:  Okay, thank you. Just to add a little bit of information in nuclear, we are trying to simplify the process of building nuclear power plant, etc.
Speaker F:  So we have what we call SMRs. I don't know if you have heard about them, which are small modular reactors, a type of, let's say micro modular reactors. So with your JAPA style models,
Speaker F:  I think there is a potential collaboration that you
Speaker F:  that you could benefit from.
Speaker F:  Yeah,
Speaker F:  it could
Speaker A:  Yeah,
Speaker F:  be something
Speaker A:  that would useful. be... Yeah, yeah,
Speaker F:  So
Speaker A:  I mean, thank it.
Speaker F:  you again.
Speaker F:  It was very interesting to follow you. Thank you.
Speaker A:  Thank you.
Speaker G:  Is there another question?
Speaker H:  There is a question in the chat, Nabil.
Speaker G:  I don't see it.
Speaker G:  Can you?
Speaker H:  Yes,
Speaker G:  Ah, yes.
Speaker H:  Mohammed Alwadi.
Speaker A:  Yes.
Speaker G:  Mohammed,
Speaker G:  if you are with us, you can ask them, ask Dr.
Speaker G:  LeCun directly,
Speaker G:  Mohammed.
Speaker H:  Yes, can you hear me?
Speaker A:  Yes,
Speaker G:  Yes.
Speaker A:  we hear you.
Speaker G:  Yes.
Speaker G:  Okay, yeah, I'm very happy to see you live.
Speaker G:  My question is a recurring one.
Speaker G:  It's about how the spark of intelligence occurred suddenly in a system that's only conceived to predict the next word.
Speaker G:  It's based on language,
Speaker G:  yet at the same time we have the impression it's exhibiting real intelligence at times.
Speaker G:  And it's baffling.
Speaker G:  I was wondering whether you had an explanation on
Speaker A:  Yeah.
Speaker G:  when and how that happened.
Speaker G:  And
Speaker A:  Okay.
Speaker G:  thank you.
Speaker A:  Sure.
Speaker A:  There is only two or three domains where LLMs exhibit sort of baffling intelligence,
Speaker A:  if you want.
Speaker G:  Yes.
Speaker A:  And those are computer code generation,
Speaker A:  mathematics.
Speaker A:  and perhaps law okay so legal text and things like that and the reason is these are domains at least for the first two certainly where the language itself is a kind of substrate for reasoning right when we do mathematics the the simple manipulation of symbols gives us sometimes results that we did not expect right so the the reasoning
Speaker A:  can be basically supported by the language itself and there's a similar phenomenon when you write code where where where you know you may have a you know some idea about how to organize the code but when you start writing it it kind of crystallizes and the simple fact that you're writing the code sort of makes your your your concepts clearer in in many ways at least if you're a good computer scientist so
Speaker A:  You can imagine that for those two domains,
Speaker A:  manipulating symbols,
Speaker A:  which is what LLMs do,
Speaker A:  can help with reasoning.
Speaker A:  And in fact, you know, the way those systems do math and code is that they generate lots and lots of different sequences of symbols and then they have another network that kind of selects the best ones.
Speaker A:  And if it's code generation,
Speaker A:  you can just test whether the code works and then iterate,
Speaker A:  which is what code generation takes so long.
Speaker A:  If it's mathematics,
Speaker A:  you know, you arrive at a result and,
Speaker A:  you know, you can try to prove it, right?
Speaker A:  You can verify is a result, you know, is true or not, you know, with perhaps numerical examples or something like that.
Speaker A:  So those are two domains where there is self-adjustment because you can verify if an answer is correct or not. And the reasoning...
Speaker A:  Substrate is the language itself.
Speaker A:  Most of human reasoning and intelligence has nothing to do with language.
Speaker A:  Okay,
Speaker A:  it has to do with our experience of the real world,
Speaker A:  but it's not language-bound or it's not even helped by language.
Speaker A:  So it's certainly true of animals,
Speaker A:  right?
Speaker A:  They don't have language,
Speaker A:  at least not to the same extent.
Speaker A:  So, okay,
Speaker A:  so that's only a partial answer to your question.
Speaker A:  So the type of intelligence that we observe in LLMs is very narrow,
Speaker A:  is very restricted.
Speaker A:  And the reason why they seem to be intelligent by answering all the questions we ask them is a bit of an illusion.
Speaker A:  They basically do retrieval,
Speaker A:  okay.
Speaker A:  So those systems are not particularly intelligent,
Speaker A:  but they are extremely good at accumulating enormous amounts of knowledge and then regurgitating that knowledge at the right time and maybe adapting it in minor ways,
Speaker A:  okay.
Speaker A:  But they're not that smart. In fact, they do, they give you really stupid answers sometimes,
Speaker A:  right.
Speaker A:  There is a story that has circulated recently on social networks where someone said,
Speaker A:  Okay,
Speaker A:  I need to wash my car.
Speaker A:  I need to get my car washed.
Speaker A:  And the car wash place is 100 meters from my house. Should I walk?
Speaker B:  Yeah.
Speaker A:  And most LLMs, you know, chat GPT,
Speaker A:  the latest one, Claude, you know, all of those,
Speaker A:  meta AI,
Speaker A:  they say, no,
Speaker A:  you should, I mean, yes, you should work because it's only 100 meters away,
Speaker A:  like not realizing you're not going to have your car with you, okay.
Speaker A:  The only one that answers correctly is Gemini from Google,
Speaker A:  but it's very likely that the reason it answers correctly is because in the last few weeks it was fine-tuned with the correct answer.
Speaker A:  It was to detect that question and answer it correctly.
Speaker A:  I was made fun of in the past year or two because on an interview with Lex Freedman,
Speaker A:  a pretty popular podcast,
Speaker A:  I said, look,
Speaker A:  you know,
Speaker A:  LLMs don't have any physical need.
Speaker A:  If you put an object on the table and you push the table, you know the object will move with the table,
Speaker A:  right? That's kind of...
Speaker A:  GPT
Speaker C:  Right.
Speaker A:  obviously physical intuition but if you have if you ask you know chat GPT or one of its successor it's not going to be able to you know
Speaker A:  understand the physical reality behind this and make the right prediction and of course six months later like so if you ask a question to ChagiPT at that time it would not answer correctly but if you ask the next version of ChagiPT it did answer correctly and the reason is it's not that it you know understood physical reality any better it's that it was explicitly fine-tuned to answer that particular question because as soon as as you know the podcast was published hundreds of people actually asked the question to ChagiPT to verify the
Speaker A:  idea and so it was incorrect and so that became part of the training set now and and you know open ai integrated that that question in the fine-tuning set and of course you know any particular question that you ask in a system you can fine-tune it to answer it correctly but it's retrieval it's like those students you have in your class that you know do rote learning but don't really have a deep understanding of the underlying mathematics right
Speaker D:  All right. Thank you.
Speaker A:  If there is no other questions,
Speaker A:  I have perhaps,
Speaker A:  est-ce que tu vois d'autres questions Rafiq à la fin de l'université
Speaker D:  Yes, I have a question.
Speaker D:  Thank you, Professor Jan,
Speaker D:  for this nice lecture.
Speaker D:  In this lecture, you focus especially on human interests in artificial intelligence.
Speaker D:  My question is in that direction.
Speaker D:  Should humanity be afraid of AI in the future?
Speaker A:  Yeah, it's a very common question.
Speaker A:  Okay,
Speaker A:  we should be careful about AI.
Speaker A:  Because it's, you know, powerful technology with a big impact,
Speaker A:  we have to make sure the impact is beneficial to all of us.
Speaker A:  But like society is used to doing this.
Speaker A:  I mean, we do this with every new technology that comes out.
Speaker A:  We have, you know, particularly if it's consumer facing,
Speaker A:  we have regulation to make sure it's safe and things like that, right?
Speaker A:  Or, you know, particularly for things like nuclear power.
Speaker A:  But OK,
Speaker A:  but we should not be afraid of it for the reasons that a lot of people are claiming we should be afraid of it.
Speaker A:  So the idea somehow that AI is qualitatively different from other technology and is intrinsically dangerous at the research level,
Speaker A:  that's just completely false.
Speaker A:  That's just ridiculous,
Speaker A:  in fact.
Speaker A:  It's basically a cult that started in Silicon Valley.
Speaker A:  It's called effective altruism of people who...
Speaker A:  are claiming to kind of try to make long-term prediction about the future of humanity and basically they focus on the idea that if a technology is potentially dangerous you know or powerful necessarily is dangerous then we should stop working on it I mean it's just

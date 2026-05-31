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

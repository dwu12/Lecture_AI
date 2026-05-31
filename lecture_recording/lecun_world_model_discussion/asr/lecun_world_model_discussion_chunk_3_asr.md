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

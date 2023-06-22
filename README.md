# Handling some of the gotcahs associated with the function call feature of OpenAI's Chat APIs

If you are planning to use the function call feature of OpenAI's chat APIs, the there are some potential problems you need to be aware of:

- The ChatGPT model may not generate function call argument in correct details as you may expect it to
- Even if you give it all the function call names, it may not call multiple functions in a sequence. If that's what you want it to do, you need to make handle it.
- It will hallucinate the names of functions and their arguments. This espcially happens as the number of functions provided to it grows.

You can handle some of these issues in your code via logic, however the best possible way to handle them is to let the ChatGPT model correct itself, or let it do the right thing in the first place.

In [my article](https://codeconfessions.substack.com/p/navigating-sharp-edges-in-openais) I discuss these problems, provide code examples showing exactly how the model breaks expectations and how to fix them without complicated logic in code.
[https://codeconfessions.substack.com/p/navigating-sharp-edges-in-openais](https://codeconfessions.substack.com/p/navigating-sharp-edges-in-openais)


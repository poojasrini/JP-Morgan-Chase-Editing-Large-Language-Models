# Editing-Large-Language-Models
Large Language Models (LLMs) today encapsulate a vast amount of information and generative capabilities. This is supported through a complex architecture driven by hundreds of millions of parameters. However, since the model’s factual knowledge can change over time, it requires a way to stay updated. To address this, various editing methods have been developed to address incorrect facts and provide a more computationally efficient alternative to retraining the LLMs.

We analyze the storage paradigm that autoregressive transformer models follow to facilitate easy retrieval of specific facts driven by the input prompt. This is done to edit factual associations stored in these locations to extend the current knowledge that the language models hold and ensure that they store information that is current and relevant. We perform a series of experiments to analyze the location of facts. The examination has also been performed on editing methodologies followed by current strategies and certain shortcomings are identified and underlined. Overall, our work drives the direction of future research to take into account the properties of a fact in itself along with all its input tokens to find the corresponding knowledge centers in transformers.

**JP Morgan Chase & Co. mentors:** Simerjot Kaur, Akshat Gupta <br/>
[Working with JP Morgan Chase & Co's AI research team as an integral part of the Data Science Capstone project]<br/>

**Group members names:** Pooja Srinivasan, Gokul Sunilkumar, Saili Myana, Sai Rithvik Kanakamedala, Utsav Vachhani

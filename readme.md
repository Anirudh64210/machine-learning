## Hi me and whoever looking at this,
-- Learning ML development w projects, this is a trial ml model spam ham detection, using NLP w TensorFlow/Keras, leveraging LSTM NN w embedding layers for text sequence modeling. 

Pipeline Used:
1. Text Cleaning
2. Tokenization
3. Padding Sequences
4. Embedding Layers
5. LSTM Model
6. Dense Layers
7. Sigmoid O/P

(As of 04/26/26 The Latest py vr 3.14 does not support TensorFlow modules, so used a py venv to use an older vr of py i.e. py 3.13.0/3.13.3 to download the required module and run code, keep in mind if you want to try this yourself as well.)

- PreProcessed data using tokenization, padding and scikit-learn for train-test splitting and eval, along w a confusion matrix. 


- Initially achieved low accuracy, but optimized model config - fixed loss function, and padding with consistent length and removing over aggressive preprocessing, to achieve around 96% accuracy, model is not perfect as it might be overfitting  and memorising a bit towards the end cycles of epoch, but used EarlyStopping for smart training. 


- Might optimize again later to make it practical and test using custom text.

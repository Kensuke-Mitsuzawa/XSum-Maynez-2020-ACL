# TF1 version
import tensorflow.compat.v1 as tf
import tensorflow_hub as hub
import tensorflow_text as tf_text

tf.compat.v1.disable_eager_execution()


text_generator = hub.Module('https://www.kaggle.com/models/google/bertseq2seq/TensorFlow1/roberta24-bbc/1')
input_documents = ['This is text from the first document.',
                   'This is text from the second document.']
output_summaries = text_generator(input_documents)

# Create a TensorFlow session
with tf.Session() as sess:
    # Initialize variables if the module has any (often needed for Hub modules)
    sess.run(tf.global_variables_initializer())
    sess.run(tf.tables_initializer()) # Also often needed for text/lookup tables

    # Run the tensor and fetch its value
    summaries = sess.run(output_summaries)

# --- End of new code ---

# Print the fetched summaries
print("Generated Summaries:")
for i, summary in enumerate(summaries):
    print(f"Document {i+1}: {summary.decode('utf-8')}") # Decode from bytes to string

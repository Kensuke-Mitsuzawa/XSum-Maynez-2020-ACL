# TF1 version
import tensorflow.compat.v1 as tf
import tensorflow_hub as hub
import tensorflow_text as tf_text

tf.compat.v1.disable_eager_execution()
tf.disable_eager_execution()


URL_HUB = "https://www.kaggle.com/models/google/bertseq2seq/TensorFlow1/roberta24-bbc/1"
module = hub.Module(URL_HUB)
# Define placeholders
input_ids = tf.placeholder(tf.int32, [None, None], name="input_ids")
input_mask = tf.placeholder(tf.int32, [None, None], name="input_mask")
segment_ids = tf.placeholder(tf.int32, [None, None], name="segment_ids")

inputs = {
    "input_ids": input_ids,
    "input_mask": input_mask,
    "segment_ids": segment_ids,
}

# Get all outputs using the correct signature
outputs = module(inputs, signature="tokens", as_dict=True)

tf.saved_model.simple_save(sess, "./tfhub_export", inputs=inputs, outputs=outputs)    


# 

# exporting the model
bert_layer = hub.KerasLayer(URL_HUB, trainable=False)
# Dummy wrapper model with input signature matching BERT
input_word_ids = tf.keras.layers.Input(shape=(None,), dtype=tf.int32, name="input_word_ids")
input_mask = tf.keras.layers.Input(shape=(None,), dtype=tf.int32, name="input_mask")
input_type_ids = tf.keras.layers.Input(shape=(None,), dtype=tf.int32, name="input_type_ids")
bert_outputs = bert_layer({
    "input_word_ids": input_word_ids,
    "input_mask": input_mask,
    "input_type_ids": input_type_ids
})

model = tf.keras.Model(
    inputs=[input_word_ids, input_mask, input_type_ids],
    outputs=bert_outputs
)

print(bert_layer, model)
print()
raise Exception()

# the document id = 34687720
input_text_bbc = """France\'s Dubuisson carded a 67 to tie with overnight leader Van Zyl of South Africa on 16 under par.\nMcIlroy carded a third straight five under-par 67 to move to 15 under par with Thailand\'s Kiradech Aphibarnrat.\nThe world number three\'s round included an eagle on the 12th as he bids to win his first title since May.\n"The 67s I\'ve shot this week have all been a little different and I feel like I\'ve played within myself for all of them, " said four-time major winner McIlroy of Northern Ireland. "I feel there\'s a low round out there for me and hopefully it\'s tomorrow."\nMcIlroy was level par for the day after 10 holes, dropping his first shots of the week by three-putting the third and 10th, the latter mistake prompting the 26-year-old to throw his putter at his bag.\nBut he hit back with a birdie on the par-five 11th and a towering four iron from 229 yards on the 13th set up an eagle from just four feet.\nThe former world number one ruptured a ligament in his left ankle during a game of football with friends in July, ruling him out of several tournaments.\nBut he returned in time to unsuccessfully defend his US PGA title at Whistling Straits in August and played in three of the FedEx Cup play-off events before starting the new PGA Tour season with a tie for 26th in the Frys.com Open in California.\nHe is targeting a third Race to Dubai title in four years and leads England\'s Danny Willett by 271, 214 points with three events remaining after the Turkish Open.\nEnglish pair Chris Wood (-13) and Richard Bland (-12) who were tied for second overnight are fifth and seventh respectively."""

input_documents = [input_text_bbc]
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

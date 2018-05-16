import tensorflow as tf
import numpy as np

tf.logging.set_verbosity(tf.logging.INFO)


def cnn_model_fn(features,labels,mode):
    
    #Input layer
    input_layer=tf.reshape(features["x"],[-1,28,28,1])
    
    #Convolutional Layer #1
    conv_1 = tf.layers.conv2d(
        inputs = input_layer,
        filters = 32,
        kernel_size = [5,5],
        padding = "same",
        activation = tf.nn.relu
    )
    
    #Pooling Layer #1
    pool_1 = tf.layers.max_pooling2d(
        inputs = conv_1,
        pool_size = [2,2],
        strides = 2
    )
    
    #Convolutional Layer #2
    conv_2 = tf.layers.conv2d(
        inputs = pool_1,
        filters = 64,
        kernel_size = [5,5],
        padding = "same",
        activation = tf.nn.relu
     )
    
    #Pooling Layer #2
    pool_2 = tf.layers.max_pooling2d(
        inputs = conv_2,
        pool_size = [2,2],
        strides = 2
    )
    
    #Dense layer
    pool2_flat=tf.reshape(pool_2,[-1, 3136])
    
    dense = tf.layers.dense(
        inputs = pool2_flat,
        units = 1024,
        activation = tf.nn.relu
    )
    
    dropout = tf.layers.dropout(
        inputs = dense,
        rate = 0.4,
        training = mode == tf.estimator.ModeKeys.TRAIN
    )
    
    # Logits layer
    logits = tf.layers.dense(
        inputs = dropout,
        units = 4
    )
    
    predictions = {
        "classes": tf.argmax(input = logits, axis =1),
        "probabilities" : tf.nn.softmax(
            logits,
            name = "softmax_tensor"
        )
    }
    
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode = mode, predictions = predictions)
    
    loss = tf.losses.sparse_softmax_cross_entropy(labels = labels, logits = logits)
    
    # Configure the Training Op
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.001)
        train_op = optimizer.minimize(loss = loss, global_step = tf.train.get_global_step())
        
        return tf.estimator.EstimatorSpec(mode = mode, loss = loss, train_op = train_op)
    
    # Evaluation metrics
    
    eval_metric_ops = {
      "accuracy": tf.metrics.accuracy(
          labels=labels, 
          predictions=predictions["classes"])
    }
    return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)

def main(unused_argv):
    data = np.load("dataset/figsFull.npy")
    data = np.float64(data)
    
    train_data = data[:8000,1:]
    test_data = data[8000:,1:]

    train_labels = np.int32(data[:8000,0])
    #validation_labels = data[7000:10000,0]
    test_labels = np.int32(data[8000:,0])
    
    shapes_classifier = tf.estimator.Estimator(
        model_fn = cnn_model_fn,
        model_dir="mdl/convol_shapes")
    
    # Set up logging for predictions
    tensors_to_log = {"probabilities": "softmax_tensor"}
    logging_hook = tf.train.LoggingTensorHook(tensors=tensors_to_log, every_n_iter=50)

    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x = {"x":train_data},
        y = train_labels,
        batch_size = 100,
        num_epochs = None,
        shuffle = True)

    shapes_classifier.train(
        input_fn = train_input_fn,
        steps = 1000,
        hooks = [logging_hook])

    #Evaluate the model and print results
    test_input_fn = tf.estimator.inputs.numpy_input_fn(
        x = {"x": test_data},
        y = test_labels,
        num_epochs=1,
        shuffle=False)

    eval_results = shapes-_classifier.evaluate(input_fn=test_input_fn)
    print(eval_results)

if __name__ == "__main__":
      tf.app.run()
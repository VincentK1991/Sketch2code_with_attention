# Sketch2code_with_attention
 Tutorial on how to use attention based image captioning model to perform sketch 2 code task, implemented in Pytorch.
 
 For more information, read this [blog post](https://vincentk1991.github.io/sketch2code/).
 
 This repo contains the encoder-decoder model in the model folder. The dataset is not provided here. But you can download it here:
 
 `wget https://s3-us-west-2.amazonaws.com/sketch2code/data.zip -O data/all_data.zip`
 
 then unzip
 
 `unzip data/all_data.zip -d data/all_data`
 
For the pre-processing step, please refer to the pre-processing notebook in the notebook folder.
 
 The code to run training/validation is "train.py".
 
 `python train.py --epochs=20 --encoder_lr=1e-4 --decoder_lr=1e-4 --train_data='insert-your-train-data-here' --val_data='insert-your-validation-data-here' --val_every=2 --model_name='Jun09_2020' --grad_clip=5.0`
 
 For the visualization step, please refer to the visualization notebook in the notebook folder.

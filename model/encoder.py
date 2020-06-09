# -*- coding: utf-8 -*-
"""Encoder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eb9zqI5rQlXnv5kwh58C3svp2YtMISQn
"""

import torch
import torch.nn as nn
import torchvision

class Encoder(nn.Module):
  """
  encoder
  use resnet-101 which take 224,224,3 input size
  the output layer is the last convolution before average pulling
  
  this is 2048,7,7 output size. this then we be resize to 512,14,14
  """
  def __init__(self,encoded_image_size=14):
    super(Encoder,self).__init__()
    self.enc_image_size = encoded_image_size
    
    resnet = torchvision.models.resnet101(pretrained=True)

    # remove linear and pool layer
    modules = list(resnet.children())[:-2] # leave out avg pooling and fully connected linear layer
    self.resnet = nn.Sequential(*modules)

    # resize the image to fixed size
    self.adaptive_pool = nn.AdaptiveAvgPool2d((encoded_image_size,encoded_image_size))

    self.fine_tune()  # execute the fine_fune function now

  def fine_tune(self,fine_tune=True):
    """
    specify which convolutional blocks to be fine-tuned.
    In this case, we will fine-tuned block 2-4 of resnet-101
    """
    for p in self.resnet.parameters():
      p.requires_grad = False
    for c in list(self.resnet.children())[5:]:
      for p in c.parameters():
        p.requires_grad = fine_tune  # if fine_tune == True, then the layers in block 2-4 will learn
  
  def forward(self,images):
    """
    forward propagation

    input image : a tensor of dimension (batch_size,3,image_size,image_size)
    where image_size = 224 for resnet-101
    the image should be pre-processed, i.e. normalized, RGB.

    output return encoded images dimension (512,14,14)
    """
    out = self.resnet(images) #output (batch_size,2048,image_size/32,image_size/32)
    out = self.adaptive_pool(out) #output (batch_size,2048,encoded_image_size,encoded_image_size)
    out = out.permute(0,2,3,1)
    return out
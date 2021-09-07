# Popular Loss Functions for Semantic Segmentation

There is an article that summarizes the most popular loss functions for semantic segmentation. The article is available [here](https://arxiv.org/abs/2006.14822).

## Content

* [Cross Entropy](#CE)
* [Focal Loss](#FL)
* [Dice Loss](#Dice)

## Cross Entropy<a name="CE"/>

Cross Entropy is the most typical loss function used for classification. Here, we use binary cross entropy as an example for illustrating this echnique mathmatically.

<p align="center">
  <img src="./images/ce.png">
</p>

Sometimes, the unbalanced dataset may affect the performance of cross entropy. Therefore, an improved version, weighted cross entropy, has been employed by many researchers.

<p align="center">
  <img src="./images/wce.png">
</p>

To further improve the generalization of weighted cross entropy, a new form, called balanced cross entropy, is proposed as follow.

<p align="center">
  <img src="./images/bce.png">
</p

The generalized form of Cross Entropy is:

<p align="center">
  <img src="./images/bce_g.png">
</p

## [Focal Loss](https://arxiv.org/abs/1708.02002)<a name="FL"/>

The formal mathmatical definition of Focal Loss is as follow:

<p align="center">
  <img src="./images/fl.png">
</p

Two parameters can be tuned during the training process, which are the alpha and the gamma. The alpha is the weight of the positive samples and the gamma is the power of term `1 - p_t`.

## [Dice Loss](https://arxiv.org/abs/1606.04797)<a name="Dice"/>

The generalized form of Dice Loss is:

<p align="center">
  <img src="./images/dice.png">
</p

For the easy understanding of the mathmatical definition, we can also use the following notation:

<p align="center">
  <img src="./images/dice_.png">
</p

Dice loss has a slight difference with iou loss, where the iou loss can be expressed as follow:

<p align="center">
  <img src="./images/iou_.png">
</p
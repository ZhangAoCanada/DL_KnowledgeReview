# Popular Choices of Operations for Object Detection

## Content

- [Activation Functions](#Activations)
    - [ReLU](#ReLU)
    - [Leaky ReLU](#LeakyReLU)
    - [Parametric ReLU](#ParametricReLU)
    - [ReLU6](#ReLU6)
    - [SELU](#SELU)
    - [GELU](#GELU)
    - [Swish](#Swish)
    - [Mish](#Mish)
- [Loss Functions for Box Regression](#LossFunctions)
    - [MSE](#MSE)
    - [IoU](#IoU)
    - [GIoU](#GIoU)
    - [DIoU](#DIoU)
    - [CIoU](#CIoU)
- [Data Augmentation](#DataAugmentation)
    - [Rotation](#Rotation)
- [Regularization](#Regularization)
- [Normalization](#Normalization)

## Activation Functions<a name="Activations"/>

### ReLU<a name="ReLU"/>

```python
ReLU(x) = max(0, x)
```

### Leaky ReLU<a name="LeakyReLU"/>

```python
a = 0.1 # manually assigned
LeakyReLU(x) = max(0, x) + a * min(0, x)
```

### Parametric ReLU<a name="ParametricReLU"/>

```python
a = tf.Variable(0.1) # learnable
ParametricReLU(x) = max(0, x) + a * min(0, x)
```

### ReLU6<a name="ReLU6"/>

`6` is an arbitrary choice that worked well. According to the authors, the upper bound encouraged their model to learn sparse features earlier.
```python
ReLU6(x) = min(6, max(0, x)) + a * min(0, x)
```

### SELU<a name="SELU"/>

Scaled Exponential Linear Unit
```python
SELU(x) = b * ( max(0, x) + a * (exp(min(0, x)) - 1) )
```

### GELU<a name="GELU"/>

Gaussian Error Linear Unit
```python
GELU(x) = 0.5 * x * (1 + tanh(sqrt(2/pi)) * (x + 0.044715 * x**3))
```

### Swish<a name="Swish"/>

```python
Swish(x) = x * sigmoid(a * x) = x / (1 + exp(- a * x))
```

### [Mish](https://arxiv.org/abs/1908.08681) (2020)<a name="Mish"/>

```python
Mish(x) = x * tanh(softplus(x))
```

## Loss Functions<a name="LossFunctions"/>

### MSE<a name="MSE"/>

```python
MSE(gt, pred) = mean(square(gt - pred))
```

### [IoU](https://arxiv.org/abs/1908.03851) (2019)<a name="IoU"/>

<p align="center">
  <img src="./images/iou.png" height="300">
</p>

### [GIoU](https://arxiv.org/abs/1902.09630) (2019)<a name="GIoU"/>

Generalized IoU
<p align="center">
  <img src="./images/giou.png" height="300">
</p>

### [DIoU](https://arxiv.org/abs/1911.08287) (2019)<a name="DIoU"/>

Distance IoU
<p align="center">
  <img src="./images/diou.png" height="400">
</p>

### [CIoU](https://arxiv.org/abs/1911.08287) (2019)<a name="CIoU"/>

Complete IoU
<p align="center">
  <img src="./images/ciou.png" height="400">
</p>
---
title: "Kaggle Connectivity to Colab"
date: 2025-01-11T18:35:41+05:30
draft: False
author: Ronak Rathore
tags: ["Kaggle", "Colab"]
image: /images/blogs/kaggle_colab/cover.png
description: ""
toc: True
---

In this article, I will provide a detailed guide on how to upload a Kaggle dataset directly to Google Colab. This process simplifies data access, allowing users to seamlessly integrate Kaggle datasets into their Colab notebooks for analysis, machine learning, or data engineering tasks.

---
### Prerequisite
- Colab
- Kaggle Dataset

---
### Steps:
#### 1. Choose Dataset

Pick the dataset you want to import into CoLab. I will be using Reviews for Hotels Worldwide (Booking.com)
<div align="center">
    <img src="/images/blogs/kaggle_colab/1.png" alt="Image Description" width = 900 height=200>
</div>

---
#### 2. API Token

To download a dataset, kaggle services require authentication. You must now download an API token.

You may quickly generate this token from your Kaggle account’s profile page. Easily access your Kaggle profile by clicking here.

```
select account –> find API section –> create new API token
```
<div align="center">
    <img src="/images/blogs/kaggle_colab/2.png" alt="Image Description" width = 300 height=200 />
</div>
<br>
<div align="center">
    <img src="/images/blogs/kaggle_colab/3.png" alt="Image Description" width = 900 height=100 />
</div>
<br>
<div align="center">
    <img src="/images/blogs/kaggle_colab/4.png" alt="Image Description" width = 900 height=100 />
</div>
<br>
A file named as kaggle.json will be downloaded on your local machine.

---
#### 3. Colab Notebook
Set up your colab notebook and upload kaggle.json which was downloaded in step 2 to it.

<div align="center">
    <img src="/images/blogs/kaggle_colab/5.png" alt="Image Description" width = 300 height=200 />
</div>

Now install Kaggle Library, make .kaggle directory, copy kaggle.json to it, change its permission.
```
    ! pip install kaggle
    ! mkdir ~/.kaggle
    ! cp kaggle.json ~/.kaggle/
    ! chmod 600 ~/.kaggle/kaggle.json
```
<div align="center">
    <img src="/images/blogs/kaggle_colab/6.png" alt="Image Description" width = 900 height=400 />
</div>

---
### 4. Download data
Now you just need to download dataset. There are two types of datasets:

- Competitions
- Datasets Downloading Competitions dataset:
```
! kaggle competitons download «name-of-competition»
```
Downloading Datasets:
```
! kaggle datasets download «name-of-dataset»
```
for example:
<div align="center">
    <img src="/images/blogs/kaggle_colab/7.png" alt="Image Description" width = 800 height=100 />
</div>

In case dataset is downloaded as zip extension, you can simply use unzip command of linux:
```
! unzip «name-of-file»
```
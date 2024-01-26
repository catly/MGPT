# Welcome to MGPT
## Our MGPT is split into three stages:
 1. Heterogeneous Network Construction
 2. Graph Pre-training
 3. Sub-graph Representation
## Datasets
Our experiments were conducted on two public data sets: Luo’s data [1] and Zheng’s data [2], which include various drug associations. We provide all the data for these two datasets at MGPT/get_nodefeature_module/data

## Examples Instructions
Take the Zheng’s dataset for example.
 1. Constructing heterogeneous graph:
```
 MGPT/get_nodefeature_module/test/random_vector_generation_10000_zheng.py
 MGPT/get_nodefeature_module/graph_dti/shuffle_save_down_graph.py
```
2. Graph Pre-training:
```
MGPT/prompt_module/pretrain.py
```
3. Sub-graph Representation:
```
MGPT/prompt_module/run.py
```

## References
```
[1] Luo, Y., Zhao, X., Zhou, J., Yang, J., Zhang, Y., Kuang, W., Peng, J., Chen, L., Zeng, J.: A network integration approach for drug-target interaction prediction and computational drug repositioning from heterogeneous information. Nature communications 8(1), 573 (2017)
[2] Zheng, Y., Peng, H., Zhang, X., Gao, X., Li, J.: Predicting drug targets from heterogeneous spaces using anchor graph hashing and ensemble learning. In: 2018 International Joint Conference on Neural Networks (IJCNN), pp. 1–7 (2018). IEEE
```

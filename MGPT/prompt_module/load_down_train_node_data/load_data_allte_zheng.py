import random
import numpy as np

random.seed(42)


trainset = []
valset = []
testset = []


# 设置交叉验证
link_DPPS = {}
notLink_DPPS = {}


link_DPPS["drug_chemical"] = [i for i in range(0,333)]
link_DPPS["drug_sideeffects"] = [i for i in range(666,999)]
link_DPPS["drug_substituent"] = [i for i in range(1332,1665)]
link_DPPS["drug_target"] = [i for i in range(1998,2331)]
link_DPPS["target_go"] = [i for i in range(2664,2997)]

notLink_DPPS["drug_chemical"] = [i for i in range(333,666)]
notLink_DPPS["drug_sideeffects"] = [i for i in range(999,1332)]
notLink_DPPS["drug_substituent"] = [i for i in range(1665,1998)]
notLink_DPPS["drug_target"] = [i for i in range(2331,2664)]
notLink_DPPS["target_go"] = [i for i in range(2997,3330)]



link_DPPS["all"] = link_DPPS["drug_chemical"] + link_DPPS["drug_sideeffects"] + link_DPPS["drug_substituent"] + link_DPPS["drug_target"] + link_DPPS["target_go"]
notLink_DPPS["all"] = notLink_DPPS["drug_chemical"] + notLink_DPPS["drug_sideeffects"] + notLink_DPPS["drug_substituent"] + notLink_DPPS["drug_target"] + notLink_DPPS["target_go"]

random.shuffle(link_DPPS["all"])
random.shuffle(notLink_DPPS["all"])

pice = len(link_DPPS["all"])//10
a = [link_DPPS["all"][i:i+pice] for i in range(0, len(link_DPPS["all"]), pice)]
b = [notLink_DPPS["all"][i:i+pice] for i in range(0, len(notLink_DPPS["all"]), pice)]

for i in range(10):
    trainset.append(a[((i) % 10)][:20] + b[((i) % 10)][:20])
    valset.append(a[((i + 1) % 10)][:20] + b[((i + 1) % 10)][:20])
    testset.append(a[((i + 2) % 10)] + b[((i + 2) % 10)])



np.save('../node_data/zheng/20-shot/all/all_train.npy', trainset)  # 保存文件
np.save('../node_data/zheng/20-shot/all/all_val.npy', valset)  # 保存文件
np.save('../node_data/zheng/20-shot/all/all_test.npy', testset)  # 保存文件



'''

'''
import torch
import numpy as np
import dgl
from dgl import save_graphs, load_graphs
import random
import json

random.seed(16)
def save_graph():


    adj_drug_chemical = np.loadtxt('../data/Zhengs_DTIdata/mat_drug_chemical_substructures.txt', dtype=np.float32)
    adj_drug_sideeffects = np.loadtxt('../data/Zhengs_DTIdata/mat_drug_sideeffects.txt', dtype=np.float32)
    adj_drug_substituent = np.loadtxt('../data/Zhengs_DTIdata/mat_drug_sub_stituent.txt', dtype=np.float32)
    adj_drug_target = np.loadtxt('../data/Zhengs_DTIdata/mat_drug_target_1.txt', dtype=np.float32)
    adj_target_go = np.loadtxt('../data/Zhengs_DTIdata/mat_target_GO.txt', dtype=np.float32)


    # edge_type = "protein_disease"

    nums_drug = len(adj_drug_chemical)
    nums_chemical = len(adj_drug_chemical[0])
    nums_sideeffects = len(adj_drug_sideeffects[0])
    nums_substituent = len(adj_drug_substituent[0])
    nums_target = len(adj_drug_target[0])
    nums_go = len(adj_target_go[0])


#################################################################################

    embedding_drug = np.random.normal(loc=6, scale=3, size=(nums_drug, 128))
    embedding_chemical = np.random.normal(loc=6, scale=3, size=(nums_chemical, 128))
    embedding_sideeffects = np.random.normal(loc=6, scale=3, size=(nums_sideeffects, 128))
    embedding_substituent = np.random.normal(loc=6, scale=3, size=(nums_substituent, 128))
    embedding_target = np.random.normal(loc=6, scale=3, size=(nums_target, 128))
    embedding_go = np.random.normal(loc=6, scale=3, size=(nums_go, 128))

    embedding_drug = torch.tensor(embedding_drug, dtype=torch.float32)
    embedding_chemical = torch.tensor(embedding_chemical, dtype=torch.float32)
    embedding_sideeffects = torch.tensor(embedding_sideeffects, dtype=torch.float32)
    embedding_substituent = torch.tensor(embedding_substituent, dtype=torch.float32)
    embedding_target = torch.tensor(embedding_target, dtype=torch.float32)
    embedding_go = torch.tensor(embedding_go, dtype=torch.float32)

#################################################################################
    link_DPPS = {}
    notLink_DPPS = {}
    link_num = {}
    notlink_num = {}

    link_DPPS["drug_chemical"] = []
    link_DPPS["drug_sideeffects"] = []
    link_DPPS["drug_substituent"] = []
    link_DPPS["drug_target"] = []
    link_DPPS["target_go"] = []

    notLink_DPPS["drug_chemical"] = []
    notLink_DPPS["drug_sideeffects"] = []
    notLink_DPPS["drug_substituent"] = []
    notLink_DPPS["drug_target"] = []
    notLink_DPPS["target_go"] = []

    link_num["drug_chemical"] = 0
    link_num["drug_sideeffects"] = 0
    link_num["drug_substituent"] = 0
    link_num["drug_target"] = 0
    link_num["target_go"] = 0

    notlink_num["drug_chemical"] = 0
    notlink_num["drug_sideeffects"] = 0
    notlink_num["drug_substituent"] = 0
    notlink_num["drug_target"] = 0
    notlink_num["target_go"] = 0

    node_labels = []
    graph_DPPNode = []
    # has_embedding_DPPs = [[0 for i in range(nums_disease)] for _ in range(nums_protein)]

    for i in range(nums_drug):
        for j in range(nums_chemical):
            if adj_drug_chemical[i][j] == 1:
                link_DPPS["drug_chemical"].append((("drug", "chemical"), (i, j)))
                link_num["drug_chemical"] += 1
            else:
                notLink_DPPS["drug_chemical"].append((("drug", "chemical"), (i, j)))
                notlink_num["drug_chemical"] += 1

    # drug-disease
    for i in range(nums_drug):
        for j in range(nums_sideeffects):
            if adj_drug_sideeffects[i][j] == 1:
                link_DPPS["drug_sideeffects"].append((("drug", "sideeffects"), (i, j)))
                link_num["drug_sideeffects"] += 1
            else:
                notLink_DPPS["drug_sideeffects"].append((("drug", "sideeffects"), (i, j)))
                notlink_num["drug_sideeffects"] += 1

    # drug-se
    for i in range(nums_drug):
        for j in range(nums_substituent):
            if adj_drug_substituent[i][j] == 1:
                link_DPPS["drug_substituent"].append((("drug", "substituent"), (i, j)))
                link_num["drug_substituent"] += 1
            else:
                notLink_DPPS["drug_substituent"].append((("drug", "substituent"), (i, j)))
                notlink_num["drug_substituent"] += 1

    # protein-disease
    for i in range(nums_drug):
        for j in range(nums_target):
            if adj_drug_target[i][j] == 1:
                link_DPPS["drug_target"].append((("drug", "target"), (i, j)))
                link_num["drug_target"] += 1
            else:
                notLink_DPPS["drug_target"].append((("drug", "target"), (i, j)))
                notlink_num["drug_target"] += 1

    for i in range(nums_target):
        for j in range(nums_go):
            if adj_target_go[i][j] == 1:
                link_DPPS["target_go"].append((("target", "go"), (i, j)))
                link_num["target_go"] += 1
            else:
                notLink_DPPS["target_go"].append((("target", "go"), (i, j)))
                notlink_num["target_go"] += 1






    graph_DPPNode += random.sample(link_DPPS["drug_chemical"], len(link_DPPS["drug_chemical"]))
    graph_DPPNode += random.sample(notLink_DPPS["drug_chemical"], len(link_DPPS["drug_chemical"]))
    graph_DPPNode += random.sample(link_DPPS["drug_sideeffects"], len(link_DPPS["drug_sideeffects"]))
    graph_DPPNode += random.sample(notLink_DPPS["drug_sideeffects"], len(link_DPPS["drug_sideeffects"]))
    graph_DPPNode += random.sample(link_DPPS["drug_substituent"], len(link_DPPS["drug_substituent"]))
    graph_DPPNode += random.sample(notLink_DPPS["drug_substituent"], len(link_DPPS["drug_substituent"]))
    graph_DPPNode += random.sample(link_DPPS["drug_target"], len(link_DPPS["drug_target"]))
    graph_DPPNode += random.sample(notLink_DPPS["drug_target"], len(link_DPPS["drug_target"]))
    graph_DPPNode += random.sample(link_DPPS["target_go"], len(link_DPPS["target_go"]))
    graph_DPPNode += random.sample(notLink_DPPS["target_go"], len(link_DPPS["target_go"]))

    '''
    temp = graph_DPPNode[-1]
    graph_DPPNode[-1] = graph_DPPNode[-2]
    graph_DPPNode[-2] = temp
    '''

    node_labels += [[1] for _ in range(len(link_DPPS["drug_chemical"]))]
    node_labels += [[0] for _ in range(len(link_DPPS["drug_chemical"]))]
    node_labels += [[1] for _ in range(len(link_DPPS["drug_sideeffects"]))]
    node_labels += [[0] for _ in range(len(link_DPPS["drug_sideeffects"]))]
    node_labels += [[1] for _ in range(len(link_DPPS["drug_substituent"]))]
    node_labels += [[0] for _ in range(len(link_DPPS["drug_substituent"]))]
    node_labels += [[1] for _ in range(len(link_DPPS["drug_target"]))]
    node_labels += [[0] for _ in range(len(link_DPPS["drug_target"]))]
    node_labels += [[1] for _ in range(len(link_DPPS["target_go"]))]
    node_labels += [[0] for _ in range(len(link_DPPS["target_go"]))]


    graph_DPPNode = [(i, item) for i, item in enumerate(graph_DPPNode)]

    lis_link_source = []
    lis_link_sink = []
    lis_embedding = []


    num = 0
    for i in graph_DPPNode:
        if num % 100 == 0:
            print(num)
        if i[1][0] == ("drug", "chemical"):
            for j in graph_DPPNode[:576577]:
                if i[1][1][0] == j[1][1][0] or i[1][1][1] == j[1][1][1]:
                    if i[0] != j[0]:
                        lis_link_source.append(i[0])
                        lis_link_sink.append(j[0])
        elif i[1][0] == ("drug", "sideeffects"):
            for j in graph_DPPNode[:576577]:
                if i[1][1][0] == j[1][1][0] or i[1][1][1] == j[1][1][1]:
                    if i[0] != j[0]:
                        lis_link_source.append(i[0])
                        lis_link_sink.append(j[0])
        elif i[1][0] == ("drug", "substituent"):
            for j in graph_DPPNode[:576577]:
                if i[1][1][0] == j[1][1][0] or i[1][1][1] == j[1][1][1]:
                    if i[0] != j[0]:
                        lis_link_source.append(i[0])
                        lis_link_sink.append(j[0])
        elif i[1][0] == ("drug", "target"):
            for j in graph_DPPNode:
                if i[1][1][0] == j[1][1][0] or i[1][1][1] == j[1][1][1]:
                    if i[0] != j[0]:
                        lis_link_source.append(i[0])
                        lis_link_sink.append(j[0])
                elif j[0] >= 576578:
                    if i[1][1][1] == j[1][1][0]:
                        lis_link_source.append(i[0])
                        lis_link_sink.append(j[0])
        elif i[1][0] == ("target", "go"):
            for j in graph_DPPNode[554940:]:
                if i[1][1][0] == j[1][1][0] or i[1][1][1] == j[1][1][1] or i[1][1][0] == j[1][1][1] or i[1][1][1] == j[1][1][0]:
                    if i[0] != j[0]:
                        lis_link_source.append(i[0])
                        lis_link_sink.append(j[0])
        num += 1





    for i,j in (graph_DPPNode):
        if j[0][0] == "drug" and j[0][1] == "chemical":
            em = torch.cat((embedding_drug[j[1][0]],embedding_chemical[j[1][1]]),dim=0)
        elif j[0][0] == "drug" and j[0][1] == "sideeffects":
            em = torch.cat((embedding_drug[j[1][0]], embedding_sideeffects[j[1][1]]), dim=0)
        elif j[0][0] == "drug" and j[0][1] == "substituent":
            em = torch.cat((embedding_drug[j[1][0]], embedding_substituent[j[1][1]]), dim=0)
        elif j[0][0] == "drug" and j[0][1] == "target":
            em = torch.cat((embedding_drug[j[1][0]], embedding_target[j[1][1]]), dim=0)
        elif j[0][0] == "target" and j[0][1] == "go":
            em = torch.cat((embedding_target[j[1][0]], embedding_go[j[1][1]]), dim=0)
        # em = torch.randn(1024)  消融
        lis_embedding.append(em)

    g = dgl.graph((lis_link_source, lis_link_sink))
    node_labels = torch.tensor(node_labels)
    g.ndata['label'] = node_labels
    lis_embedding= torch.tensor([item.cpu().detach().numpy() for item in lis_embedding])
    g.ndata['feature'] = lis_embedding
    save_path = f"../graph_dti/zheng_graph_dti/n(6,3)_all_link_random/init_graph_all"
    save_graphs(save_path, [g])

save_graph()
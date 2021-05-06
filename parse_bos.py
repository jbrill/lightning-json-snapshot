import json

with open("graph_data.json", encoding='utf-8-sig') as json_file:
    raw_data = json.load(json_file)
    node_data = raw_data.get("nodes")
    channel_data = raw_data.get("links")

with open("bos_data.json", encoding='utf-8-sig') as json_file:
    bos_data = json.load(json_file)
    bos_nodes = [id["publicKey"] for id in bos_data.get("data")]

# from pprint import pprint
# pprint(channel_data)
graph_data = {"nodes": [], "links": []}
for node in node_data:
    if node["id"] not in bos_nodes:
        graph_data["nodes"].append({
            "id": node["id"]
        }) 
        continue
    bos_idx = bos_nodes.index(node["id"])
    graph_data["nodes"].append({
        "id": node["id"],
        "score": bos_data.get("data")[bos_idx]["score"],
        "alias": bos_data.get("data")[bos_idx]["alias"],
        "percentile": (bos_data.get("data")[bos_idx]["score"] / 1000000),
    })


for channel in channel_data:
    # if (channel["source"] not in bos_nodes) or (channel["target"] not in bos_nodes):
    #     continue
    flag = False
    for sub_channel in graph_data["links"]:
        if (channel["source"] == sub_channel["source"] and channel["target"] == sub_channel["target"]):
            if flag is True:
                continue
            flag = True
    if flag is False:
        graph_data["links"].append(channel)

with open('graph_data_merged.json', 'w', encoding='utf-8') as f:
    json.dump(graph_data, f, ensure_ascii=False, indent=4)

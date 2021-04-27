import json

with open("channel-list.json", encoding='utf-8-sig') as json_file:
    channel_data = json.load(json_file)

# from pprint import pprint
# pprint(channel_data)

graph_data = {"nodes": [], "links": []}
for channel in channel_data:
    for node_id in channel["nodes"]:
        if node_id not in [
            existing_node['id'] for existing_node in graph_data["nodes"]
        ]:
            graph_data["nodes"].append({
                "id": node_id,
            })
    graph_data["links"].append({
        "source": channel["nodes"][0],
        "target": channel["nodes"][1],
    })

with open('graph_data.json', 'w', encoding='utf-8') as f:
    json.dump(graph_data, f, ensure_ascii=False, indent=4)

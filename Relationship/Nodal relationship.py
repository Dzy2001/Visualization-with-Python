from pyecharts import options as opts
from pyecharts.charts import Graph

nodes = [
    {"name": "nodal1", "symbolSize": 10},
    {"name": "nodal2", "symbolSize": 20},
    {"name": "nodal3", "symbolSize": 30},
    {"name": "nodal4", "symbolSize": 40},
    {"name": "nodal5", "symbolSize": 50},
    {"name": "nodal6", "symbolSize": 40},
    {"name": "nodal7", "symbolSize": 30},
    {"name": "nodal8", "symbolSize": 20},
]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get("name"), "target": j.get("name")})
c = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph——base"))
    .render("Simple example.html")
)

"""
Functions for corneto 0.9.1a0
"""


def plot(graph, format=None):
    import graphviz

    vertices, edges = graph.vertices, graph.edges
    custom_vertex = dict()
    custom_edge = dict()
    if format:
        # Add custom values per edge/vertex
        for v in vertices:
            value = format.get(v, 0)
            if value < 0:
                custom_vertex[v] = dict(
                    color="blue", penwidth="2", fillcolor="azure2", style="filled"
                )
            elif value > 0:
                custom_vertex[v] = dict(
                    color="red",
                    penwidth="2",
                    fillcolor="lightcoral",
                    style="filled",
                )
        for e in edges:
            value = format.get(e, 0)
            if value < 0:
                custom_edge[e] = dict(color="blue", penwidth="2")
            elif value > 0:
                custom_edge[e] = dict(color="red", penwidth="2")

    node_attr = dict(fixedsize="true")
    g = graphviz.Digraph(node_attr=node_attr)
    for e, p in zip(edges, graph.edge_properties):
        s, t = e
        s = list(s)
        if len(s) == 0:
            s = f"*_{str(t)}"
            g.node(s, shape="point")
        elif len(s) == 1:
            s = str(s[0])
            props = custom_vertex.get(s, dict())
            g.node(s, shape="circle", **props)
        else:
            raise NotImplementedError("Represent- hyperedges as composite edges")
        t = list(t)
        if len(t) == 0:
            t = f"{str(s)}_*"
            g.node(t, shape="point")
        elif len(t) == 1:
            t = str(t[0])
            props = custom_vertex.get(t, dict())
            g.node(t, shape="circle", **props)
        edge_type = p.get("interaction", 0)
        props = custom_edge.get(e, dict())
        if edge_type >= 0:
            g.edge(s, t, arrowhead="normal", **props)
        else:
            g.edge(s, t, arrowhead="tee", **props)
    return g


def get_problem_values(graph, problem, condition=None):
    values = dict()
    if condition is None:
        condition = "c0"
    vertex_values = (
        problem.symbols[f"species_activated_{condition}"].value
        - problem.symbols[f"species_inhibited_{condition}"].value
    )
    edge_values = (
        problem.symbols[f"reaction_sends_activation_{condition}"].value
        - problem.symbols[f"reaction_sends_inhibition_{condition}"].value
    )
    for v, val in zip(graph.vertices, vertex_values):
        values[v] = val
    for e, val in zip(graph.edges, edge_values):
        values[e] = val
    return values


def get_selected_edges_and_nodes(graph, problem):
    sel_edges = (
        problem.symbols["reaction_sends_activation_c0"].value
        + problem.symbols["reaction_sends_inhibition_c0"].value
    )
    sel_vertices = (
        problem.symbols["species_activated_c0"].value
        + problem.symbols["species_inhibited_c0"].value
    )
    ge = graph.edges
    ge = [ge[i] for i, v in enumerate(sel_edges) if v > 0]
    ve = graph.vertices
    ve = [ve[i] for i, v in enumerate(sel_vertices) if v > 0]
    return ge, ve


def set_problem_value(problem, graph, node, value):
    p = problem.copy()
    index = graph.vertices.index(node)
    if value > 0:
        node_values = p.symbols["species_activated_c0"]
        p += node_values[index] == 1
    elif value < 0:
        node_values = p.symbols["species_inhibited_c0"]
        p += node_values[index] == 1
    else:
        node_values = p.symbols["species_activated_c0"]
        p += node_values[index] == 0
        node_values = p.symbols["species_inhibited_c0"]
        p += node_values[index] == 0
    return p

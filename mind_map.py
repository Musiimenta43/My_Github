import dash #this is the main library used for building web apps in python
import dash_cytoscape as cyto #this is for creating interactive mind maps
from dash import html,dcc, Input, Output
app = dash.Dash(__name__) #intialize the dash app
nodes = [
    {"data": {"id": "Title", "label": "TITLE"}, "position": {"x": 375, "y": 250}},
    {"data": {"id": "Aim", "label": "Aim or Goal"}, "position": {"x": 200, "y": 100}},
    {"data": {"id": "Objectives", "label": "Objectives"}, "position": {"x": 550, "y": 100}},
    {"data": {"id": "LitReview", "label": "Literature Review"}, "position": {"x": 550, "y": 200}},
    {"data": {"id": "Methodology", "label": " Methodology"}, "position": {"x": 550, "y": 300}},
    {"data": {"id": "Results", "label": "Results"}, "position": {"x": 375, "y": 400}},
    {"data": {"id": "Analysis", "label": "Analysis"}, "position": {"x": 200, "y": 300}},
    {"data": {"id": "Limitations", "label": "Limitations"}, "position": {"x": 200, "y": 200}},
    {"data": {"id": "Conclusion", "label": "Conclusion & Recommendations"}, "position": {"x": 200, "y": 400}},
    ]
edges = [
    {"data":  {"source": "Title", "target": "Aim"}},
    {"data":  {"source": "Title", "target": "Objectives"}},
    {"data":  {"source": "Title", "target": "LitReview"}},
    {"data":  {"source": "Title", "target": "Methodology"}},
    {"data":  {"source": "Title", "target": "Results"}},
    {"data":  {"source": "Title", "target": "Analysis"}},
    {"data":  {"source": "Title", "target": "Limitations"}},
    {"data":  {"source": "Title", "target": "Conclusion"}},
    ]
app.layout = html.Div([
    html.H3("Interactive Mind Map"),
    cyto.Cytoscape(
        id="cytoscape",
        elements= nodes + edges,
        style={"width": "100%", "height": "500px"},
        layout={"name": "preset"},
        stylesheet=[
            {"selector": 'node', "style": {"label": "data(label)"}},
            {"selector": 'edge', "style": {"curve-style": "bezier", "target arrow-shape": "triangle"}}
        ]
    ),
    html.Br(),
    html.Div(id='node-info', style={'fontSize': 20, 'color': 'blue'}),
    html.Br(),
    dcc.Input(id='node-edit', type='text', placeholder='Edit Node Label', debounce=True),
    html.Button("Update", id="update-button", n_clicks=0)
])
Output('node-info', 'children'),
Input('cytoscape', 'tapNodeData')

def display_node_info(node_data):
    if node_data:
        return f"Clicked Node: {node_data['label']}"
        return "Click a node to see deatils."
        @app.callback(
            Output('cytoscape', 'elements'),
            [Input('update_button', 'n_clicks')],
            [Input('cytoscape', 'tapNodeData'), Input('node-edit', 'value')]
        )
def edit_node_label(n_clicks, node_data, new_label):
    if n_clicks > 0 and node-data and new_label:
        for node in nodes:
            if node["data"]["id"] == node_data["id"]:
                node["data"]["label"] = new_label
                break
                return nodes + edges
                return nodes + edges
if __name__ == '__main__':
    app.run_server(debug=True)
            

        )
    ])
if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
    
    

import dash #this is the main library used for building web apps in python
import dash_cytoscape as cyto #this is for creating interactive mind maps
from dash import html
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
    html.H1("Research Mind Map"),
    cyto.Cytoscape(
        id="cytoscape",
        elements= nodes + edges,
        style={"width": "100%", "height": "500px"},
        layout={"name": "preset"},
        )
    ])
if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
    
    

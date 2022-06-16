from dash_app import app


def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#title", timeout=10)


def test_graph(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualization", timeout=10)


def test_region_picker(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("region", timeout=10)

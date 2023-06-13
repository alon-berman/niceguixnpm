from nicegui import ui, app

from components.counter.counter import Counter
from components.leaderline.leader_line import LeaderLine


# Important to have external npm modules. In this case, leader-line
app.add_static_files("/node_modules", "node_modules")

ui.markdown('''
#### neat.
''')
ui.add_head_html(f'''
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">

</head>
<body>
    
  <script src="node_modules/leader-line/leader-line.min.js"></script>
  <div id="start" style="color: red; width:80px; height:20px;">start</div>
  <div id="end" style="margin: 160px 0 0 240px; color: blue; width: 80px">end</div>

</body>
</html>
''')

with ui.card():
    leader = LeaderLine('start', 'end', 'blue', size=2, on_show=ui.card)
    counter = Counter('Clicks', on_change=lambda msg: ui.notify(f'The value changed to {msg["args"]}.'))

ui.button('Reset', on_click=counter.reset).props('small outline')

ui.run(port=1234)
{"filter":false,"title":"settings.py","tooltip":"/django_todo/settings.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":[" "],"id":35}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":22},"action":"insert","lines":["dj_database_url"],"id":36}],[{"start":{"row":84,"column":47},"end":{"row":85,"column":1},"action":"remove","lines":["postgres://ptolycsujunxhe:15c05ecda410b11dfd943c9e92ac9f06afa88cdc4de21b3bfbc7b8298cc9b7c5@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d47n3fm8rtvugs"," "],"id":37}],[{"start":{"row":84,"column":47},"end":{"row":84,"column":207},"action":"insert","lines":["postgres://ptolycsujunxhe:15c05ecda410b11dfd943c9e92ac9f06afa88cdc4de21b3bfbc7b8298cc9b7c5@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d47n3fm8rtvugs"],"id":38}],[{"start":{"row":83,"column":0},"end":{"row":83,"column":161},"action":"insert","lines":["postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562"],"id":39}],[{"start":{"row":84,"column":47},"end":{"row":84,"column":207},"action":"remove","lines":["postgres://ptolycsujunxhe:15c05ecda410b11dfd943c9e92ac9f06afa88cdc4de21b3bfbc7b8298cc9b7c5@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d47n3fm8rtvugs"],"id":40}],[{"start":{"row":84,"column":47},"end":{"row":84,"column":208},"action":"insert","lines":["postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562"],"id":41}],[{"start":{"row":82,"column":2},"end":{"row":83,"column":161},"action":"remove","lines":["","postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562"],"id":42}],[{"start":{"row":16,"column":70},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":43},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":19,"column":0},"end":{"row":29,"column":1},"action":"insert","lines":["BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.9/howto/static-files/","STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')","STATIC_URL = '/static/'","","# Extra places for collectstatic to find static files.","STATICFILES_DIRS = (","    os.path.join(BASE_DIR, 'static'),",")"],"id":44}],[{"start":{"row":18,"column":0},"end":{"row":20,"column":0},"action":"remove","lines":["","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))",""],"id":45}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":23},"action":"remove","lines":["STATIC_URL = '/static/'"],"id":46}],[{"start":{"row":11,"column":0},"end":{"row":23,"column":72},"action":"insert","lines":["# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))","STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')","STATIC_URL = '/static/'","","# Extra lookup directories for collectstatic to find static files","STATICFILES_DIRS = (","    os.path.join(PROJECT_ROOT, 'static'),",")","","#  Add configuration for static files storage using whitenoise","STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'"],"id":47}],[{"start":{"row":23,"column":72},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":58},"action":"remove","lines":["PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))","STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')"],"id":49}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":23},"action":"remove","lines":["STATIC_URL = '/static/'"],"id":50}],[{"start":{"row":15,"column":0},"end":{"row":20,"column":0},"action":"remove","lines":["","# Extra lookup directories for collectstatic to find static files","STATICFILES_DIRS = (","    os.path.join(PROJECT_ROOT, 'static'),",")",""],"id":51}],[{"start":{"row":16,"column":2},"end":{"row":19,"column":0},"action":"remove","lines":[" Add configuration for static files storage using whitenoise","STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'","",""],"id":52},{"start":{"row":16,"column":1},"end":{"row":16,"column":2},"action":"remove","lines":[" "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["#"]}],[{"start":{"row":100,"column":47},"end":{"row":100,"column":208},"action":"remove","lines":["postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562"],"id":53}],[{"start":{"row":100,"column":47},"end":{"row":100,"column":208},"action":"insert","lines":["postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562"],"id":54}],[{"start":{"row":45,"column":86},"end":{"row":45,"column":87},"action":"insert","lines":[","],"id":55}],[{"start":{"row":45,"column":87},"end":{"row":45,"column":88},"action":"insert","lines":[" "],"id":56}],[{"start":{"row":45,"column":88},"end":{"row":45,"column":90},"action":"insert","lines":["''"],"id":57}],[{"start":{"row":45,"column":89},"end":{"row":45,"column":134},"action":"insert","lines":["https://django-simple-todo-app.herokuapp.com/"],"id":58}],[{"start":{"row":45,"column":96},"end":{"row":45,"column":97},"action":"remove","lines":["/"],"id":59},{"start":{"row":45,"column":95},"end":{"row":45,"column":96},"action":"remove","lines":["/"]},{"start":{"row":45,"column":94},"end":{"row":45,"column":95},"action":"remove","lines":[":"]},{"start":{"row":45,"column":93},"end":{"row":45,"column":94},"action":"remove","lines":["s"]},{"start":{"row":45,"column":92},"end":{"row":45,"column":93},"action":"remove","lines":["p"]},{"start":{"row":45,"column":91},"end":{"row":45,"column":92},"action":"remove","lines":["t"]},{"start":{"row":45,"column":90},"end":{"row":45,"column":91},"action":"remove","lines":["t"]},{"start":{"row":45,"column":89},"end":{"row":45,"column":90},"action":"remove","lines":["h"]}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["",""],"id":60},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":41,"column":88},"end":{"row":41,"column":127},"action":"remove","lines":["'django-simple-todo-app.herokuapp.com/'"],"id":61}],[{"start":{"row":41,"column":88},"end":{"row":41,"column":126},"action":"insert","lines":["'django-simple-todo-app.herokuapp.com'"],"id":62}],[{"start":{"row":41,"column":88},"end":{"row":41,"column":89},"action":"remove","lines":["'"],"id":63}],[{"start":{"row":41,"column":88},"end":{"row":41,"column":89},"action":"insert","lines":["\""],"id":64}],[{"start":{"row":41,"column":125},"end":{"row":41,"column":126},"action":"remove","lines":["'"],"id":65}],[{"start":{"row":41,"column":125},"end":{"row":41,"column":126},"action":"insert","lines":["\""],"id":66}],[{"start":{"row":41,"column":126},"end":{"row":41,"column":127},"action":"insert","lines":[" "],"id":67}],[{"start":{"row":41,"column":126},"end":{"row":41,"column":127},"action":"remove","lines":[" "],"id":68},{"start":{"row":41,"column":125},"end":{"row":41,"column":126},"action":"remove","lines":["\""]}],[{"start":{"row":41,"column":125},"end":{"row":41,"column":126},"action":"insert","lines":["\""],"id":69}],[{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"remove","lines":["'"],"id":70}],[{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"insert","lines":["\""],"id":71}],[{"start":{"row":41,"column":85},"end":{"row":41,"column":86},"action":"remove","lines":["'"],"id":72}],[{"start":{"row":41,"column":85},"end":{"row":41,"column":86},"action":"insert","lines":["\""],"id":73}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":1},"action":"insert","lines":["h"],"id":75},{"start":{"row":43,"column":1},"end":{"row":43,"column":2},"action":"insert","lines":["o"]},{"start":{"row":43,"column":2},"end":{"row":43,"column":3},"action":"insert","lines":["s"]}],[{"start":{"row":43,"column":3},"end":{"row":43,"column":4},"action":"insert","lines":["t"],"id":76}],[{"start":{"row":43,"column":4},"end":{"row":43,"column":5},"action":"insert","lines":[" "],"id":77},{"start":{"row":43,"column":5},"end":{"row":43,"column":6},"action":"insert","lines":["="]}],[{"start":{"row":43,"column":6},"end":{"row":43,"column":7},"action":"insert","lines":[" "],"id":78},{"start":{"row":43,"column":7},"end":{"row":43,"column":8},"action":"insert","lines":["o"]},{"start":{"row":43,"column":8},"end":{"row":43,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":43,"column":9},"end":{"row":43,"column":10},"action":"insert","lines":["."],"id":79},{"start":{"row":43,"column":10},"end":{"row":43,"column":11},"action":"insert","lines":["e"]},{"start":{"row":43,"column":11},"end":{"row":43,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":43,"column":10},"end":{"row":43,"column":12},"action":"remove","lines":["en"],"id":80},{"start":{"row":43,"column":10},"end":{"row":43,"column":17},"action":"insert","lines":["environ"]}],[{"start":{"row":43,"column":17},"end":{"row":43,"column":18},"action":"insert","lines":["."],"id":81},{"start":{"row":43,"column":18},"end":{"row":43,"column":19},"action":"insert","lines":["g"]}],[{"start":{"row":43,"column":19},"end":{"row":43,"column":20},"action":"insert","lines":["e"],"id":82},{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":43,"column":18},"end":{"row":43,"column":21},"action":"remove","lines":["get"],"id":83},{"start":{"row":43,"column":18},"end":{"row":43,"column":23},"action":"insert","lines":["get()"]}],[{"start":{"row":43,"column":22},"end":{"row":43,"column":24},"action":"insert","lines":["''"],"id":84}],[{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"insert","lines":["S"],"id":85},{"start":{"row":43,"column":24},"end":{"row":43,"column":25},"action":"insert","lines":["I"]},{"start":{"row":43,"column":25},"end":{"row":43,"column":26},"action":"insert","lines":["T"]},{"start":{"row":43,"column":26},"end":{"row":43,"column":27},"action":"insert","lines":["E"]}],[{"start":{"row":43,"column":27},"end":{"row":43,"column":28},"action":"insert","lines":["_"],"id":86}],[{"start":{"row":43,"column":28},"end":{"row":43,"column":29},"action":"insert","lines":["H"],"id":87},{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["O"]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"insert","lines":["S"]},{"start":{"row":43,"column":31},"end":{"row":43,"column":32},"action":"insert","lines":["T"]}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":34},"action":"remove","lines":["host = os.environ.get('SITE_HOST')"],"id":88}],[{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"insert","lines":["o"],"id":89},{"start":{"row":41,"column":18},"end":{"row":41,"column":19},"action":"insert","lines":["s"]},{"start":{"row":41,"column":19},"end":{"row":41,"column":20},"action":"insert","lines":["."]}],[{"start":{"row":41,"column":20},"end":{"row":41,"column":21},"action":"insert","lines":["e"],"id":90},{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"insert","lines":["n"]},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["v"]}],[{"start":{"row":41,"column":20},"end":{"row":41,"column":23},"action":"remove","lines":["env"],"id":91},{"start":{"row":41,"column":20},"end":{"row":41,"column":27},"action":"insert","lines":["environ"]}],[{"start":{"row":41,"column":27},"end":{"row":41,"column":28},"action":"insert","lines":["."],"id":92}],[{"start":{"row":41,"column":28},"end":{"row":41,"column":33},"action":"insert","lines":["get()"],"id":93}],[{"start":{"row":41,"column":32},"end":{"row":41,"column":33},"action":"insert","lines":["C"],"id":94},{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"insert","lines":["9"]}],[{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"remove","lines":["9"],"id":95},{"start":{"row":41,"column":32},"end":{"row":41,"column":33},"action":"remove","lines":["C"]}],[{"start":{"row":41,"column":32},"end":{"row":41,"column":34},"action":"insert","lines":["''"],"id":96}],[{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"insert","lines":["C"],"id":97},{"start":{"row":41,"column":34},"end":{"row":41,"column":35},"action":"insert","lines":["9"]}],[{"start":{"row":41,"column":35},"end":{"row":41,"column":36},"action":"insert","lines":["_"],"id":98}],[{"start":{"row":41,"column":36},"end":{"row":41,"column":37},"action":"insert","lines":["H"],"id":99}],[{"start":{"row":41,"column":37},"end":{"row":41,"column":38},"action":"insert","lines":["o"],"id":100},{"start":{"row":41,"column":38},"end":{"row":41,"column":39},"action":"insert","lines":["s"]},{"start":{"row":41,"column":39},"end":{"row":41,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":41,"column":40},"end":{"row":41,"column":41},"action":"insert","lines":["n"],"id":101},{"start":{"row":41,"column":41},"end":{"row":41,"column":42},"action":"insert","lines":["a"]},{"start":{"row":41,"column":42},"end":{"row":41,"column":43},"action":"insert","lines":["m"]}],[{"start":{"row":41,"column":42},"end":{"row":41,"column":43},"action":"remove","lines":["m"],"id":102},{"start":{"row":41,"column":41},"end":{"row":41,"column":42},"action":"remove","lines":["a"]},{"start":{"row":41,"column":40},"end":{"row":41,"column":41},"action":"remove","lines":["n"]},{"start":{"row":41,"column":39},"end":{"row":41,"column":40},"action":"remove","lines":["t"]},{"start":{"row":41,"column":38},"end":{"row":41,"column":39},"action":"remove","lines":["s"]},{"start":{"row":41,"column":37},"end":{"row":41,"column":38},"action":"remove","lines":["o"]}],[{"start":{"row":41,"column":37},"end":{"row":41,"column":38},"action":"insert","lines":["O"],"id":103},{"start":{"row":41,"column":38},"end":{"row":41,"column":39},"action":"insert","lines":["S"]},{"start":{"row":41,"column":39},"end":{"row":41,"column":40},"action":"insert","lines":["T"]},{"start":{"row":41,"column":40},"end":{"row":41,"column":41},"action":"insert","lines":["N"]},{"start":{"row":41,"column":41},"end":{"row":41,"column":42},"action":"insert","lines":["A"]},{"start":{"row":41,"column":42},"end":{"row":41,"column":43},"action":"insert","lines":["M"]},{"start":{"row":41,"column":43},"end":{"row":41,"column":44},"action":"insert","lines":["E"]}],[{"start":{"row":41,"column":46},"end":{"row":41,"column":155},"action":"remove","lines":["\"6de882e1a3214cf4bdbf7bc44a909c1e.vfs.cloud9.us-east-1.amazonaws.com\", \"django-simple-todo-app.herokuapp.com\""],"id":104}],[{"start":{"row":41,"column":46},"end":{"row":41,"column":47},"action":"insert","lines":[","],"id":105}],[{"start":{"row":41,"column":47},"end":{"row":41,"column":48},"action":"insert","lines":[" "],"id":106}],[{"start":{"row":41,"column":48},"end":{"row":41,"column":77},"action":"insert","lines":["os.environ.get('C9_HOSTNAME')"],"id":107}],[{"start":{"row":41,"column":66},"end":{"row":41,"column":67},"action":"remove","lines":["_"],"id":108},{"start":{"row":41,"column":65},"end":{"row":41,"column":66},"action":"remove","lines":["9"]},{"start":{"row":41,"column":64},"end":{"row":41,"column":65},"action":"remove","lines":["C"]}],[{"start":{"row":96,"column":46},"end":{"row":96,"column":209},"action":"remove","lines":["\"postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562\""],"id":109}],[{"start":{"row":96,"column":46},"end":{"row":96,"column":72},"action":"insert","lines":["os.environ.get('HOSTNAME')"],"id":110}],[{"start":{"row":96,"column":69},"end":{"row":96,"column":70},"action":"remove","lines":["E"],"id":111},{"start":{"row":96,"column":68},"end":{"row":96,"column":69},"action":"remove","lines":["M"]},{"start":{"row":96,"column":67},"end":{"row":96,"column":68},"action":"remove","lines":["A"]},{"start":{"row":96,"column":66},"end":{"row":96,"column":67},"action":"remove","lines":["N"]},{"start":{"row":96,"column":65},"end":{"row":96,"column":66},"action":"remove","lines":["T"]},{"start":{"row":96,"column":64},"end":{"row":96,"column":65},"action":"remove","lines":["S"]},{"start":{"row":96,"column":63},"end":{"row":96,"column":64},"action":"remove","lines":["O"]},{"start":{"row":96,"column":62},"end":{"row":96,"column":63},"action":"remove","lines":["H"]}],[{"start":{"row":96,"column":62},"end":{"row":96,"column":63},"action":"insert","lines":["D"],"id":112},{"start":{"row":96,"column":63},"end":{"row":96,"column":64},"action":"insert","lines":["A"]},{"start":{"row":96,"column":64},"end":{"row":96,"column":65},"action":"insert","lines":["T"]},{"start":{"row":96,"column":65},"end":{"row":96,"column":66},"action":"insert","lines":["A"]},{"start":{"row":96,"column":66},"end":{"row":96,"column":67},"action":"insert","lines":["B"]},{"start":{"row":96,"column":67},"end":{"row":96,"column":68},"action":"insert","lines":["A"]},{"start":{"row":96,"column":68},"end":{"row":96,"column":69},"action":"insert","lines":["S"]},{"start":{"row":96,"column":69},"end":{"row":96,"column":70},"action":"insert","lines":["E"]}],[{"start":{"row":96,"column":70},"end":{"row":96,"column":71},"action":"insert","lines":["_"],"id":113},{"start":{"row":96,"column":71},"end":{"row":96,"column":72},"action":"insert","lines":["U"]},{"start":{"row":96,"column":72},"end":{"row":96,"column":73},"action":"insert","lines":["R"]},{"start":{"row":96,"column":73},"end":{"row":96,"column":74},"action":"insert","lines":["L"]}],[{"start":{"row":96,"column":46},"end":{"row":96,"column":48},"action":"insert","lines":["\"p"],"id":114},{"start":{"row":96,"column":50},"end":{"row":96,"column":156},"action":"insert","lines":["tgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214"]},{"start":{"row":96,"column":158},"end":{"row":96,"column":162},"action":"remove","lines":["nvir"]},{"start":{"row":96,"column":158},"end":{"row":96,"column":179},"action":"insert","lines":["u-west-1.compute.amaz"]},{"start":{"row":96,"column":181},"end":{"row":96,"column":184},"action":"insert","lines":["aws"]},{"start":{"row":96,"column":185},"end":{"row":96,"column":204},"action":"remove","lines":["get('DATABASE_URL')"]},{"start":{"row":96,"column":185},"end":{"row":96,"column":209},"action":"insert","lines":["com:5432/daj1rlf3h5q562\""]}],[{"start":{"row":96,"column":46},"end":{"row":96,"column":209},"action":"remove","lines":["\"postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562\""],"id":115}],[{"start":{"row":96,"column":46},"end":{"row":96,"column":47},"action":"insert","lines":["o"],"id":116},{"start":{"row":96,"column":47},"end":{"row":96,"column":48},"action":"insert","lines":["s"]},{"start":{"row":96,"column":48},"end":{"row":96,"column":49},"action":"insert","lines":["."]},{"start":{"row":96,"column":49},"end":{"row":96,"column":50},"action":"insert","lines":["e"]},{"start":{"row":96,"column":50},"end":{"row":96,"column":51},"action":"insert","lines":["n"]}],[{"start":{"row":96,"column":49},"end":{"row":96,"column":51},"action":"remove","lines":["en"],"id":117},{"start":{"row":96,"column":49},"end":{"row":96,"column":56},"action":"insert","lines":["environ"]}],[{"start":{"row":96,"column":56},"end":{"row":96,"column":58},"action":"insert","lines":["()"],"id":118}],[{"start":{"row":96,"column":57},"end":{"row":96,"column":59},"action":"insert","lines":["\"\""],"id":119}],[{"start":{"row":96,"column":58},"end":{"row":96,"column":59},"action":"insert","lines":["C"],"id":120},{"start":{"row":96,"column":59},"end":{"row":96,"column":60},"action":"insert","lines":["9"]},{"start":{"row":96,"column":60},"end":{"row":96,"column":61},"action":"insert","lines":["_"]}],[{"start":{"row":96,"column":61},"end":{"row":96,"column":62},"action":"insert","lines":["O"],"id":121}],[{"start":{"row":96,"column":61},"end":{"row":96,"column":62},"action":"remove","lines":["O"],"id":122}],[{"start":{"row":96,"column":58},"end":{"row":96,"column":61},"action":"remove","lines":["C9_"],"id":123},{"start":{"row":96,"column":58},"end":{"row":96,"column":69},"action":"insert","lines":["C9_HOSTNAME"]}],[{"start":{"row":96,"column":71},"end":{"row":96,"column":72},"action":"insert","lines":[","],"id":124}],[{"start":{"row":96,"column":72},"end":{"row":96,"column":73},"action":"insert","lines":[" "],"id":125}],[{"start":{"row":96,"column":73},"end":{"row":96,"column":74},"action":"insert","lines":["o"],"id":126},{"start":{"row":96,"column":74},"end":{"row":96,"column":75},"action":"insert","lines":["s"]},{"start":{"row":96,"column":75},"end":{"row":96,"column":76},"action":"insert","lines":["."]},{"start":{"row":96,"column":76},"end":{"row":96,"column":77},"action":"insert","lines":["e"]}],[{"start":{"row":96,"column":76},"end":{"row":96,"column":77},"action":"remove","lines":["e"],"id":127},{"start":{"row":96,"column":76},"end":{"row":96,"column":83},"action":"insert","lines":["environ"]}],[{"start":{"row":96,"column":83},"end":{"row":96,"column":85},"action":"insert","lines":["()"],"id":128}],[{"start":{"row":96,"column":84},"end":{"row":96,"column":86},"action":"insert","lines":["\"\""],"id":129}],[{"start":{"row":96,"column":85},"end":{"row":96,"column":93},"action":"insert","lines":["HOSTNAME"],"id":130}],[{"start":{"row":96,"column":71},"end":{"row":96,"column":95},"action":"remove","lines":[", os.environ(\"HOSTNAME\")"],"id":131}],[{"start":{"row":96,"column":68},"end":{"row":96,"column":69},"action":"remove","lines":["E"],"id":132},{"start":{"row":96,"column":67},"end":{"row":96,"column":68},"action":"remove","lines":["M"]},{"start":{"row":96,"column":66},"end":{"row":96,"column":67},"action":"remove","lines":["A"]},{"start":{"row":96,"column":65},"end":{"row":96,"column":66},"action":"remove","lines":["N"]},{"start":{"row":96,"column":64},"end":{"row":96,"column":65},"action":"remove","lines":["T"]},{"start":{"row":96,"column":63},"end":{"row":96,"column":64},"action":"remove","lines":["S"]},{"start":{"row":96,"column":62},"end":{"row":96,"column":63},"action":"remove","lines":["O"]},{"start":{"row":96,"column":61},"end":{"row":96,"column":62},"action":"remove","lines":["H"]},{"start":{"row":96,"column":60},"end":{"row":96,"column":61},"action":"remove","lines":["_"]},{"start":{"row":96,"column":59},"end":{"row":96,"column":60},"action":"remove","lines":["9"]},{"start":{"row":96,"column":58},"end":{"row":96,"column":59},"action":"remove","lines":["C"]}],[{"start":{"row":96,"column":58},"end":{"row":96,"column":59},"action":"insert","lines":["D"],"id":133},{"start":{"row":96,"column":59},"end":{"row":96,"column":60},"action":"insert","lines":["A"]},{"start":{"row":96,"column":60},"end":{"row":96,"column":61},"action":"insert","lines":["T"]},{"start":{"row":96,"column":61},"end":{"row":96,"column":62},"action":"insert","lines":["A"]},{"start":{"row":96,"column":62},"end":{"row":96,"column":63},"action":"insert","lines":["B"]},{"start":{"row":96,"column":63},"end":{"row":96,"column":64},"action":"insert","lines":["A"]},{"start":{"row":96,"column":64},"end":{"row":96,"column":65},"action":"insert","lines":["S"]},{"start":{"row":96,"column":65},"end":{"row":96,"column":66},"action":"insert","lines":["E"]}],[{"start":{"row":96,"column":66},"end":{"row":96,"column":67},"action":"insert","lines":["_"],"id":134},{"start":{"row":96,"column":67},"end":{"row":96,"column":68},"action":"insert","lines":["U"]},{"start":{"row":96,"column":68},"end":{"row":96,"column":69},"action":"insert","lines":["R"]},{"start":{"row":96,"column":69},"end":{"row":96,"column":70},"action":"insert","lines":["L"]}],[{"start":{"row":96,"column":56},"end":{"row":96,"column":57},"action":"insert","lines":["."],"id":135}],[{"start":{"row":96,"column":57},"end":{"row":96,"column":60},"action":"insert","lines":["get"],"id":136}]]},"ace":{"folds":[],"scrolltop":1387,"scrollleft":0,"selection":{"start":{"row":96,"column":60},"end":{"row":96,"column":60},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":80,"state":"start","mode":"ace/mode/python"}},"timestamp":1565118913305,"hash":"fb3b77c99d2eca5f02be288274091fdaf8ee7264"}
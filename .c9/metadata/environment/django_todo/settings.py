{"changed":true,"filter":false,"title":"settings.py","tooltip":"/django_todo/settings.py","value":"\"\"\"\nDjango settings for django_todo project.\n\nGenerated by 'django-admin startproject' using Django 1.11.\n\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.11/topics/settings/\n\nFor the full list of settings and their values, see\nhttps://docs.djangoproject.com/en/1.11/ref/settings/\n\"\"\"\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\nimport os\nimport dj_database_url\n\n\nif os.environ.get('DEVELOPMENT'):\n    development = True\nelse:\n    development = False\n\n    \n    \n# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\nBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.9/howto/static-files/\nSTATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')\n\n\n# Extra places for collectstatic to find static files.\nSTATICFILES_DIRS = (\n    os.path.join(BASE_DIR, 'static'),\n)\n\n\n# Quick-start development settings - unsuitable for production\n# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/\n\n# SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = os.environ.get('SECRET_KEY')\n\n# SECURITY WARNING: don't run with debug turned on in production!\n\nDEBUG = development\n\nALLOWED_HOSTS = ['django-simple-todo-app.herokuapp.com','6de882e1a3214cf4bdbf7bc44a909c1e.vfs.cloud9.us-east-1.amazonaws.com', os.environ.get('HOSTNAME')]\n\n\n# Application definition\n\nINSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    'todo'\n]\n\nMIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',\n    'django.contrib.sessions.middleware.SessionMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    'django.middleware.csrf.CsrfViewMiddleware',\n    'django.contrib.auth.middleware.AuthenticationMiddleware',\n    'django.contrib.messages.middleware.MessageMiddleware',\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n]\n\nROOT_URLCONF = 'django_todo.urls'\n\nTEMPLATES = [\n    {\n        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n        'DIRS': [],\n        'APP_DIRS': True,\n        'OPTIONS': {\n            'context_processors': [\n                'django.template.context_processors.debug',\n                'django.template.context_processors.request',\n                'django.contrib.auth.context_processors.auth',\n                'django.contrib.messages.context_processors.messages',\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = 'django_todo.wsgi.application'\n\n\n# Database\n# https://docs.djangoproject.com/en/1.11/ref/settings/#databases\nif development:\n    DATABASES = {\n       'default': {\n           'ENGINE': 'django.db.backends.sqlite3',\n            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n      }\n    }\nelse:\n    DATABASES = {'default': dj_database_url.parse(os.environ.get(\"DATABASE_URL\"))}\n\n\n# Password validation\n# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n    },\n]\n\n\n# Internationalization\n# https://docs.djangoproject.com/en/1.11/topics/i18n/\n\nLANGUAGE_CODE = 'en-us'\n\nTIME_ZONE = 'UTC'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\nSTATIC_URL = '/static/'\n","undoManager":{"mark":87,"position":100,"stack":[[{"start":{"row":41,"column":17},"end":{"row":41,"column":46},"action":"remove","lines":["os.environ.get('C9_HOSTNAME')"],"id":137},{"start":{"row":41,"column":17},"end":{"row":41,"column":55},"action":"insert","lines":["'django-simple-todo-app.herokuapp.com'"]}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"insert","lines":["h"],"id":138}],[{"start":{"row":41,"column":85},"end":{"row":41,"column":86},"action":"insert","lines":["h"],"id":139}],[{"start":{"row":41,"column":85},"end":{"row":41,"column":86},"action":"remove","lines":["h"],"id":140}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"remove","lines":["h"],"id":141}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":142},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["",""],"id":143}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["i"],"id":144},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["f"]}],[{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":[" "],"id":145},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":["o"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["s"]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["."]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["n"],"id":146}],[{"start":{"row":18,"column":6},"end":{"row":18,"column":8},"action":"remove","lines":["en"],"id":147},{"start":{"row":18,"column":6},"end":{"row":18,"column":13},"action":"insert","lines":["environ"]}],[{"start":{"row":18,"column":13},"end":{"row":18,"column":15},"action":"insert","lines":["()"],"id":148}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["0"],"id":149}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["D"],"id":150},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["E"]},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["V"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["E"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["L"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["O"]}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["P"],"id":151},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":["M"]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["E"]},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["N"]}],[{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":["T"],"id":152}],[{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"remove","lines":["0"],"id":153}],[{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"insert","lines":["'"],"id":154}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["'"],"id":155}],[{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["."],"id":156}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":17},"action":"insert","lines":["get"],"id":157}],[{"start":{"row":18,"column":32},"end":{"row":18,"column":33},"action":"insert","lines":[":"],"id":158}],[{"start":{"row":18,"column":33},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":159},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":20,"column":0},"action":"insert","lines":["",""]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":21,"column":0},"action":"insert","lines":["",""]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["d"],"id":160},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["e"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["v"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["e"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["l"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["o"]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["p"]}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["m"],"id":161},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["e"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["n"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":[" "],"id":162},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":[" "],"id":163},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["T"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["r"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["u"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":22},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":164},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":165}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"insert","lines":["e"],"id":166},{"start":{"row":20,"column":1},"end":{"row":20,"column":2},"action":"insert","lines":["l"]},{"start":{"row":20,"column":2},"end":{"row":20,"column":3},"action":"insert","lines":["s"]},{"start":{"row":20,"column":3},"end":{"row":20,"column":4},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":4},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":167}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":[":"],"id":168}],[{"start":{"row":20,"column":5},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":169},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["d"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["v"],"id":170},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["e"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["l"]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["o"]},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["p"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["m"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["e"]},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["n"]},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":[" "],"id":171},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":[" "],"id":172},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["F"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["a"]}],[{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["l"],"id":173},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["s"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":46,"column":65},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":174},{"start":{"row":47,"column":0},"end":{"row":48,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":1},"action":"insert","lines":["i"],"id":175},{"start":{"row":48,"column":1},"end":{"row":48,"column":2},"action":"insert","lines":["d"]}],[{"start":{"row":48,"column":2},"end":{"row":48,"column":3},"action":"insert","lines":[" "],"id":176},{"start":{"row":48,"column":3},"end":{"row":48,"column":4},"action":"insert","lines":["d"]},{"start":{"row":48,"column":4},"end":{"row":48,"column":5},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":3},"end":{"row":48,"column":5},"action":"remove","lines":["de"],"id":177},{"start":{"row":48,"column":3},"end":{"row":48,"column":14},"action":"insert","lines":["development"]}],[{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"insert","lines":[" "],"id":178},{"start":{"row":48,"column":15},"end":{"row":48,"column":16},"action":"insert","lines":["i"]},{"start":{"row":48,"column":16},"end":{"row":48,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"insert","lines":[" "],"id":179},{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"insert","lines":["T"]},{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"insert","lines":["r"]},{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"insert","lines":["u"]},{"start":{"row":48,"column":21},"end":{"row":48,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":22},"end":{"row":48,"column":23},"action":"insert","lines":[":"],"id":180}],[{"start":{"row":48,"column":22},"end":{"row":48,"column":23},"action":"remove","lines":[":"],"id":181},{"start":{"row":48,"column":21},"end":{"row":48,"column":22},"action":"remove","lines":["e"]},{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"remove","lines":["u"]},{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"remove","lines":["r"]},{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"remove","lines":["T"]},{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"remove","lines":[" "]},{"start":{"row":48,"column":16},"end":{"row":48,"column":17},"action":"remove","lines":["s"]},{"start":{"row":48,"column":15},"end":{"row":48,"column":16},"action":"remove","lines":["i"]},{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"remove","lines":[" "]}],[{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"insert","lines":[":"],"id":182}],[{"start":{"row":48,"column":15},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":183},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":49,"column":4},"end":{"row":50,"column":0},"action":"remove","lines":["",""],"id":184}],[{"start":{"row":49,"column":15},"end":{"row":49,"column":16},"action":"remove","lines":["e"],"id":185},{"start":{"row":49,"column":14},"end":{"row":49,"column":15},"action":"remove","lines":["u"]},{"start":{"row":49,"column":13},"end":{"row":49,"column":14},"action":"remove","lines":["r"]},{"start":{"row":49,"column":12},"end":{"row":49,"column":13},"action":"remove","lines":["T"]}],[{"start":{"row":49,"column":12},"end":{"row":49,"column":13},"action":"insert","lines":["d"],"id":186},{"start":{"row":49,"column":13},"end":{"row":49,"column":14},"action":"insert","lines":["e"]},{"start":{"row":49,"column":14},"end":{"row":49,"column":15},"action":"insert","lines":["v"]},{"start":{"row":49,"column":15},"end":{"row":49,"column":16},"action":"insert","lines":["e"]},{"start":{"row":49,"column":16},"end":{"row":49,"column":17},"action":"insert","lines":["l"]},{"start":{"row":49,"column":17},"end":{"row":49,"column":18},"action":"insert","lines":["o"]},{"start":{"row":49,"column":18},"end":{"row":49,"column":19},"action":"insert","lines":["p"]},{"start":{"row":49,"column":19},"end":{"row":49,"column":20},"action":"insert","lines":["m"]},{"start":{"row":49,"column":20},"end":{"row":49,"column":21},"action":"insert","lines":["e"]},{"start":{"row":49,"column":21},"end":{"row":49,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":49,"column":22},"end":{"row":49,"column":23},"action":"insert","lines":["t"],"id":187}],[{"start":{"row":48,"column":0},"end":{"row":49,"column":3},"action":"remove","lines":["id development:","   "],"id":188}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":1},"action":"remove","lines":[" "],"id":189}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"insert","lines":["i"],"id":190},{"start":{"row":98,"column":1},"end":{"row":98,"column":2},"action":"insert","lines":["f"]}],[{"start":{"row":98,"column":2},"end":{"row":98,"column":3},"action":"insert","lines":[" "],"id":191},{"start":{"row":98,"column":3},"end":{"row":98,"column":4},"action":"insert","lines":["d"]},{"start":{"row":98,"column":4},"end":{"row":98,"column":5},"action":"insert","lines":["e"]},{"start":{"row":98,"column":5},"end":{"row":98,"column":6},"action":"insert","lines":["v"]},{"start":{"row":98,"column":6},"end":{"row":98,"column":7},"action":"insert","lines":["e"]},{"start":{"row":98,"column":7},"end":{"row":98,"column":8},"action":"insert","lines":["l"]},{"start":{"row":98,"column":8},"end":{"row":98,"column":9},"action":"insert","lines":["o"]},{"start":{"row":98,"column":9},"end":{"row":98,"column":10},"action":"insert","lines":["p"]}],[{"start":{"row":98,"column":10},"end":{"row":98,"column":11},"action":"insert","lines":["m"],"id":192},{"start":{"row":98,"column":11},"end":{"row":98,"column":12},"action":"insert","lines":["e"]},{"start":{"row":98,"column":12},"end":{"row":98,"column":13},"action":"insert","lines":["n"]},{"start":{"row":98,"column":13},"end":{"row":98,"column":14},"action":"insert","lines":["t"]},{"start":{"row":98,"column":14},"end":{"row":98,"column":15},"action":"insert","lines":[":"]}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"remove","lines":["#"],"id":193}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":1},"action":"remove","lines":["#"],"id":194},{"start":{"row":101,"column":0},"end":{"row":101,"column":1},"action":"remove","lines":["#"]}],[{"start":{"row":102,"column":0},"end":{"row":102,"column":1},"action":"remove","lines":["#"],"id":195}],[{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"remove","lines":["#"],"id":196}],[{"start":{"row":104,"column":0},"end":{"row":104,"column":1},"action":"remove","lines":["#"],"id":197}],[{"start":{"row":98,"column":15},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":198},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "],"id":199},{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"insert","lines":["    "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"insert","lines":["    "]},{"start":{"row":103,"column":0},"end":{"row":103,"column":4},"action":"insert","lines":["    "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":4},"action":"insert","lines":["    "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":99,"column":1},"end":{"row":99,"column":2},"action":"remove","lines":[" "],"id":200},{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"remove","lines":[" "]},{"start":{"row":98,"column":15},"end":{"row":99,"column":2},"action":"remove","lines":["","  "]}],[{"start":{"row":104,"column":5},"end":{"row":105,"column":0},"action":"insert","lines":["",""],"id":201},{"start":{"row":105,"column":0},"end":{"row":105,"column":4},"action":"insert","lines":["    "]},{"start":{"row":105,"column":4},"end":{"row":105,"column":5},"action":"insert","lines":["e"]},{"start":{"row":105,"column":5},"end":{"row":105,"column":6},"action":"insert","lines":["l"]},{"start":{"row":105,"column":6},"end":{"row":105,"column":7},"action":"insert","lines":["s"]},{"start":{"row":105,"column":7},"end":{"row":105,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":105,"column":8},"end":{"row":105,"column":9},"action":"insert","lines":[":"],"id":202}],[{"start":{"row":105,"column":9},"end":{"row":106,"column":0},"action":"insert","lines":["",""],"id":203},{"start":{"row":106,"column":0},"end":{"row":106,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":105,"column":0},"end":{"row":105,"column":4},"action":"remove","lines":["    "],"id":204}],[{"start":{"row":106,"column":8},"end":{"row":107,"column":0},"action":"remove","lines":["",""],"id":205},{"start":{"row":106,"column":4},"end":{"row":106,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":50,"column":56},"end":{"row":50,"column":125},"action":"insert","lines":["'6de882e1a3214cf4bdbf7bc44a909c1e.vfs.cloud9.us-east-1.amazonaws.com'"],"id":206}],[{"start":{"row":50,"column":125},"end":{"row":50,"column":126},"action":"insert","lines":[","],"id":207}],[{"start":{"row":50,"column":17},"end":{"row":50,"column":55},"action":"remove","lines":["'django-simple-todo-app.herokuapp.com'"],"id":208}],[{"start":{"row":50,"column":17},"end":{"row":50,"column":18},"action":"remove","lines":[","],"id":209}],[{"start":{"row":50,"column":17},"end":{"row":50,"column":31},"action":"insert","lines":["HEROKU_APP_URL"],"id":210}],[{"start":{"row":50,"column":30},"end":{"row":50,"column":31},"action":"remove","lines":["L"],"id":211},{"start":{"row":50,"column":29},"end":{"row":50,"column":30},"action":"remove","lines":["R"]},{"start":{"row":50,"column":28},"end":{"row":50,"column":29},"action":"remove","lines":["U"]},{"start":{"row":50,"column":27},"end":{"row":50,"column":28},"action":"remove","lines":["_"]},{"start":{"row":50,"column":26},"end":{"row":50,"column":27},"action":"remove","lines":["P"]},{"start":{"row":50,"column":25},"end":{"row":50,"column":26},"action":"remove","lines":["P"]},{"start":{"row":50,"column":24},"end":{"row":50,"column":25},"action":"remove","lines":["A"]},{"start":{"row":50,"column":23},"end":{"row":50,"column":24},"action":"remove","lines":["_"]},{"start":{"row":50,"column":22},"end":{"row":50,"column":23},"action":"remove","lines":["U"]},{"start":{"row":50,"column":21},"end":{"row":50,"column":22},"action":"remove","lines":["K"]},{"start":{"row":50,"column":20},"end":{"row":50,"column":21},"action":"remove","lines":["O"]},{"start":{"row":50,"column":19},"end":{"row":50,"column":20},"action":"remove","lines":["R"]},{"start":{"row":50,"column":18},"end":{"row":50,"column":19},"action":"remove","lines":["E"]}],[{"start":{"row":50,"column":17},"end":{"row":50,"column":18},"action":"remove","lines":["H"],"id":212}],[{"start":{"row":50,"column":17},"end":{"row":50,"column":43},"action":"insert","lines":["os.environ.get('HOSTNAME')"],"id":213}],[{"start":{"row":50,"column":43},"end":{"row":50,"column":44},"action":"insert","lines":[" "],"id":214}],[{"start":{"row":50,"column":43},"end":{"row":50,"column":44},"action":"remove","lines":[" "],"id":215}],[{"start":{"row":50,"column":43},"end":{"row":50,"column":44},"action":"insert","lines":[","],"id":216}],[{"start":{"row":50,"column":40},"end":{"row":50,"column":41},"action":"remove","lines":["E"],"id":217},{"start":{"row":50,"column":39},"end":{"row":50,"column":40},"action":"remove","lines":["M"]},{"start":{"row":50,"column":38},"end":{"row":50,"column":39},"action":"remove","lines":["A"]},{"start":{"row":50,"column":37},"end":{"row":50,"column":38},"action":"remove","lines":["N"]},{"start":{"row":50,"column":36},"end":{"row":50,"column":37},"action":"remove","lines":["T"]},{"start":{"row":50,"column":35},"end":{"row":50,"column":36},"action":"remove","lines":["S"]},{"start":{"row":50,"column":34},"end":{"row":50,"column":35},"action":"remove","lines":["O"]},{"start":{"row":50,"column":33},"end":{"row":50,"column":34},"action":"remove","lines":["H"]}],[{"start":{"row":50,"column":33},"end":{"row":50,"column":47},"action":"insert","lines":["HEROKU_APP_URL"],"id":218}],[{"start":{"row":50,"column":17},"end":{"row":50,"column":49},"action":"remove","lines":["os.environ.get('HEROKU_APP_URL')"],"id":219},{"start":{"row":50,"column":17},"end":{"row":50,"column":39},"action":"insert","lines":["git push origin master"]}],[{"start":{"row":50,"column":38},"end":{"row":50,"column":39},"action":"remove","lines":["r"],"id":220},{"start":{"row":50,"column":37},"end":{"row":50,"column":38},"action":"remove","lines":["e"]},{"start":{"row":50,"column":36},"end":{"row":50,"column":37},"action":"remove","lines":["t"]},{"start":{"row":50,"column":35},"end":{"row":50,"column":36},"action":"remove","lines":["s"]},{"start":{"row":50,"column":34},"end":{"row":50,"column":35},"action":"remove","lines":["a"]},{"start":{"row":50,"column":33},"end":{"row":50,"column":34},"action":"remove","lines":["m"]},{"start":{"row":50,"column":32},"end":{"row":50,"column":33},"action":"remove","lines":[" "]},{"start":{"row":50,"column":31},"end":{"row":50,"column":32},"action":"remove","lines":["n"]},{"start":{"row":50,"column":30},"end":{"row":50,"column":31},"action":"remove","lines":["i"]},{"start":{"row":50,"column":29},"end":{"row":50,"column":30},"action":"remove","lines":["g"]},{"start":{"row":50,"column":28},"end":{"row":50,"column":29},"action":"remove","lines":["i"]},{"start":{"row":50,"column":27},"end":{"row":50,"column":28},"action":"remove","lines":["r"]},{"start":{"row":50,"column":26},"end":{"row":50,"column":27},"action":"remove","lines":["o"]},{"start":{"row":50,"column":25},"end":{"row":50,"column":26},"action":"remove","lines":[" "]},{"start":{"row":50,"column":24},"end":{"row":50,"column":25},"action":"remove","lines":["h"]},{"start":{"row":50,"column":23},"end":{"row":50,"column":24},"action":"remove","lines":["s"]},{"start":{"row":50,"column":22},"end":{"row":50,"column":23},"action":"remove","lines":["u"]},{"start":{"row":50,"column":21},"end":{"row":50,"column":22},"action":"remove","lines":["p"]},{"start":{"row":50,"column":20},"end":{"row":50,"column":21},"action":"remove","lines":[" "]},{"start":{"row":50,"column":19},"end":{"row":50,"column":20},"action":"remove","lines":["t"]},{"start":{"row":50,"column":18},"end":{"row":50,"column":19},"action":"remove","lines":["i"]},{"start":{"row":50,"column":17},"end":{"row":50,"column":18},"action":"remove","lines":["g"]}],[{"start":{"row":50,"column":17},"end":{"row":50,"column":55},"action":"insert","lines":["'django-simple-todo-app.herokuapp.com'"],"id":221}],[{"start":{"row":44,"column":13},"end":{"row":44,"column":65},"action":"remove","lines":["'+#)rng-+q-&4s((9y8qm#7)63lyhgq%yl-!8fzv83(_zg%#_rr'"],"id":222}],[{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["S"],"id":223},{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":["E"]},{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":["C"]},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["R"]},{"start":{"row":44,"column":17},"end":{"row":44,"column":18},"action":"insert","lines":["E"]}],[{"start":{"row":44,"column":13},"end":{"row":44,"column":18},"action":"remove","lines":["SECRE"],"id":224},{"start":{"row":44,"column":13},"end":{"row":44,"column":23},"action":"insert","lines":["SECRET_KEY"]}],[{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"remove","lines":[" "],"id":225}],[{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"remove","lines":[" "],"id":226}],[{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"remove","lines":["="],"id":227}],[{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":[" "],"id":228},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["="]}],[{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":[" "],"id":229},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["o"]}],[{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":["s"],"id":230},{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":["."]}],[{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["e"],"id":231}],[{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"remove","lines":["e"],"id":232},{"start":{"row":44,"column":16},"end":{"row":44,"column":23},"action":"insert","lines":["environ"]}],[{"start":{"row":44,"column":23},"end":{"row":44,"column":24},"action":"insert","lines":["."],"id":233}],[{"start":{"row":44,"column":24},"end":{"row":44,"column":29},"action":"insert","lines":["get()"],"id":234}],[{"start":{"row":44,"column":28},"end":{"row":44,"column":29},"action":"remove","lines":[")"],"id":235}],[{"start":{"row":44,"column":28},"end":{"row":44,"column":29},"action":"insert","lines":["'"],"id":236}],[{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"insert","lines":["'"],"id":237},{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"insert","lines":[")"]}]]},"ace":{"folds":[],"scrolltop":480,"scrollleft":0,"selection":{"start":{"row":44,"column":41},"end":{"row":44,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":44,"state":"start","mode":"ace/mode/python"}},"timestamp":1565206582790}
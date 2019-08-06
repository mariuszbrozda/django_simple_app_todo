{"changed":true,"filter":false,"title":"settings.py","tooltip":"/django_todo/settings.py","value":"\"\"\"\nDjango settings for django_todo project.\n\nGenerated by 'django-admin startproject' using Django 1.11.\n\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.11/topics/settings/\n\nFor the full list of settings and their values, see\nhttps://docs.djangoproject.com/en/1.11/ref/settings/\n\"\"\"\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\nimport os\nimport dj_database_url\n\n\nif os.environ.get('DEVELOPMENT'):\n    development = True\nelse:\n    development = False\n\n    \n    \n# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\nBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.9/howto/static-files/\nSTATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')\n\n\n# Extra places for collectstatic to find static files.\nSTATICFILES_DIRS = (\n    os.path.join(BASE_DIR, 'static'),\n)\n\n\n# Quick-start development settings - unsuitable for production\n# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/\n\n# SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = '+#)rng-+q-&4s((9y8qm#7)63lyhgq%yl-!8fzv83(_zg%#_rr'\n\n# SECURITY WARNING: don't run with debug turned on in production!\n\nDEBUG = development\n\nALLOWED_HOSTS = ['6de882e1a3214cf4bdbf7bc44a909c1e.vfs.cloud9.us-east-1.amazonaws.com', os.environ.get('HOSTNAME')]\n\n\n# Application definition\n\nINSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    'todo'\n]\n\nMIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',\n    'django.contrib.sessions.middleware.SessionMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    'django.middleware.csrf.CsrfViewMiddleware',\n    'django.contrib.auth.middleware.AuthenticationMiddleware',\n    'django.contrib.messages.middleware.MessageMiddleware',\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n]\n\nROOT_URLCONF = 'django_todo.urls'\n\nTEMPLATES = [\n    {\n        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n        'DIRS': [],\n        'APP_DIRS': True,\n        'OPTIONS': {\n            'context_processors': [\n                'django.template.context_processors.debug',\n                'django.template.context_processors.request',\n                'django.contrib.auth.context_processors.auth',\n                'django.contrib.messages.context_processors.messages',\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = 'django_todo.wsgi.application'\n\n\n# Database\n# https://docs.djangoproject.com/en/1.11/ref/settings/#databases\nif development:\n    DATABASES = {\n       'default': {\n           'ENGINE': 'django.db.backends.sqlite3',\n            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n      }\n    }\nelse:\n    DATABASES = {'default': dj_database_url.parse(os.environ.get(\"DATABASE_URL\"))}\n\n\n# Password validation\n# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n    },\n]\n\n\n# Internationalization\n# https://docs.djangoproject.com/en/1.11/topics/i18n/\n\nLANGUAGE_CODE = 'en-us'\n\nTIME_ZONE = 'UTC'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\nSTATIC_URL = '/static/'\n","undoManager":{"mark":98,"position":100,"stack":[[{"start":{"row":96,"column":46},"end":{"row":96,"column":209},"action":"remove","lines":["\"postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562\""],"id":109}],[{"start":{"row":96,"column":46},"end":{"row":96,"column":72},"action":"insert","lines":["os.environ.get('HOSTNAME')"],"id":110}],[{"start":{"row":96,"column":69},"end":{"row":96,"column":70},"action":"remove","lines":["E"],"id":111},{"start":{"row":96,"column":68},"end":{"row":96,"column":69},"action":"remove","lines":["M"]},{"start":{"row":96,"column":67},"end":{"row":96,"column":68},"action":"remove","lines":["A"]},{"start":{"row":96,"column":66},"end":{"row":96,"column":67},"action":"remove","lines":["N"]},{"start":{"row":96,"column":65},"end":{"row":96,"column":66},"action":"remove","lines":["T"]},{"start":{"row":96,"column":64},"end":{"row":96,"column":65},"action":"remove","lines":["S"]},{"start":{"row":96,"column":63},"end":{"row":96,"column":64},"action":"remove","lines":["O"]},{"start":{"row":96,"column":62},"end":{"row":96,"column":63},"action":"remove","lines":["H"]}],[{"start":{"row":96,"column":62},"end":{"row":96,"column":63},"action":"insert","lines":["D"],"id":112},{"start":{"row":96,"column":63},"end":{"row":96,"column":64},"action":"insert","lines":["A"]},{"start":{"row":96,"column":64},"end":{"row":96,"column":65},"action":"insert","lines":["T"]},{"start":{"row":96,"column":65},"end":{"row":96,"column":66},"action":"insert","lines":["A"]},{"start":{"row":96,"column":66},"end":{"row":96,"column":67},"action":"insert","lines":["B"]},{"start":{"row":96,"column":67},"end":{"row":96,"column":68},"action":"insert","lines":["A"]},{"start":{"row":96,"column":68},"end":{"row":96,"column":69},"action":"insert","lines":["S"]},{"start":{"row":96,"column":69},"end":{"row":96,"column":70},"action":"insert","lines":["E"]}],[{"start":{"row":96,"column":70},"end":{"row":96,"column":71},"action":"insert","lines":["_"],"id":113},{"start":{"row":96,"column":71},"end":{"row":96,"column":72},"action":"insert","lines":["U"]},{"start":{"row":96,"column":72},"end":{"row":96,"column":73},"action":"insert","lines":["R"]},{"start":{"row":96,"column":73},"end":{"row":96,"column":74},"action":"insert","lines":["L"]}],[{"start":{"row":96,"column":46},"end":{"row":96,"column":48},"action":"insert","lines":["\"p"],"id":114},{"start":{"row":96,"column":50},"end":{"row":96,"column":156},"action":"insert","lines":["tgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214"]},{"start":{"row":96,"column":158},"end":{"row":96,"column":162},"action":"remove","lines":["nvir"]},{"start":{"row":96,"column":158},"end":{"row":96,"column":179},"action":"insert","lines":["u-west-1.compute.amaz"]},{"start":{"row":96,"column":181},"end":{"row":96,"column":184},"action":"insert","lines":["aws"]},{"start":{"row":96,"column":185},"end":{"row":96,"column":204},"action":"remove","lines":["get('DATABASE_URL')"]},{"start":{"row":96,"column":185},"end":{"row":96,"column":209},"action":"insert","lines":["com:5432/daj1rlf3h5q562\""]}],[{"start":{"row":96,"column":46},"end":{"row":96,"column":209},"action":"remove","lines":["\"postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562\""],"id":115}],[{"start":{"row":96,"column":46},"end":{"row":96,"column":47},"action":"insert","lines":["o"],"id":116},{"start":{"row":96,"column":47},"end":{"row":96,"column":48},"action":"insert","lines":["s"]},{"start":{"row":96,"column":48},"end":{"row":96,"column":49},"action":"insert","lines":["."]},{"start":{"row":96,"column":49},"end":{"row":96,"column":50},"action":"insert","lines":["e"]},{"start":{"row":96,"column":50},"end":{"row":96,"column":51},"action":"insert","lines":["n"]}],[{"start":{"row":96,"column":49},"end":{"row":96,"column":51},"action":"remove","lines":["en"],"id":117},{"start":{"row":96,"column":49},"end":{"row":96,"column":56},"action":"insert","lines":["environ"]}],[{"start":{"row":96,"column":56},"end":{"row":96,"column":58},"action":"insert","lines":["()"],"id":118}],[{"start":{"row":96,"column":57},"end":{"row":96,"column":59},"action":"insert","lines":["\"\""],"id":119}],[{"start":{"row":96,"column":58},"end":{"row":96,"column":59},"action":"insert","lines":["C"],"id":120},{"start":{"row":96,"column":59},"end":{"row":96,"column":60},"action":"insert","lines":["9"]},{"start":{"row":96,"column":60},"end":{"row":96,"column":61},"action":"insert","lines":["_"]}],[{"start":{"row":96,"column":61},"end":{"row":96,"column":62},"action":"insert","lines":["O"],"id":121}],[{"start":{"row":96,"column":61},"end":{"row":96,"column":62},"action":"remove","lines":["O"],"id":122}],[{"start":{"row":96,"column":58},"end":{"row":96,"column":61},"action":"remove","lines":["C9_"],"id":123},{"start":{"row":96,"column":58},"end":{"row":96,"column":69},"action":"insert","lines":["C9_HOSTNAME"]}],[{"start":{"row":96,"column":71},"end":{"row":96,"column":72},"action":"insert","lines":[","],"id":124}],[{"start":{"row":96,"column":72},"end":{"row":96,"column":73},"action":"insert","lines":[" "],"id":125}],[{"start":{"row":96,"column":73},"end":{"row":96,"column":74},"action":"insert","lines":["o"],"id":126},{"start":{"row":96,"column":74},"end":{"row":96,"column":75},"action":"insert","lines":["s"]},{"start":{"row":96,"column":75},"end":{"row":96,"column":76},"action":"insert","lines":["."]},{"start":{"row":96,"column":76},"end":{"row":96,"column":77},"action":"insert","lines":["e"]}],[{"start":{"row":96,"column":76},"end":{"row":96,"column":77},"action":"remove","lines":["e"],"id":127},{"start":{"row":96,"column":76},"end":{"row":96,"column":83},"action":"insert","lines":["environ"]}],[{"start":{"row":96,"column":83},"end":{"row":96,"column":85},"action":"insert","lines":["()"],"id":128}],[{"start":{"row":96,"column":84},"end":{"row":96,"column":86},"action":"insert","lines":["\"\""],"id":129}],[{"start":{"row":96,"column":85},"end":{"row":96,"column":93},"action":"insert","lines":["HOSTNAME"],"id":130}],[{"start":{"row":96,"column":71},"end":{"row":96,"column":95},"action":"remove","lines":[", os.environ(\"HOSTNAME\")"],"id":131}],[{"start":{"row":96,"column":68},"end":{"row":96,"column":69},"action":"remove","lines":["E"],"id":132},{"start":{"row":96,"column":67},"end":{"row":96,"column":68},"action":"remove","lines":["M"]},{"start":{"row":96,"column":66},"end":{"row":96,"column":67},"action":"remove","lines":["A"]},{"start":{"row":96,"column":65},"end":{"row":96,"column":66},"action":"remove","lines":["N"]},{"start":{"row":96,"column":64},"end":{"row":96,"column":65},"action":"remove","lines":["T"]},{"start":{"row":96,"column":63},"end":{"row":96,"column":64},"action":"remove","lines":["S"]},{"start":{"row":96,"column":62},"end":{"row":96,"column":63},"action":"remove","lines":["O"]},{"start":{"row":96,"column":61},"end":{"row":96,"column":62},"action":"remove","lines":["H"]},{"start":{"row":96,"column":60},"end":{"row":96,"column":61},"action":"remove","lines":["_"]},{"start":{"row":96,"column":59},"end":{"row":96,"column":60},"action":"remove","lines":["9"]},{"start":{"row":96,"column":58},"end":{"row":96,"column":59},"action":"remove","lines":["C"]}],[{"start":{"row":96,"column":58},"end":{"row":96,"column":59},"action":"insert","lines":["D"],"id":133},{"start":{"row":96,"column":59},"end":{"row":96,"column":60},"action":"insert","lines":["A"]},{"start":{"row":96,"column":60},"end":{"row":96,"column":61},"action":"insert","lines":["T"]},{"start":{"row":96,"column":61},"end":{"row":96,"column":62},"action":"insert","lines":["A"]},{"start":{"row":96,"column":62},"end":{"row":96,"column":63},"action":"insert","lines":["B"]},{"start":{"row":96,"column":63},"end":{"row":96,"column":64},"action":"insert","lines":["A"]},{"start":{"row":96,"column":64},"end":{"row":96,"column":65},"action":"insert","lines":["S"]},{"start":{"row":96,"column":65},"end":{"row":96,"column":66},"action":"insert","lines":["E"]}],[{"start":{"row":96,"column":66},"end":{"row":96,"column":67},"action":"insert","lines":["_"],"id":134},{"start":{"row":96,"column":67},"end":{"row":96,"column":68},"action":"insert","lines":["U"]},{"start":{"row":96,"column":68},"end":{"row":96,"column":69},"action":"insert","lines":["R"]},{"start":{"row":96,"column":69},"end":{"row":96,"column":70},"action":"insert","lines":["L"]}],[{"start":{"row":96,"column":56},"end":{"row":96,"column":57},"action":"insert","lines":["."],"id":135}],[{"start":{"row":96,"column":57},"end":{"row":96,"column":60},"action":"insert","lines":["get"],"id":136}],[{"start":{"row":41,"column":17},"end":{"row":41,"column":46},"action":"remove","lines":["os.environ.get('C9_HOSTNAME')"],"id":137},{"start":{"row":41,"column":17},"end":{"row":41,"column":55},"action":"insert","lines":["'django-simple-todo-app.herokuapp.com'"]}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"insert","lines":["h"],"id":138}],[{"start":{"row":41,"column":85},"end":{"row":41,"column":86},"action":"insert","lines":["h"],"id":139}],[{"start":{"row":41,"column":85},"end":{"row":41,"column":86},"action":"remove","lines":["h"],"id":140}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"remove","lines":["h"],"id":141}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":142},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["",""],"id":143}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["i"],"id":144},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["f"]}],[{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":[" "],"id":145},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":["o"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["s"]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["."]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["n"],"id":146}],[{"start":{"row":18,"column":6},"end":{"row":18,"column":8},"action":"remove","lines":["en"],"id":147},{"start":{"row":18,"column":6},"end":{"row":18,"column":13},"action":"insert","lines":["environ"]}],[{"start":{"row":18,"column":13},"end":{"row":18,"column":15},"action":"insert","lines":["()"],"id":148}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["0"],"id":149}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["D"],"id":150},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["E"]},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["V"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["E"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["L"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["O"]}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["P"],"id":151},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":["M"]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["E"]},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["N"]}],[{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":["T"],"id":152}],[{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"remove","lines":["0"],"id":153}],[{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"insert","lines":["'"],"id":154}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["'"],"id":155}],[{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["."],"id":156}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":17},"action":"insert","lines":["get"],"id":157}],[{"start":{"row":18,"column":32},"end":{"row":18,"column":33},"action":"insert","lines":[":"],"id":158}],[{"start":{"row":18,"column":33},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":159},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":20,"column":0},"action":"insert","lines":["",""]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":21,"column":0},"action":"insert","lines":["",""]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["d"],"id":160},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["e"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["v"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["e"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["l"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["o"]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["p"]}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["m"],"id":161},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["e"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["n"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":[" "],"id":162},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":[" "],"id":163},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["T"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["r"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["u"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":22},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":164},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":165}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"insert","lines":["e"],"id":166},{"start":{"row":20,"column":1},"end":{"row":20,"column":2},"action":"insert","lines":["l"]},{"start":{"row":20,"column":2},"end":{"row":20,"column":3},"action":"insert","lines":["s"]},{"start":{"row":20,"column":3},"end":{"row":20,"column":4},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":4},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":167}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":[":"],"id":168}],[{"start":{"row":20,"column":5},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":169},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["d"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["v"],"id":170},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["e"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["l"]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["o"]},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["p"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["m"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["e"]},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["n"]},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":[" "],"id":171},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":[" "],"id":172},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["F"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["a"]}],[{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["l"],"id":173},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["s"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":46,"column":65},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":174},{"start":{"row":47,"column":0},"end":{"row":48,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":1},"action":"insert","lines":["i"],"id":175},{"start":{"row":48,"column":1},"end":{"row":48,"column":2},"action":"insert","lines":["d"]}],[{"start":{"row":48,"column":2},"end":{"row":48,"column":3},"action":"insert","lines":[" "],"id":176},{"start":{"row":48,"column":3},"end":{"row":48,"column":4},"action":"insert","lines":["d"]},{"start":{"row":48,"column":4},"end":{"row":48,"column":5},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":3},"end":{"row":48,"column":5},"action":"remove","lines":["de"],"id":177},{"start":{"row":48,"column":3},"end":{"row":48,"column":14},"action":"insert","lines":["development"]}],[{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"insert","lines":[" "],"id":178},{"start":{"row":48,"column":15},"end":{"row":48,"column":16},"action":"insert","lines":["i"]},{"start":{"row":48,"column":16},"end":{"row":48,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"insert","lines":[" "],"id":179},{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"insert","lines":["T"]},{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"insert","lines":["r"]},{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"insert","lines":["u"]},{"start":{"row":48,"column":21},"end":{"row":48,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":22},"end":{"row":48,"column":23},"action":"insert","lines":[":"],"id":180}],[{"start":{"row":48,"column":22},"end":{"row":48,"column":23},"action":"remove","lines":[":"],"id":181},{"start":{"row":48,"column":21},"end":{"row":48,"column":22},"action":"remove","lines":["e"]},{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"remove","lines":["u"]},{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"remove","lines":["r"]},{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"remove","lines":["T"]},{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"remove","lines":[" "]},{"start":{"row":48,"column":16},"end":{"row":48,"column":17},"action":"remove","lines":["s"]},{"start":{"row":48,"column":15},"end":{"row":48,"column":16},"action":"remove","lines":["i"]},{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"remove","lines":[" "]}],[{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"insert","lines":[":"],"id":182}],[{"start":{"row":48,"column":15},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":183},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":49,"column":4},"end":{"row":50,"column":0},"action":"remove","lines":["",""],"id":184}],[{"start":{"row":49,"column":15},"end":{"row":49,"column":16},"action":"remove","lines":["e"],"id":185},{"start":{"row":49,"column":14},"end":{"row":49,"column":15},"action":"remove","lines":["u"]},{"start":{"row":49,"column":13},"end":{"row":49,"column":14},"action":"remove","lines":["r"]},{"start":{"row":49,"column":12},"end":{"row":49,"column":13},"action":"remove","lines":["T"]}],[{"start":{"row":49,"column":12},"end":{"row":49,"column":13},"action":"insert","lines":["d"],"id":186},{"start":{"row":49,"column":13},"end":{"row":49,"column":14},"action":"insert","lines":["e"]},{"start":{"row":49,"column":14},"end":{"row":49,"column":15},"action":"insert","lines":["v"]},{"start":{"row":49,"column":15},"end":{"row":49,"column":16},"action":"insert","lines":["e"]},{"start":{"row":49,"column":16},"end":{"row":49,"column":17},"action":"insert","lines":["l"]},{"start":{"row":49,"column":17},"end":{"row":49,"column":18},"action":"insert","lines":["o"]},{"start":{"row":49,"column":18},"end":{"row":49,"column":19},"action":"insert","lines":["p"]},{"start":{"row":49,"column":19},"end":{"row":49,"column":20},"action":"insert","lines":["m"]},{"start":{"row":49,"column":20},"end":{"row":49,"column":21},"action":"insert","lines":["e"]},{"start":{"row":49,"column":21},"end":{"row":49,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":49,"column":22},"end":{"row":49,"column":23},"action":"insert","lines":["t"],"id":187}],[{"start":{"row":48,"column":0},"end":{"row":49,"column":3},"action":"remove","lines":["id development:","   "],"id":188}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":1},"action":"remove","lines":[" "],"id":189}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"insert","lines":["i"],"id":190},{"start":{"row":98,"column":1},"end":{"row":98,"column":2},"action":"insert","lines":["f"]}],[{"start":{"row":98,"column":2},"end":{"row":98,"column":3},"action":"insert","lines":[" "],"id":191},{"start":{"row":98,"column":3},"end":{"row":98,"column":4},"action":"insert","lines":["d"]},{"start":{"row":98,"column":4},"end":{"row":98,"column":5},"action":"insert","lines":["e"]},{"start":{"row":98,"column":5},"end":{"row":98,"column":6},"action":"insert","lines":["v"]},{"start":{"row":98,"column":6},"end":{"row":98,"column":7},"action":"insert","lines":["e"]},{"start":{"row":98,"column":7},"end":{"row":98,"column":8},"action":"insert","lines":["l"]},{"start":{"row":98,"column":8},"end":{"row":98,"column":9},"action":"insert","lines":["o"]},{"start":{"row":98,"column":9},"end":{"row":98,"column":10},"action":"insert","lines":["p"]}],[{"start":{"row":98,"column":10},"end":{"row":98,"column":11},"action":"insert","lines":["m"],"id":192},{"start":{"row":98,"column":11},"end":{"row":98,"column":12},"action":"insert","lines":["e"]},{"start":{"row":98,"column":12},"end":{"row":98,"column":13},"action":"insert","lines":["n"]},{"start":{"row":98,"column":13},"end":{"row":98,"column":14},"action":"insert","lines":["t"]},{"start":{"row":98,"column":14},"end":{"row":98,"column":15},"action":"insert","lines":[":"]}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"remove","lines":["#"],"id":193}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":1},"action":"remove","lines":["#"],"id":194},{"start":{"row":101,"column":0},"end":{"row":101,"column":1},"action":"remove","lines":["#"]}],[{"start":{"row":102,"column":0},"end":{"row":102,"column":1},"action":"remove","lines":["#"],"id":195}],[{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"remove","lines":["#"],"id":196}],[{"start":{"row":104,"column":0},"end":{"row":104,"column":1},"action":"remove","lines":["#"],"id":197}],[{"start":{"row":98,"column":15},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":198},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "],"id":199},{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"insert","lines":["    "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"insert","lines":["    "]},{"start":{"row":103,"column":0},"end":{"row":103,"column":4},"action":"insert","lines":["    "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":4},"action":"insert","lines":["    "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":99,"column":1},"end":{"row":99,"column":2},"action":"remove","lines":[" "],"id":200},{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"remove","lines":[" "]},{"start":{"row":98,"column":15},"end":{"row":99,"column":2},"action":"remove","lines":["","  "]}],[{"start":{"row":104,"column":5},"end":{"row":105,"column":0},"action":"insert","lines":["",""],"id":201},{"start":{"row":105,"column":0},"end":{"row":105,"column":4},"action":"insert","lines":["    "]},{"start":{"row":105,"column":4},"end":{"row":105,"column":5},"action":"insert","lines":["e"]},{"start":{"row":105,"column":5},"end":{"row":105,"column":6},"action":"insert","lines":["l"]},{"start":{"row":105,"column":6},"end":{"row":105,"column":7},"action":"insert","lines":["s"]},{"start":{"row":105,"column":7},"end":{"row":105,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":105,"column":8},"end":{"row":105,"column":9},"action":"insert","lines":[":"],"id":202}],[{"start":{"row":105,"column":9},"end":{"row":106,"column":0},"action":"insert","lines":["",""],"id":203},{"start":{"row":106,"column":0},"end":{"row":106,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":105,"column":0},"end":{"row":105,"column":4},"action":"remove","lines":["    "],"id":204}],[{"start":{"row":106,"column":8},"end":{"row":107,"column":0},"action":"remove","lines":["",""],"id":205},{"start":{"row":106,"column":4},"end":{"row":106,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":50,"column":56},"end":{"row":50,"column":125},"action":"insert","lines":["'6de882e1a3214cf4bdbf7bc44a909c1e.vfs.cloud9.us-east-1.amazonaws.com'"],"id":206}],[{"start":{"row":50,"column":125},"end":{"row":50,"column":126},"action":"insert","lines":[","],"id":207}],[{"start":{"row":50,"column":17},"end":{"row":50,"column":55},"action":"remove","lines":["'django-simple-todo-app.herokuapp.com'"],"id":208}],[{"start":{"row":50,"column":17},"end":{"row":50,"column":18},"action":"remove","lines":[","],"id":209}]]},"ace":{"folds":[],"scrolltop":651,"scrollleft":0,"selection":{"start":{"row":50,"column":17},"end":{"row":50,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":37,"state":"start","mode":"ace/mode/python"}},"timestamp":1565125983111}
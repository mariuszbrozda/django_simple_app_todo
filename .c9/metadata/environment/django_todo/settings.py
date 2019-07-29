{"changed":true,"filter":false,"title":"settings.py","tooltip":"/django_todo/settings.py","value":"\"\"\"\nDjango settings for django_todo project.\n\nGenerated by 'django-admin startproject' using Django 1.11.\n\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.11/topics/settings/\n\nFor the full list of settings and their values, see\nhttps://docs.djangoproject.com/en/1.11/ref/settings/\n\"\"\"\n\nimport os\nimport dj_database_url\n\n# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\nBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.9/howto/static-files/\nSTATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')\n\n\n# Extra places for collectstatic to find static files.\nSTATICFILES_DIRS = (\n    os.path.join(BASE_DIR, 'static'),\n)\n\n\n# Quick-start development settings - unsuitable for production\n# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/\n\n# SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = '+#)rng-+q-&4s((9y8qm#7)63lyhgq%yl-!8fzv83(_zg%#_rr'\n\n# SECURITY WARNING: don't run with debug turned on in production!\nDEBUG = True\n\nALLOWED_HOSTS = ['6de882e1a3214cf4bdbf7bc44a909c1e.vfs.cloud9.us-east-1.amazonaws.com']\n\n\n# Application definition\n\nINSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    'todo'\n]\n\nMIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',\n    'django.contrib.sessions.middleware.SessionMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    'django.middleware.csrf.CsrfViewMiddleware',\n    'django.contrib.auth.middleware.AuthenticationMiddleware',\n    'django.contrib.messages.middleware.MessageMiddleware',\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n]\n\nROOT_URLCONF = 'django_todo.urls'\n\nTEMPLATES = [\n    {\n        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n        'DIRS': [],\n        'APP_DIRS': True,\n        'OPTIONS': {\n            'context_processors': [\n                'django.template.context_processors.debug',\n                'django.template.context_processors.request',\n                'django.contrib.auth.context_processors.auth',\n                'django.contrib.messages.context_processors.messages',\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = 'django_todo.wsgi.application'\n\n\n# Database\n# https://docs.djangoproject.com/en/1.11/ref/settings/#databases\n\n#DATABASES = {\n#   'default': {\n#       'ENGINE': 'django.db.backends.sqlite3',\n#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n#  }\n#}\nDATABASES = {'default': dj_database_url.parse(\"postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562\")}\n\n\n# Password validation\n# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n    },\n]\n\n\n# Internationalization\n# https://docs.djangoproject.com/en/1.11/topics/i18n/\n\nLANGUAGE_CODE = 'en-us'\n\nTIME_ZONE = 'UTC'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\nSTATIC_URL = '/static/'\n","undoManager":{"mark":33,"position":34,"stack":[[{"start":{"row":38,"column":33},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":6},"action":"insert","lines":["''"],"id":12}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["t"],"id":13},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["o"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["d"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["o"]}],[{"start":{"row":76,"column":0},"end":{"row":76,"column":1},"action":"insert","lines":["#"],"id":15}],[{"start":{"row":77,"column":1},"end":{"row":77,"column":2},"action":"insert","lines":["#"],"id":16}],[{"start":{"row":78,"column":1},"end":{"row":78,"column":2},"action":"insert","lines":["#"],"id":17}],[{"start":{"row":79,"column":0},"end":{"row":79,"column":1},"action":"insert","lines":["#"],"id":18}],[{"start":{"row":80,"column":2},"end":{"row":80,"column":3},"action":"insert","lines":["#"],"id":19}],[{"start":{"row":81,"column":0},"end":{"row":81,"column":1},"action":"insert","lines":["#"],"id":20}],[{"start":{"row":77,"column":0},"end":{"row":77,"column":1},"action":"remove","lines":[" "],"id":21}],[{"start":{"row":78,"column":0},"end":{"row":78,"column":1},"action":"remove","lines":[" "],"id":22}],[{"start":{"row":80,"column":1},"end":{"row":80,"column":2},"action":"remove","lines":[" "],"id":23},{"start":{"row":80,"column":0},"end":{"row":80,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":81,"column":2},"end":{"row":82,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":82,"column":0},"end":{"row":83,"column":0},"action":"insert","lines":["",""]},{"start":{"row":83,"column":0},"end":{"row":83,"column":1},"action":"insert","lines":["D"]},{"start":{"row":83,"column":1},"end":{"row":83,"column":2},"action":"insert","lines":["A"]},{"start":{"row":83,"column":2},"end":{"row":83,"column":3},"action":"insert","lines":["T"]},{"start":{"row":83,"column":3},"end":{"row":83,"column":4},"action":"insert","lines":["A"]}],[{"start":{"row":83,"column":4},"end":{"row":83,"column":5},"action":"insert","lines":["B"],"id":25},{"start":{"row":83,"column":5},"end":{"row":83,"column":6},"action":"insert","lines":["A"]},{"start":{"row":83,"column":6},"end":{"row":83,"column":7},"action":"insert","lines":["S"]},{"start":{"row":83,"column":7},"end":{"row":83,"column":8},"action":"insert","lines":["E"]},{"start":{"row":83,"column":8},"end":{"row":83,"column":9},"action":"insert","lines":["S"]}],[{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"insert","lines":[" "],"id":26}],[{"start":{"row":83,"column":10},"end":{"row":84,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":84,"column":0},"end":{"row":84,"column":160},"action":"insert","lines":["postgres://ptolycsujunxhe:15c05ecda410b11dfd943c9e92ac9f06afa88cdc4de21b3bfbc7b8298cc9b7c5@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d47n3fm8rtvugs"],"id":28}],[{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"remove","lines":[" "],"id":29},{"start":{"row":83,"column":8},"end":{"row":83,"column":9},"action":"remove","lines":["S"]},{"start":{"row":83,"column":7},"end":{"row":83,"column":8},"action":"remove","lines":["E"]},{"start":{"row":83,"column":6},"end":{"row":83,"column":7},"action":"remove","lines":["S"]},{"start":{"row":83,"column":5},"end":{"row":83,"column":6},"action":"remove","lines":["A"]},{"start":{"row":83,"column":4},"end":{"row":83,"column":5},"action":"remove","lines":["B"]},{"start":{"row":83,"column":3},"end":{"row":83,"column":4},"action":"remove","lines":["A"]},{"start":{"row":83,"column":2},"end":{"row":83,"column":3},"action":"remove","lines":["T"]},{"start":{"row":83,"column":1},"end":{"row":83,"column":2},"action":"remove","lines":["A"]},{"start":{"row":83,"column":0},"end":{"row":83,"column":1},"action":"remove","lines":["D"]}],[{"start":{"row":83,"column":0},"end":{"row":83,"column":73},"action":"insert","lines":["DATABASES = {'default': dj_database_url.parse(\" database url from cars\")}"],"id":30}],[{"start":{"row":83,"column":48},"end":{"row":83,"column":70},"action":"remove","lines":["database url from cars"],"id":31}],[{"start":{"row":83,"column":47},"end":{"row":84,"column":0},"action":"insert","lines":["postgres://ptolycsujunxhe:15c05ecda410b11dfd943c9e92ac9f06afa88cdc4de21b3bfbc7b8298cc9b7c5@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d47n3fm8rtvugs",""],"id":32}],[{"start":{"row":85,"column":0},"end":{"row":86,"column":0},"action":"remove","lines":["postgres://ptolycsujunxhe:15c05ecda410b11dfd943c9e92ac9f06afa88cdc4de21b3bfbc7b8298cc9b7c5@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d47n3fm8rtvugs",""],"id":33}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["i"]},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["m"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"]},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["o"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["r"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":[" "],"id":35}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":22},"action":"insert","lines":["dj_database_url"],"id":36}],[{"start":{"row":84,"column":47},"end":{"row":85,"column":1},"action":"remove","lines":["postgres://ptolycsujunxhe:15c05ecda410b11dfd943c9e92ac9f06afa88cdc4de21b3bfbc7b8298cc9b7c5@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d47n3fm8rtvugs"," "],"id":37}],[{"start":{"row":84,"column":47},"end":{"row":84,"column":207},"action":"insert","lines":["postgres://ptolycsujunxhe:15c05ecda410b11dfd943c9e92ac9f06afa88cdc4de21b3bfbc7b8298cc9b7c5@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d47n3fm8rtvugs"],"id":38}],[{"start":{"row":83,"column":0},"end":{"row":83,"column":161},"action":"insert","lines":["postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562"],"id":39}],[{"start":{"row":84,"column":47},"end":{"row":84,"column":207},"action":"remove","lines":["postgres://ptolycsujunxhe:15c05ecda410b11dfd943c9e92ac9f06afa88cdc4de21b3bfbc7b8298cc9b7c5@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d47n3fm8rtvugs"],"id":40}],[{"start":{"row":84,"column":47},"end":{"row":84,"column":208},"action":"insert","lines":["postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562"],"id":41}],[{"start":{"row":82,"column":2},"end":{"row":83,"column":161},"action":"remove","lines":["","postgres://tuscuncqxjfemg:8316120671d74a3b42adf1e010c9ce26a986d66b2d35e1ed264847c0bf315a6a@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/daj1rlf3h5q562"],"id":42}],[{"start":{"row":16,"column":70},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":43},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":19,"column":0},"end":{"row":29,"column":1},"action":"insert","lines":["BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.9/howto/static-files/","STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')","STATIC_URL = '/static/'","","# Extra places for collectstatic to find static files.","STATICFILES_DIRS = (","    os.path.join(BASE_DIR, 'static'),",")"],"id":44}],[{"start":{"row":18,"column":0},"end":{"row":20,"column":0},"action":"remove","lines":["","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))",""],"id":45}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":23},"action":"remove","lines":["STATIC_URL = '/static/'"],"id":46}]]},"ace":{"folds":[],"scrolltop":180,"scrollleft":0,"selection":{"start":{"row":22,"column":0},"end":{"row":22,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"state":"start","mode":"ace/mode/python"}},"timestamp":1564439013720}
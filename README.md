# Module Python - Projet

## Objectifs

+ Extraction des données (Selenium) 
+ Conversion des données avec pandas et push sur la base de donnée Mongogb
+ API (Flask)
+ Dashboard Streamlit  

## Pré-requis

```
pip install requests pandas selenium pymongo matplotlib streamlit st_aggrid plotly
```


## Comment utiliser le projet en local ?

1. Cloner le depot

```
git clone https://github.com/FeitanSama/ynov_b3_module_python_projet/
```

2. Télécharger la version du chrome driver associé à votre navigateur et le remplacer dans dossier

```
https://chromedriver.chromium.org/downloads
```

3. Installer Mangodb sur votre machine

```
https://www.mongodb.com/
```

4. Démarrer la base de donnée Mongodb dans le terminal 

```
mongo #mac/linux
mongod #windows
```

5. Lancer le premier script : data_scraper.py (/!\ le scrapping prend environ 20 minutes)

```
python3 data_scraper.py
```

6. Lancer le deuxième script : load_data_in_mongo.py

```
python3 load_data_in_mongo.py
```

7. Lancer le troisème script : api.py

```
python3 api.py
```

8. Lancer le quatrième script : app.py

```
streamlit run app.py
```

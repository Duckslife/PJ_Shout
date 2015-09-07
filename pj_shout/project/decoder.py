import yaml
import codecs
dbconfig = yaml.load(codecs.open('config/dbconfig.yaml', 'r'))
mysql = dbconfig['mysql']

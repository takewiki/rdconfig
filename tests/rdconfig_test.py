from rdconfig.config import Config

cfg = Config(file_name='db.ini')
data = cfg.read_ini(node_name='mysql')
print(data)



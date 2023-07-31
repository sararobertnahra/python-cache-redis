import uvicorn, fastapi, os, redis, time

#Essa função pode ser substituída por uma função que conecta com o banco de dados e busca por uma chave-valor
def getValorBancoDeDados():
    return os.environ['CASA']

def getRedis():
    retries = 5
    while True:
        try:
            #os.environ['REDIS']
            r = redis.Redis(host='redis', port=6379)
            r.ping()
            return r
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

app = fastapi.FastAPI()

@app.get("/hello")
def handlesara():
    try:
        key = "MinhaVariávelÉ"
        r = getRedis()
        value = r.get(key)
        if value is None:
            value = getValorBancoDeDados()
            r.set(key,value,ex=2)
        return {key:value}
    except redis.exceptions.ConnectionError as exc:
        return {"erro", "Falha na conexão com o Redis."}

def start():
    uvicorn.run(app,host="0.0.0.0",port=5000)
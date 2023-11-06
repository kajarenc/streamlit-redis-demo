# streamlit-redis-demo

Demo repo for streamlit-redis

#### Use streamlit wheel file from this repository

`./.streamlit/config.toml`

```
[global]
useCustomCacheStorageManager=true
customCacheStorageManagerClass="streamlit_redis.RedisCacheStorageManager"
```

`./.streamlit/secrets.toml`

```
[streamlit_redis]
dsn = "redis://localhost:6379/1"
```

To run docker redis container:

```bash
docker run --name redis -p 6379:6379 -d redis
```

To run streamlit app with memray profiling:

```bash
memray run -m streamlit run demo_app.py
```

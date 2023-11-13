# streamlit-redis-demo

Demo repo for streamlit-redis

#### Use streamlit wheel file from this repository

`./.streamlit/config.toml`

```toml
[global]
useCustomCacheStorageManager=true
customCacheStorageManagerClass="streamlit_redis.RedisCacheStorageManager"
```

`./.streamlit/secrets.toml`

```toml
[streamlit_redis]
app_prefix = "unique_app_prefix"
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

or just without profiling:

```bash
streamlit run demo_app.py
```

# Configuration file for Superset
import os

# Connection to metadata database
SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('SUPERSET_META_USER')}:{os.getenv('SUPERSET_META_PASS')}@metadata_db:{os.getenv('SUPERSET_META_PORT')}/superset"

# Secret key for session management
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "default_secret_key")

FEATURE_FLAGS = {
    "HORIZONTAL_FILTER_BAR": True,
    "ENABLE_TEMPLATE_PROCESSING": True
}

####### Superset Customization ######
## Set up a path for the Home page when a logo icon is pressed
# LOGO_TARGET_PATH = "https://superset.apache.org/"

## Change logo width
LOGO_WIDTH = 200

## Change the logo image
APP_ICON = "/static/assets/images/custom_logos/logo.png"

## Set up a text next to the logo
LOGO_RIGHT_TEXT = "Operation Group"

## Set up a tooltop text for the logo
LOGO_TOOLTIP = "Navigates to superset landing page"

## Set up a favourite icon
FAVICONS = [{"href": "/static/assets/images/custom_logos/favicon.png"}]

## Change name of the tab
APP_NAME = "LOTTE Operation"

# Sử dụng tên container 'superset_cache' mà chúng ta đã đặt trong docker-compose
REDIS_HOST = "superset_cache"
REDIS_PORT = "6379"

# Cấu hình Caching chung (Metadata, Filter state)
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 86400, # 1 ngày
    "CACHE_KEY_PREFIX": "superset_cache_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": 1,
}

# Cấu hình Caching cho dữ liệu Chart (Giúp load chart nhanh hơn)
DATA_CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 86400,
    "CACHE_KEY_PREFIX": "superset_data_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": 2,
}

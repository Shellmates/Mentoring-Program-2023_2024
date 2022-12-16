# script.py
DEBUG = True

# GCP project
INSTANCE_NAME = "mp-haproxy-instance"
INSTANCE_ZONE = "europe-west1-b"
HAPROXY_USER = "root"
PROJECT_ID = "mentoring-program-371116"

# HAProxy config
STATS_PORT = 8080
STATS_USER = "shellmates"
STATS_PASSWORD = "4YALhtxXP4qAsqPNxRinok0UeXDu6H"
DOMAIN_NAME = ""
HAPROXY_ROOT = "/etc/haproxy"
HAPROXY_MAPS_ROOT = f"{HAPROXY_ROOT}/maps"
HTTP_HOSTS_MAP = "http-hosts.map"
SNI_MAP = "sni.map"
HTTP_HOSTS_MAP_PATH = f"{HAPROXY_MAPS_ROOT}/{HTTP_HOSTS_MAP}"
SNI_MAP_PATH = f"{HAPROXY_MAPS_ROOT}/{SNI_MAP}"
SSL_CERTIFICATE_PATH = f"/etc/haproxy/{DOMAIN_NAME}.pem"
NODES = [
    {
        "name": "node1",
        "ip": "10.132.0.5"
    },
]
HTTP_TYPE = "http"
TCP_TYPE = "tcp"
CHALLENGES_JSON_PATH = "config/chals.json"
TEMPLATES_DIR = "templates"
HAPROXY_CFG = "haproxy.cfg"
HAPROXY_CONFIG_DIR = "config/haproxy"
DEPLOY = True

# Helm config
USE_REMOTE_REPO = False
HELM_REGISTRY = ""
HELM_CHART_REPO = "helm-charts/ctf-challenge-chart"
HELM_CHART_VERSION = "0.1.0"

# IP blacklisting
IP_BAN_MINUTES = 2 # 2 minutes
CONN_RATE_SECONDS = 30 # 30 seconds
CONNS_PER_RATE = 50 # allow at most 50 connections in a 30s window (per IP)
CONCUR_CONNS = 25 # allow at most 25 concurrent connections (per IP)

# CTFd decay
DECAY = 50
MAX_NODES = 1
# NODES_FQDN = "gke-nodes.internal"
NODES_FQDN = "10.132.0.5"
CTFD_LINK = "http://ctf.shellmates.club/"

# challenge.py
NODEPORT_START = 30000
PORT_MOD = 1000
PORTS_PATH = "config/ports.yml"
YML_FILE = "challenge.yml"
INDENT = 4
CHAL_DIRS = {
    "crypto",
    "forensics",
    "jail",
    "linux",
    "misc",
    "osint",
    "pwn",
    "reverse",
    "web",
    "general-skills",
    "sanity-check",
}
AUTOBAN_DEFAULT = False
FW_PRIORITY = 1000
FW_SOURCE_RANGES = "0.0.0.0/0"
FW_TARGET_TAGS = "haproxy"
FW_SKIP_CHECK = False
DYNAMIC_CHAL_TYPE = "dynamic"
DOCKER_CHAL_TYPE = "docker"
PORT_PLACE_HOLDER = "${PORT}"
PROJECT_ID_PLACE_HOLDER = "${PROJECT_ID}"

# Override existing challenges in chals.json
OVERRIDE_CHALS_JSON = True

# Override existing firewall rules
OVERRIDE_FW = False
DEFAULT_DELETE_FW = False
GCR_REPO = f"gcr.io/{PROJECT_ID}"
DOCKERFILE_DIRS = {
    ".",
    "challenge",
    "app",
}
DOCKERFILE_NAME = "Dockerfile"

# ctfcli
CTFCLI_CMD = "ctf"
CTFCLI_CHAL_TRACKER_PATH = "config/ctfcli_chals.json"
CHSTATE_VISIBLE = "visible"
CHSTATE_HIDDEN = "hidden"

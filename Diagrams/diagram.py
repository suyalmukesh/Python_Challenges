from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

DIAGRAM_PATH = "/Applications/MyData/MY_DEVELOPMENT_WORK/dev_work/Python_Challenges/Diagrams/MY_DIAGRAMS/"

DIAGRAM_NAME = "Clustered Web Services"

with Diagram(F"{DIAGRAM_PATH}/{DIAGRAM_NAME}", show=False):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        svc_group = [ECS("web1"),
                     ECS("web2"),
                     ECS("web3")]

    with Cluster("DB Cluster"):
        db_primary = RDS("userdb")
        db_primary - [RDS("userdb ro")]

    memcached = ElastiCache("memcached")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached
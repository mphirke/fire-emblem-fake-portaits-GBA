import os
import subprocess

resultdir = "results/"

if "network-snapshot-000636.pkl" not in os.listdir():
    url = "11zlhXogZ7xHfTpG35MNYzcVU6CcfVFdJ"
    output = "network-snapshot-000636.pkl"
    print("Pkl model not found, downloading...")
    subprocess.run("gdown --id " + url, shell=True)

if "network-snapshot-000480.pkl" not in os.listdir():
    url = "106iquKT4Hpkl578qSTSmrkiqxOAdbsog"
    output = "network-snapshot-000480.pkl"
    print("Pkl model not found, downloading...")
    subprocess.run("gdown --id " + url, shell=True)

if "network-snapshot-000624.pkl" not in os.listdir():
    url = "11wiWBtYSg2lQGJcSm_uykqLcm7wh8xgp"
    output = "network-snapshot-000624.pkl"
    print("Pkl model not found, downloading...")
    subprocess.run("gdown --id " + url, shell=True)

if "network-snapshot-000612.pkl" not in os.listdir():
    url = "11v44jDzlrDhKuG6GmpQNinpLvWthujR9"
    output = "network-snapshot-000612.pkl"
    print("Pkl model not found, downloading...")
    subprocess.run("gdown --id " + url, shell=True)

if "network-snapshot-000492.pkl" not in os.listdir():
    url = "10B2hZS8-NGiuLLNxagZYkkqL1qI0dYdl"
    output = "network-snapshot-000492.pkl"
    print("Pkl model not found, downloading...")
    subprocess.run("gdown --id " + url, shell=True)

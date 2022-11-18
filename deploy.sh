docker build -t simeonch7/multi-client:latest -t simeonch7/multi-client:$SHA -f ./client/Dockerfile ./client
docker build -t simeonch7/multi-server:latest -t simeonch7/multi-server:$SHA -f ./server/Dockerfile ./server
docker build -t simeonch7/multi-worker:latest -t simeonch7/multi-worker:$SHA -f ./worker/Dockerfile ./worker

docker push simeonch7/multi-client:latest
docker push simeonch7/multi-client:$SHA

docker push simeonch7/multi-server:latest
docker push simeonch7/multi-server:$SHA

docker push simeonch7/multi-worker:latest
docker push simeonch7/multi-worker:$SHA

kubectl apply -f k8s

kubectl set image deployments/client-deployment client=simeonch7/multi-client:$SHA
kubectl set image deployments/server-deployment server=simeonch7/multi-server:$SHA
kubectl set image deployments/worker-deployment worker=simeonch7/multi-worker:$SHA
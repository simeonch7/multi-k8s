docker build -t simeonch7/multi-client:latest -t simeonch7/multi-client:$SHA -f ./client/Dockerfile ./client
docker build -t simeonch7/multi-server:latest -t simeonch7/multi-server:$SHA -f ./server/Dockerfile ./server
docker build -t simeonch7/multi-worker:latest -t simeonch7/multi-worker:$SHA -f ./worker/Dockerfile ./worker

docker build -t simeonch7/mongodb:latest -t simeonch7/mongodb:$SHA -f ./mongodb/Dockerfile ./mongodb
docker build -t simeonch7/parser:latest -t simeonch7/parser:$SHA -f ./parser/Dockerfile ./parser

docker push simeonch7/multi-client:latest
docker push simeonch7/multi-client:$SHA

docker push simeonch7/multi-server:latest
docker push simeonch7/multi-server:$SHA

docker push simeonch7/multi-worker:latest
docker push simeonch7/multi-worker:$SHA

docker push simeonch7/mongodb:latest
docker push simeonch7/mongodb:$SHA

docker push simeonch7/parser:latest
docker push simeonch7/parser:$SHA

kubectl apply -f k8s

kubectl set image deployments/client-deployment client=simeonch7/multi-client:$SHA
kubectl set image deployments/server-deployment server=simeonch7/multi-server:$SHA
kubectl set image deployments/worker-deployment worker=simeonch7/multi-worker:$SHA

kubectl set image deployments/parser-deployment parser=simeonch7/parser:$SHA
kubectl set image deployments/mongodb-deployment mongodb=simeonch7/mongodb:$SHA
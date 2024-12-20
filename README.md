# Run Frontend and Backend
Group Persian Gulf
Anna Chevychalova, Jack Wyett, George Lavas, Xiang Wang and Jette Anders

## Start frontend

inside folder frontend

```sh
yarn install
yarn dev --host
```

## Start backend

inside folder backend

```sh
func start
```


# Publish Frontend and Backend to Azure

## Frontend

Inside folder frontend

Build Frontend
```sh
yarn build
```

Upload to azure

```sh
az storage blob upload-batch --destination '$web' --source dist --overwrite --connection-string {connection_string}

```

## Backend

Login into azure

```sh
az login
```

Publish backend from with backend folder

```sh
func azure functionapp publish persiangulfpredictionapp \
  --python \
  --build remote
```
